import serial
import time
import struct
from dataclasses import dataclass
from typing import Optional
import select
from threading import Lock
from queue import Queue, Empty

# ha eltűnik egy device, akkor crashelük a faszba... evvan

# glossary:
# header: that 7 bytes
# payload: usable data
# packet: header + payload
# frame: 0x69 + packet

HEADER_LEN = 7
HEADER_WITHOUT_CHECKSUM_LEN = 6
HEADER_FORMAT = ">ccBBHc"
HEADER_WITHOUT_CHECKSUM_FORMAT = ">ccBBH"


@dataclass
class DeviceWrapper:
    dev: serial.Serial
    buf: bytes
    last_new_bytes: float = 0
    last_successful_pop: float = 0

    @property
    def name(self) -> str:
        return self.dev.name

    def is_rotten(self, time_now: Optional[float] = None):
        if len(self.buf) == 0:
            return False

        if not time_now:
            time_now = time.time()

        return ((time_now - self.last_new_bytes) > 2.0) and ((time_now - self.last_successful_pop) > 4.0)

    def perform_read(self):
        buf = self.dev.read(size=65536)  # this has a 50ms timeout
        self.buf += buf
        self.last_new_bytes = time.time()

    # needed for select
    def fileno(self) -> int:
        return self.dev.fileno()

    def __hash__(self):
        return hash(self.dev)


@dataclass
class LUTEntry:
    srv: bytes
    device: DeviceWrapper
    ttd: int
    last_seen: float  # as returned by time.time()


@dataclass
class KeepaliveStats:
    last_sent: float
    counter: int = 1


@dataclass
class BufferedCallback:
    src_srv: bytes
    dst_srv: bytes
    payload: bytes
    is_broadcast: bool = False


class Line:
    # LINE Is Not Efficient
    def __init__(self, srv: bytes, devices: list[str], max_ttd: int):

        if len(srv) > 1:
            raise ValueError("srv have to be 1 byte long")

        self._srv: bytes = srv
        self._buffers: dict[serial.Serial, bytes] = {}
        self._devices: list[DeviceWrapper] = []
        self._lut: list[LUTEntry] = []
        self._max_ttd: int = max_ttd
        self._callbacks: list[callable] = []
        self._broadcast_callbacks: dict[bytes, list[callable]] = {}

        self._last_keepalive: float = 0
        self._keepalives_sent: dict[bytes, KeepaliveStats] = {}

        for device in devices:
            devw = DeviceWrapper(
                dev=serial.Serial(port=device, baudrate=9600, timeout=0.05),
                buf=b"",
                last_new_bytes=0,
                last_successful_pop=0
            )
            self._devices.append(
                devw
            )

        self._lock = Lock()
        self._callback_queue = Queue()

        self._stat_sent_packets: int = 0
        self._stat_forwarded_packets: int = 0
        self._stat_processed_packets: int = 0
        self._stat_dropped_packets: int = 0
        self._stat_broadcast_packets: int = 0
        self._stat_garbage_bytes: int = 0
        self._stat_recv_nullpackets: int = 0
        self._stat_buffer_process_timeouts: int = 0
        self._stat_callback_process_timeouts: int = 0
        self._stat_buffer_rots: int = 0

    @staticmethod
    def _xor_all(input_bytes: bytes) -> bytes:
        a = 0
        for b in input_bytes:
            a ^= b
        return bytes([a])

    @staticmethod
    def _append_checksum(header_without_checksum: bytes) -> bytes:
        checksum = Line._xor_all(header_without_checksum)
        header = header_without_checksum + checksum
        return header

    @staticmethod
    def _compile_packet(dst_srv: bytes, src_srv: bytes, ttd: int, payload: bytes) -> bytes:
        # This produces a packet not a frame (so no x64)
        header_without_checksum = struct.pack(
            HEADER_WITHOUT_CHECKSUM_FORMAT,
            dst_srv,  # <- 1 byte dst
            src_srv,  # <- 1 byte src
            ttd,  # <- ttd
            0x0,  # <- reserved
            len(payload)  # <- len
        )
        return Line._append_checksum(header_without_checksum) + payload

    #
    # Protected
    #

    def _is_lut_valid(self, entry: LUTEntry, time_now: Optional[float] = None):
        if not time_now:
            time_now = time.time()

        if (time_now - entry.last_seen) > self._max_ttd * 30:
            return False

        # Check the current state of the LUT... if there is a better entry, then this is not a valid entry.
        for e in self._lut:
            if e == entry:
                continue

            if e.srv == entry.srv:
                if e.ttd < entry.ttd:
                    return False

        return True

    def _clean_lut(self):
        new_lut: list[LUTEntry] = []
        time_now = time.time()
        for entry in self._lut:
            if self._is_lut_valid(entry, time_now):
                new_lut.append(entry)

        self._lut = new_lut

    def _update_lut(self, srv: bytes, device: DeviceWrapper, ttd: int):
        # Do not store any entry about our own service
        if srv == self._srv:
            return

        if srv[0] >= 0xC0:
            # Do not store broadcast address
            # This also causes the packet to be sent out on all interfaces
            return

        # Throw out worse entries
        new_lut = []
        for entry in self._lut:
            if entry.srv == srv:
                if entry.ttd <= ttd:
                    new_lut.append(entry)
            else:
                new_lut.append(entry)

        self._lut = new_lut

        # Update LUT if we already have this entry
        for entry in self._lut:
            if (entry.srv == srv) and (device == entry.device) and (entry.ttd == ttd):
                entry.last_seen = time.time()
                return

        # If no entry found, consider adding it to LUT
        for entry in self._lut:
            # there is a better entry in the LUT already, so don't add it
            if (entry.srv == srv) and (entry.ttd < ttd):
                return

        # No better entry found, so add it...
        new_entry = LUTEntry(
            srv=srv,
            device=device,
            ttd=ttd,
            last_seen=time.time()
        )
        self._lut.append(new_entry)

    def _find_lut_entry(self, dst_srv: bytes) -> Optional[LUTEntry]:
        candidates: list[LUTEntry] = []
        for entry in self._lut:
            if entry.srv == dst_srv:
                if self._is_lut_valid(entry):
                    candidates.append(entry)

        if len(candidates) == 0:
            return None

        candidates.sort(key=lambda x: x.ttd)  # sort in ascending order
        return candidates[0]

    def _send_packet_out(self, packet: bytes, except_to: list[DeviceWrapper], skip_lut: bool = False):
        # This is where the preamble is added
        header = packet[:HEADER_LEN]
        dst_srv, _, ttd, _, _, _ = struct.unpack(HEADER_FORMAT, header)

        if ttd >= self._max_ttd:
            # Do not send out packets with bigger ttd than the max ttd
            self._stat_dropped_packets += 1
            return

        frame = b"\x69" + packet

        dst_lut = None if skip_lut else self._find_lut_entry(dst_srv)
        actually_sent_somewhere = False
        if dst_lut:
            if dst_lut not in except_to:
                # Don't send if the device is forbidden to send to
                dst_lut.device.dev.write(frame)
                actually_sent_somewhere = True
        else:
            # if no entry found, send out on all devices
            for dev in self._devices:
                if dev not in except_to:  # Don't send if the device is forbidden to send to
                    dev.dev.write(frame)
                    actually_sent_somewhere = True

        if not actually_sent_somewhere:
            self._stat_dropped_packets += 1

    def _handle_packet(self, packet: bytes, device: DeviceWrapper):
        header = packet[:HEADER_LEN]
        payload = packet[HEADER_LEN:]
        dst_srv, src_srv, ttd, _, length, _ = struct.unpack(HEADER_FORMAT, header)

        is_broadcast = dst_srv[0] >= 0xC0

        if not is_broadcast:
            # In case the LUT have a better entry for this service
            # Then this packet is probably duplicated
            # So we just drop it
            # In case of topology change, the better entry will time out anyway
            for entry in self._lut:
                if entry.srv == src_srv:
                    if entry.ttd < entry.ttd:
                        self._stat_dropped_packets += 1
                        return

        # Update LUT first (this is needed to keep track of the source even on broadcast packets)
        self._update_lut(src_srv, device, ttd)

        # Then make a decision
        if dst_srv in ([self._srv] + list(self._broadcast_callbacks.keys())):
            if length != 0:  # do not call callbacks on nullpackets
                self._callback_queue.put(BufferedCallback(
                    src_srv=src_srv,
                    dst_srv=dst_srv,
                    payload=payload,
                    is_broadcast=is_broadcast)
                )
            else:
                self._stat_recv_nullpackets += 1
            self._stat_processed_packets += 1

        if (dst_srv != self._srv) or is_broadcast:
            # forward packet
            self._send_packet_out(self._compile_packet(dst_srv, src_srv, ttd + 1, payload), [device], is_broadcast)
            self._stat_forwarded_packets += 1

        if is_broadcast:
            self._stat_broadcast_packets += 1

    def _keepalive_periodic(self):
        # send out a keepalive packet when it's time to do so
        if not self._lut:
            return

        time_now = time.time()

        if (time_now - self._last_keepalive) <= 25:  # send keepalive every 25 sec
            return

        # keepalive sending time...

        # compile a list of all hosts that are in our lut, and assing them the time we last sent keepalive to them
        all_srvs_in_lut_with_last_keepalive_sent_time = []
        for entry in self._lut:
            if entry.srv in self._keepalives_sent.keys():
                last_keepalive_sent_to = self._keepalives_sent[entry.srv].last_sent
            else:
                last_keepalive_sent_to = 0
            all_srvs_in_lut_with_last_keepalive_sent_time.append((entry.srv, last_keepalive_sent_to))

        # order this according to the last_sent_time in ascending order
        all_srvs_in_lut_with_last_keepalive_sent_time.sort(key=lambda x: x[1])

        # choose the host with the oldest last keepalive sent
        dst_srv = all_srvs_in_lut_with_last_keepalive_sent_time[0][0]

        # send keepalive
        self._send_packet_out(self._compile_packet(dst_srv, self._srv, 0, b""), [])  # <- NULLPACKET
        self._last_keepalive = time_now

        # update stats

        if dst_srv in self._keepalives_sent:
            self._keepalives_sent[dst_srv].counter += 1
            self._keepalives_sent[dst_srv].last_sent = time_now
        else:
            self._keepalives_sent[dst_srv] = KeepaliveStats(last_sent=time_now)

    def _buffer_rot(self):
        time_now = time.time()
        for dev in self._devices:
            if dev.is_rotten(time_now):
                self._stat_garbage_bytes += len(dev.buf)
                dev.buf = b""
                self._stat_buffer_rots += 1

    def _pop_one_frame_from_buffer(self, dev: DeviceWrapper) -> Optional[bytes]:
        frame_header = 1 + HEADER_LEN  # preamble plus header length
        if len(dev.buf) < frame_header:
            # this can not possibly be a full packet
            return None

        for i in range((len(dev.buf) - frame_header) + 1):  # <- leave room for forward seeking
            if dev.buf[i] != 0x69:
                continue

            chksum = bytes([dev.buf[i + 7]])
            calculated_chksum = self._xor_all(dev.buf[i + 1:i + 7])  # xor header without checksum part
            if chksum != calculated_chksum:
                continue

            length = struct.unpack(">H", dev.buf[i + 5:i + 7])[0]
            total_frame_length = length + 8  # 8 = 7 byte header, 1 byte preamble
            if len(dev.buf) - i >= total_frame_length:
                frame = dev.buf[i:i + total_frame_length]
                dev.buf = dev.buf[i + total_frame_length:]
                self._stat_garbage_bytes += i
                dev.last_successful_pop = time.time()
                return frame

        return None

    #
    # Public
    #

    def send(self, dst_srv: bytes, payload: bytes):

        if len(dst_srv) != 1:
            raise ValueError("Destination SRV must be 1 byte long")

        packet = self._compile_packet(dst_srv, self._srv, 0, payload)
        with self._lock:
            self._send_packet_out(packet, [])
            self._stat_sent_packets += 1

    def register_callback(self, callback: callable):
        # This is an "atomic" call in python, because of the GIL (we shouldn't depend on this really)
        self._callbacks.append(callback)

    def register_broadcast_callback(self, bcast_srv: bytes, callback: callable):
        # This is not thread safe, but whatever

        if len(bcast_srv) != 1:
            raise ValueError("Address length must be 1")

        if bcast_srv[0] < 0xC0:
            raise ValueError("This is not a broadcast address")

        if bcast_srv not in self._broadcast_callbacks:
            self._broadcast_callbacks[bcast_srv] = []

        self._broadcast_callbacks[bcast_srv].append(callback)

    def get_lut(self) -> list[tuple]:
        lut_repr = []
        with self._lock:
            for entry in self._lut:
                lut_repr.append(
                    (entry.srv, entry.device.name, entry.ttd, entry.last_seen)
                )

        return lut_repr

    def get_stats(self) -> dict[str, any]:
        with self._lock:
            return {
                "buf_stat": {
                    dev.dev.name: (len(dev.buf), dev.last_new_bytes, dev.last_successful_pop) for dev in self._devices
                },
                "lut_len": len(self._lut),
                "callbacks_len": len(self._callbacks),
                "bcast_callbacks_len": sum(len(v) for k, v in self._broadcast_callbacks.items()),
                "last_keepalive_sent": self._last_keepalive,
                "max_ttd": self._max_ttd,
                "sent_packets": self._stat_sent_packets,
                "forwarded_packets": self._stat_forwarded_packets,
                "processed_packets": self._stat_processed_packets,
                "dropped_packets": self._stat_dropped_packets,
                "broadcast_packets": self._stat_broadcast_packets,
                "garbage_bytes": self._stat_garbage_bytes,
                "keepalives_sent": {k: (v.counter, v.last_sent) for k, v in self._keepalives_sent.items()},
                "recv_nullpackets": self._stat_recv_nullpackets,
                "queue_len": self._callback_queue.qsize(),
                "buffer_process_timeouts": self._stat_buffer_process_timeouts,
                "callback_process_timeouts": self._stat_callback_process_timeouts,
                "buffer_rots": self._stat_buffer_rots
            }

    @property
    def queue(self) -> Queue:
        if self._callbacks or self._broadcast_callbacks:
            raise Exception("Can not use the queue and callbacks together!")

        return self._callback_queue

    def process(self):
        with self._lock:
            # read out everything from the buffer
            for dev in self._devices:
                started = time.time()
                while frame := self._pop_one_frame_from_buffer(dev):  # this shifts the buffer
                    self._handle_packet(frame[1:], dev)  # chop off the preamble

                    if (time.time() - started) > 1.0:
                        self._stat_buffer_process_timeouts += 1
                        break

            # housekeeping
            self._clean_lut()
            self._keepalive_periodic()
            self._buffer_rot()

        if self._callbacks or self._broadcast_callbacks:
            started = time.time()
            try:
                while params := self._callback_queue.get(block=False):

                    if params.is_broadcast:
                        callbacks = self._broadcast_callbacks[params.dst_srv]
                    else:
                        callbacks = self._callbacks

                    for callback in callbacks:
                        callback(params.src_srv, params.dst_srv, params.payload)

                    if (time.time() - started) > 2.0:
                        self._stat_callback_process_timeouts += 1
                        break

            except Empty:  # The queue is empty, no callbacks needs to be called
                pass

        # we make a copy of the devices list, so we can avoid locking the whole select
        rd, _, _ = select.select(self._devices[:], [], [], 0.2)
        with self._lock:
            for dev in rd:
                dev.perform_read()

    def serve_forever(self):
        while True:
            self.process()
