"""
LX-SentenceSplitter v{version}

Marks sentence boundaries with <s>…</s>, and paragraph boundaries
with <p>…</p>. Unwraps sentences split over different lines.

A f-score of 99.94% was obtained when testing on a 12,000 sentence
corpus accurately hand tagged with respect to sentence and paragraph
boundaries.

usage: lx-sentencesplitter [options] [<input-file> [<output-file>]]

Options:
  -D, --debug      Print debug information to stderr.
  -T, --no-tags    Print sentences one per line, without <s>...</s>
                   tags and paragraphs separated by empty lines.
  -B, --blank-line-paragraphs
                   Assume paragraphs are separated by an empty line.

"""

import logging
import sys

from docopt import docopt
from openfile import openfile
from lxcommon import CintilFormatSpec
from lxsentencesplitter import LxSentenceSplitter, __version__


def write_plain_paragraphs(paragraphs, file=sys.stdout):
    paragraphs = iter(paragraphs)  # ensure paragraphs is an iterator
    # print first par without leading empty line
    for paragraph in paragraphs:
        for sentence in paragraph:
            print(sentence.raw, file=file)
        break  # break after printing first par
    for paragraph in paragraphs:  # print next paragraphs
        print(file=file)  # with leading empty line
        for sentence in paragraph:
            print(sentence.raw, file=file)


def write_cintil_paragraphs(paragraphs, file=sys.stdout):
    cintil_format = CintilFormatSpec(tokenized=False)
    for paragraph in paragraphs:
        print(paragraph.to_cintil(cintil_format), file=file)


def main(argv=None):
    args = docopt(__doc__.format(version=__version__), version=__version__, argv=argv)
    logging.basicConfig(level=logging.DEBUG if args["--debug"] else logging.WARNING)
    splitter = LxSentenceSplitter(
        paragraphs_separated_by_empty_line=args["--blank-line-paragraphs"],
    )
    with splitter:
        with openfile(args["<input-file>"], "rt") as input_file:
            with openfile(args["<output-file>"], "wt") as output_file:
                paragraphs = splitter.isplit(input_file)
                if args["--no-tags"]:
                    write_plain_paragraphs(paragraphs, output_file)
                else:
                    write_cintil_paragraphs(paragraphs, output_file)


if __name__ == "__main__":  # pragma: no cover
    main()
