# -*- coding: utf-8 -*-
import os
from rich.progress import track
import click


@click.group()
def main():
    pass


@main.command()
@click.argument("input_file")
@click.option("-n", "--nums", default=5, help="Number of split files")
def filesplit(input_file, nums):
    input_file = os.path.abspath(input_file)
    file_dir = os.path.dirname(input_file)
    if not os.path.exists(input_file):
        click.echo("Input file not exists")
        return

    filename, fext = os.path.basename(input_file).split(".")
    with open(input_file) as fp:
        files = [open(os.path.join(file_dir, f"{filename}-{i}.{fext}"), "w") for i in range(nums)]
        for i, line in enumerate(track(fp.readlines(), description="Splitting files")):
            files[i % nums].write(line)
        for f in files:
            f.close()


if __name__ == "__main__":
    main()
