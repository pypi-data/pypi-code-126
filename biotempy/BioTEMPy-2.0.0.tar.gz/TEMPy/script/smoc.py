"""
Example:
    To run SMOC on a model, `synthase.pdb`, and a map, `EMD-1234.mrc.gz`,
    with a window length of 11 and a resolution of 4.53 run::

        $ TEMPy.smoc -p synthase.pdb -m EMD-1234.mrc.gz -w 11 -r 4.53

    The default output of this command will be a series of files, one per
    chain, in tab separated format.  The files are named according to the
    parameters.  For examples, if synthase contains chains A, B and C, the
    following files are expected::

        smoc_EMD-1234_vs_synthase_chain-A_win-11_res-4p53_contig.tsv
        smoc_EMD-1234_vs_synthase_chain-B_win-11_res-4p53_contig.tsv
        smoc_EMD-1234_vs_synthase_chain-C_win-11_res-4p53_contig.tsv

    The output format can be changed using the '-f' flag which supports 'tsv',
    'csv' and 'json'.  For example, to select JSON output::

        $ TEMPy.smoc -p synthase.pdb -m EMD-1234.mrc.gz -w 11 -r 4.53 -f json

    This will result in a single JSON file with each chain stored under its own
    key.  The parameters used to generate the score are stored under the
    'parameters' key.  The output file name would be::

        smoc_EMD-1234_vs_synthase.json

    Two approaches to calculating sliding windows are provided, which handle
    unmodelled regions differently.  The new 'contig' based calculation creates
    sliding windows over contiguous residues.  The old method 'spans' these
    unmodelled regions.  The default method is the new 'contig' based approach,
    however this can be changed using the '--method' flag.
"""

import os
import json
import csv
import argparse
import time
import matplotlib.pyplot as plt
from TEMPy.cli.arg_parser import TEMPyArgParser
from TEMPy.protein.scoring_functions import FastSMOC


def write_plot_file(filename, chain, residue_scores):
    residues = list(residue_scores.keys())
    residues.sort()
    scores = [residue_scores[r] for r in residues]
    fig, ax = plt.subplots()
    ax.plot(residues, scores)
    ax.set_title(f"SMOC scores for chain {chain}")
    fig.savefig(filename)


def write_tabular_scores(filename, residue_scores, delimiter):
    with open(filename, "w") as tabular_file:
        tabular_writer = csv.writer(tabular_file, delimiter=delimiter)
        for k, v in sorted(residue_scores.items()):
            tabular_writer.writerow([k, v])


def write_json_scores(filename, parameters, chain_residue_scores):
    with open(filename, "w") as outfile:
        json.dump(
            {"chains": chain_residue_scores, "parameters": parameters},
            outfile,
            indent=4,
        )


def parse_window(window):
    try:
        window = int(window)
    except Exception:
        raise argparse.ArgumentTypeError("Expected an odd number")

    if window % 2 == 0:
        raise argparse.ArgumentTypeError("Expected an odd number")

    return window


def parse_method(method):
    method = method.lower()
    if method in ("span", "contig"):
        return method
    raise argparse.ArgumentTypeError("Expected method to be one of: span, contig")


def parse_format(format):
    format = format.lower()
    if format in ("tsv", "csv", "json", "pdf", "png"):
        return format
    raise argparse.ArgumentTypeError(
        "Expected format to be one of: tsv, csv, json, pdf or png"
    )


parser = TEMPyArgParser("Calculate SMOC scores")
parser.add_map_arg()
parser.add_model_arg()
parser.add_resolution_arg()

output_group = parser.parser.add_argument_group("output")
smoc_group = parser.parser.add_argument_group("smoc")

smoc_group.add_argument(
    "--smoc-window",
    dest="smoc_window",
    help="The window size. Should be odd.",
    default=11,
    type=parse_window,
)

output_group.add_argument(
    "--output-format",
    dest="output_format",
    help="Output format: CSV, TSV, JSON, PDF, PNG",
    required=True,
    default="tsv",
    type=parse_format,
)

smoc_group.add_argument(
    "--smoc-method",
    dest="smoc_method",
    help="How to handle unmodelled regions",
    required=False,
    default="contig",
    type=parse_method,
)

output_group.add_argument(
    "--output-prefix",
    dest="output_prefix",
    help="Use a custom prefix for output files",
    required=False,
    default=None,
    type=str,
)


def get_parser():
    return parser.parser


class SMOCScript:
    def __init__(self):
        args = parser.parser.parse_args()
        self.model = args.model
        self.map = args.map
        self.resolution = args.resolution
        self.window = args.smoc_window
        self.prefix = args.output_prefix
        self.output_format = args.output_format
        self.method = args.smoc_method

    def run(self):
        scorer = FastSMOC(self.model, self.map, self.resolution)
        chains = set(a.chain for a in self.model.atomList)

        chain_scores = {}
        tot_start = time.time()
        for chain in chains:
            chain_start = time.time()
            if self.method == "span":
                chain_scores[chain] = scorer.score_chain_span(chain, self.window)
            else:
                chain_scores[chain] = scorer.score_chain_contig(chain, self.window)
            chain_end = time.time()
            print(
                "Time for chain {} with {} residues: {}s".format(
                    chain, len(chain_scores[chain]), chain_end - chain_start
                )
            )

        tot_end = time.time()
        print("Total time: {}s".format(tot_end - tot_start))

        if self.prefix is not None:
            prefix = self.prefix
        else:
            prefix = "smoc_{}_vs_{}".format(
                os.path.basename(self.map.filename).split(".")[0],
                os.path.basename(self.model.filename).split(".")[0],
            )

        if self.output_format in ("tsv", "csv"):
            for chain in chain_scores:
                filename = "{}_chain-{}_win-{}_res-{}_{}.{}".format(
                    prefix,
                    chain,
                    self.window,
                    str(self.resolution).replace(".", "p"),
                    self.method,
                    self.output_format,
                )
                print("Writing scores for chain {} to file {}".format(chain, filename))
                delimiter = "\t"
                if self.output_format == "csv":
                    delimiter = ","
                write_tabular_scores(filename, chain_scores[chain], delimiter)
        elif self.output_format == "json":
            filename = "{}.json".format(prefix)
            print("Writing scores to {}".format(filename))
            write_json_scores(
                filename,
                {
                    "window": self.window,
                    "method": self.method,
                    "resolution": self.resolution,
                },
                chain_scores,
            )

        elif self.output_format in ("pdf", "png"):
            for chain in chain_scores:
                filename = "{}_chain-{}_win-{}_res-{}_{}.{}".format(
                    prefix,
                    chain,
                    self.window,
                    str(self.resolution).replace(".", "p"),
                    self.method,
                    self.output_format,
                )
                print("Plotting scores for chain {} to file {}".format(chain, filename))
                write_plot_file(filename, chain, chain_scores[chain])


def main():
    smoc = SMOCScript()
    try:
        smoc.run()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
