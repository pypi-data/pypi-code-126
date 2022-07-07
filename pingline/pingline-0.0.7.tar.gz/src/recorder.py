import csv
import re
import time
import subprocess


class Recorder:
    PING_REGEX = rb"time=([\d.]+) ms"

    class PacketLossException(Exception):
        pass

    def __init__(self, interval, hosts, log_file) -> None:
        self.interval = interval
        self.hosts = hosts
        self.log_file = log_file

    @staticmethod
    def comma_fmt(number):
        return str(number).replace(".", ",")

    @staticmethod
    def start_ping(host: str) -> subprocess.Popen:
        return subprocess.Popen(["ping", "-c 1", host], stdout=subprocess.PIPE)

    def read_ping(self, process: subprocess.Popen):
        response, _ = process.communicate()
        match = re.search(self.PING_REGEX, response)

        if match is None:
            raise self.PacketLossException()

        return float(match.group(1))

    def ping_loop(self, fileobj):
        ping_csv = csv.DictWriter(
            fileobj,
            fieldnames=["timestamp", *[f"{alias}_ping" for alias in self.hosts.keys()]],
            delimiter=";",
        )

        if not fileobj.tell():
            ping_csv.writeheader()

        while True:
            measure_start = time.time()

            processes = {}
            for alias, host in self.hosts.items():
                processes[alias] = self.start_ping(host)

            pings = {}
            for alias, host in self.hosts.items():
                key = f"{alias}_ping"
                try:
                    value = self.read_ping(processes[alias])
                except self.PacketLossException:
                    value = -1
                pings[key] = self.comma_fmt(value)

            ping_csv.writerow({"timestamp": self.comma_fmt(measure_start), **pings})
            fileobj.flush()

            time.sleep(self.interval)

    def start(self):
        with open(self.log_file, "a") as ping_log:
            self.ping_loop(ping_log)
