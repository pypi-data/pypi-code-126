#!/usr/bin/env python

import click


@click.command()
@click.option("--fin", '-i', help="input file name")
@click.option("--fout", '-o', default='out.txt', help="output file name")
def main(fin, fout):
    print("Input: {}\nOutput: {}".format(fin, fout))


if __name__ == '__main__':
    main()