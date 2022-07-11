"""
LX-Tokenizer v{version}

Segments text into lexically relevant tokens.

usage: {program} [options] [<input-file> [<output-file>]]

Options:
    -d, --debug   Print debug information to stderr.
    -p, --plain   Assume that input file is plain text with one sentence per line.

Unless --plain is given, the input file is expected to be formatted according to
CINTIL format, ie sentences wrapped within <s> and </s> tags and paragraphs wrapped
within <p> and </p> tags.  Warning: it is not advisable to create artificial
paragraphs containing whole documents since paragraphs are loaded into memory and
processed as a whole.

The output will always be in CINTIL format.  If --plain is given, then each input
line will be considered a paragraph.

"""

import logging
import os.path
import sys

from docopt import docopt
from openfile import openfile
from lxtokenizer import LxTokenizer, __version__
from lxcommon import CintilFormatSpec, read_cintil_paragraphs


PROGNAME = os.path.basename(sys.argv[0])
LOGGER = logging.getLogger(PROGNAME)


def sanitize_plain_input_line(linenum, line):
    for tag in ["<p>", "</p>", "<s>", "</s>"]:
        if tag in line:
            LOGGER.warning(f"removed {tag!r} from input line {linenum}")
            line = line.replace(tag, "")
    return line


def read_plain_input(input_file):
    for linenum, line in enumerate(map(str.strip, input_file), start=1):
        line = sanitize_plain_input_line(linenum, line)
        yield f"<p><s>{line}</s></p>"


def main(argv=None):
    args = docopt(__doc__.format(program=PROGNAME, version=__version__), argv=argv)
    input_file = openfile(args["<input-file>"], "rt")
    output_file = openfile(args["<output-file>"], "wt")
    read_input = read_plain_input if args["--plain"] else read_cintil_paragraphs
    output_format_spec = CintilFormatSpec(pos=False)
    with input_file, output_file, LxTokenizer() as tokenizer:
        for plain_paragraph in read_input(input_file):
            lxparagraph = tokenizer.tokenize_paragraph(plain_paragraph)
            lxparagraph.write_cintil(output_file, output_format_spec)


if __name__ == "__main__":  # pragma: no cover
    main()
