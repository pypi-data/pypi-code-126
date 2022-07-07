#!/usr/bin/env python
# coding: utf8

"""
    A pure python ping implementation using raw socket.


    Note that ICMP messages can only be sent from processes running as root.


    Derived from ping.c distributed in Linux's netkit. That code is
    copyright (c) 1989 by The Regents of the University of California.
    That code is in turn derived from code written by Mike Muuss of the
    US Army Ballistic Research Laboratory in December, 1983 and
    placed in the public domain. They have my thanks.

    Bugs are naturally mine. I'd be glad to hear about them. There are
    certainly word - size dependencies here.

    Copyright (c) Matthew Dixon Cowles, <http://www.visi.com/~mdc/>.
    Distributable under the terms of the GNU General Public License
    version 2. Provided with no warranties of any sort.

    Original Version from Matthew Dixon Cowles:
      -> ftp://ftp.visi.com/users/mdc/ping.py

    Rewrite by Jens Diemer:
      -> http://www.python-forum.de/post-69122.html#69122

    Rewrite by Anton Belousov / Stellarbit LLC <anton@stellarbit.com>
       -> http://github.com/stellarbit/aioping

    Modified by Mark Guagenti to work with Tornadio and Python 2.7
       -> https://github.com/mgenti/tornado-ping

    Revision history
    ~~~~~~~~~~~~~~~~

    November 22, 1997
    Initial hack. Doesn't do much, but rather than try to guess
    what features I (or others) will want in the future, I've only
    put in what I need now.

    December 16, 1997
    For some reason, the checksum bytes are in the wrong order when
    this is run under Solaris 2.X for SPARC but it works right under
    Linux x86. Since I don't know just what's wrong, I'll swap the
    bytes always and then do an htons().

    December 4, 2000
    Changed the struct.pack() calls to pack the checksum and ID as
    unsigned. My thanks to Jerome Poincheval for the fix.

    May 30, 2007
    little rewrite by Jens Diemer:
     -  change socket asterisk import to a normal import
     -  replace time.time() with time.clock()
     -  delete "return None" (or change to "return" only)
     -  in checksum() rename "str" to "source_string"

    March 11, 2010
    changes by Samuel Stauffer:
    - replaced time.clock with default_timer which is set to
      time.clock on windows and time.time on other systems.

    Januari 27, 2015
    Changed receive response to not accept ICMP request messages.
    It was possible to receive the very request that was sent.

    January 15, 2017
    Changes by Anton Belousov / Stellarbit LLC
    - asyncio & python 3.5+ adaptaion
    - PEP-8 code reformatting

    June 29, 2022
    Changes by Mark Guagenti
    - tornadio & python 2.7 adaptation

    Last commit info:
    ~~~~~~~~~~~~~~~~~
    $LastChangedDate: $
    $Rev: $
    $Author: $
"""
import logging
import random
import socket
import uuid
import struct
import timeit
import functools
import datetime

import tornado
from tornado import gen
from tornado.netutil import Resolver
from tornado.tcpclient import _Connector
from tornado.concurrent import Future
from tornado.platform.auto import set_close_exec
from tornado.util import TimeoutError

# ICMP types, see rfc792 for v4, rfc4443 for v6
ICMP_ECHO_REQUEST = 8
ICMP6_ECHO_REQUEST = 128
ICMP_ECHO_REPLY = 0
ICMP6_ECHO_REPLY = 129

proto_icmp = socket.getprotobyname("icmp")
proto_icmp6 = socket.getprotobyname("ipv6-icmp")

log = logging.getLogger(__name__)


def checksum(buffer):
    """
    I'm not too confident that this is right but testing seems
    to suggest that it gives the same answers as in_cksum in ping.c
    :param buffer:
    :return:
    """
    sum = 0
    count_to = (len(buffer) / 2) * 2
    count = 0

    while count < count_to:
        this_val = ord(buffer[count + 1]) * 256 + ord(buffer[count])
        sum += this_val
        sum &= 0xffffffff  # Necessary?
        count += 2

    if count_to < len(buffer):
        sum += ord(buffer[len(buffer) - 1])
        sum &= 0xffffffff  # Necessary?

    sum = (sum >> 16) + (sum & 0xffff)
    sum += sum >> 16
    answer = ~sum
    answer &= 0xffff

    # Swap bytes. Bugger me if I know why.
    answer = answer >> 8 | (answer << 8 & 0xff00)

    return answer


@gen.coroutine
def receive_one_ping(my_socket, id_, timeout):
    """
    receive the ping from the socket.
    :param my_socket:
    :param id_:
    :param timeout:
    :return:
    """
    future = Future()
    tornado.ioloop.IOLoop.current().add_handler(my_socket.fileno(),
                                                lambda fd, events: future.set_result(True),
                                                tornado.ioloop.IOLoop.READ)
    yield future

    try:
        while True:
            rec_packet = my_socket.recv(1024)
            time_received = timeit.default_timer()

            if my_socket.family == socket.AF_INET:
                offset = 20
            else:
                offset = 0

            icmp_header = rec_packet[offset:offset + 8]

            type, code, checksum, packet_id, sequence = struct.unpack(
                "bbHHh", icmp_header
            )

            if type != ICMP_ECHO_REPLY and type != ICMP6_ECHO_REPLY:
                continue

            if packet_id == id_:
                data = rec_packet[offset + 8:offset + 8 + struct.calcsize("d")]
                time_sent = struct.unpack("d", data)[0]

                tornado.ioloop.IOLoop.current().remove_handler(my_socket.fileno())
                raise gen.Return(time_received - time_sent)
    except OSError:
        tornado.ioloop.IOLoop.current().remove_handler(my_socket.fileno())
        my_socket.close()

        raise TimeoutError("Ping timeout")


def sendto_ready(packet, socket, future, dest):
    try:
        socket.sendto(packet, dest)
    except OSError as exc:
        return  # The callback will be retried
    except Exception as exc:
        tornado.ioloop.IOLoop.current().remove_handler(socket.fileno())
        future.set_exception(exc)
    else:
        tornado.ioloop.IOLoop.current().remove_handler(socket.fileno())
        future.set_result(None)


@gen.coroutine
def send_one_ping(my_socket, dest_addr, id_, timeout, family):
    """
    Send one ping to the given >dest_addr<.
    :param my_socket:
    :param dest_addr:
    :param id_:
    :param timeout:
    :return:
    """
    icmp_type = ICMP_ECHO_REQUEST if family == socket.AF_INET else ICMP6_ECHO_REQUEST

    # Header is type (8), code (8), checksum (16), id (16), sequence (16)
    my_checksum = 0

    # Make a dummy header with a 0 checksum.
    header = struct.pack("BbHHh", icmp_type, 0, my_checksum, id_, 1)
    bytes_in_double = struct.calcsize("d")
    data = (192 - bytes_in_double) * "Q"
    data = struct.pack("d", timeit.default_timer()) + data.encode("ascii")

    # Calculate the checksum on the data and the dummy header.
    my_checksum = checksum(header + data)

    # Now that we have the right checksum, we put that in. It's just easier
    # to make up a new header than to stuff it into the dummy.
    header = struct.pack(
        "BbHHh", icmp_type, 0, socket.htons(my_checksum), id_, 1
    )
    packet = header + data

    future = Future()
    callback = functools.partial(sendto_ready, packet=packet, socket=my_socket, dest=dest_addr, future=future)
    tornado.ioloop.IOLoop.current().add_handler(my_socket.fileno(),
                                                lambda fd, events: callback(),
                                                tornado.ioloop.IOLoop.WRITE)

    yield future


@gen.coroutine
def ping(dest_addr, timeout=10, family=None):
    """
     Returns either the delay (in seconds) or raises an exception.
     :param dest_addr:
     :param timeout:
     :param family:
     """
    resolver = Resolver()
    try:
        addrinfo = yield gen.with_timeout(datetime.timedelta(seconds=timeout),
                                          resolver.resolve(dest_addr, 0))
    except socket.gaierror as ex:
        log.debug("Unable to resolve %s" % dest_addr, exc_info=1)
        raise gen.Return(None)

    log.debug("%s getaddrinfo result=%s", dest_addr, addrinfo)

    primary_addrs, secondary_addrs = _Connector.split(addrinfo)
    family, addr = random.choice(primary_addrs)

    log.debug("%s resolved addr=%s", dest_addr, addr)

    if family == socket.AF_INET:
        icmp = proto_icmp
    else:
        icmp = proto_icmp6

    try:
        my_socket = socket.socket(family, socket.SOCK_RAW, icmp)
        my_socket.setblocking(False)
        set_close_exec(my_socket.fileno())
    except OSError as e:
        msg = e.strerror

        if e.errno == 1:
            # Operation not permitted
            msg += (
                " - Note that ICMP messages can only be sent from processes"
                " running as root."
            )

            raise OSError(msg)

        raise

    my_id = uuid.uuid4().int & 0xFFFF

    yield send_one_ping(my_socket, addr, my_id, timeout, family)
    try:
        recv_ping = receive_one_ping(my_socket, my_id, timeout)
        delay = yield gen.with_timeout(datetime.timedelta(seconds=timeout),
                                       recv_ping)
    except TimeoutError:
        gen.Return(None)
    my_socket.close()

    raise gen.Return(delay)


@gen.coroutine
def verbose_ping(dest_addr, timeout=2, count=3, family=None):
    """
    Send >count< ping to >dest_addr< with the given >timeout< and display
    the result.
    :param dest_addr:
    :param timeout:
    :param count:
    :param family:
    """
    responses = []

    for i in range(count):
        delay = None

        try:
            delay = yield ping(dest_addr, timeout, family)
        except TimeoutError as e:
            log.error("%s timed out after %ss" % (dest_addr, timeout))
        except Exception as e:
            log.error("%s failed: %s" % (dest_addr, str(e)))
            break

        responses.append(delay)

        if delay is not None:
            delay *= 1000
            log.info("%s get ping in %0.4fms" % (dest_addr, delay))

    raise gen.Return(responses)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    tornado.ioloop.IOLoop.instance().run_sync(lambda: verbose_ping('8.8.8.8'))

    @gen.coroutine
    def do_ping(host):
        delay = yield ping(host)
        if delay:
            print "Ping response in %s ms" % (delay * 1000, )
        else:
            print "Timed out"


    tornado.ioloop.IOLoop.instance().run_sync(lambda: do_ping('8.8.8.8'))
