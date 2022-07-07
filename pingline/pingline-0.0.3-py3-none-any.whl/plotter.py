from datetime import timedelta

import matplotlib.dates as md
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime


def plot_interactive(update_interval, show_last_n_minutes, log_file):
    ax = plt.gca()
    xfmt = md.DateFormatter("%Y-%m-%d %H:%M:%S")
    ax.xaxis.set_major_formatter(xfmt)

    plt.ion()
    plt.show()

    while True:
        ax.clear()
        df = read_csv(log_file, sep=";", decimal=",")
        df["datetime"] = to_datetime(df["timestamp"], unit="s")
        df = df.set_index("timestamp")
        end = df.index.max()
        start = end - timedelta(minutes=show_last_n_minutes).total_seconds()
        df = df.loc[start:end]

        df.plot(kind="line", x="datetime", y="router_ping", ax=ax)
        df.plot(kind="line", x="datetime", y="internet_ping", color="red", ax=ax)

        plt.gcf().canvas.draw_idle()
        plt.gcf().canvas.start_event_loop(update_interval)


def plot(log_file):
    ax = plt.gca()

    xfmt = md.DateFormatter("%Y-%m-%d %H:%M:%S")
    ax.xaxis.set_major_formatter(xfmt)

    df = read_csv(log_file, sep=";", decimal=",")
    df["datetime"] = to_datetime(df["timestamp"], unit="s")

    df.plot(kind="line", x="datetime", y="router_ping", ax=ax)
    df.plot(kind="line", x="datetime", y="internet_ping", color="red", ax=ax)

    plt.show()
