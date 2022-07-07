import fire
import pandas as pd


def datels(start, end, freq="D", format=None, sep=None):
    if format is None:
        if sep is None:
            sep = "/"
        format = sep.join(("%Y", "%m", "%d"))

    for date in pd.date_range(start=start, end=end, freq=freq):
        print(date.strftime(format))
    return


def main():
    fire.Fire(datels)


if __name__ == "__main__":
    main()
