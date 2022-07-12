"""
Example:
    To run LoQFit on a model, 7kx7.pdb - which is a PIWI protein from
    the organism *Ephydatia fluviatilis*. 7kx7 has a corresponding
    cryo EM map deposited in the EMDB at the ID 23061. We can grab
    these files from the online repositories and score the model
    with LoQFit by running::

        $ TEMPy.loqfit -p rcsb:7kx7 -m emdb:23061 -r 4.53

    The default output of this command will be a series of files, one per
    chain, in tab separated format.  The files are named according to the
    parameters.  For examples, as 7kx7 contains chains A and B, the
    following files are expected::

        loqfit_emdb_23061_vs_rcsb_7kx7_chainA.tsv
        loqfit_emdb_23061_vs_rcsb_7kx7_chainA.tsv

    As with the smoc script, the output format can be changed using the
    '-f' flag which supports 'tsv', 'csv' and 'json'.  For example,
    to select JSON output::

        $ TEMPy.loqfit -p rcsb:7kx7 -m emdb:23061 -r 4.53 -f json

    This will result in a single JSON file with each chain stored under its own
    key. The parameters used to generate the score are stored under the
    'parameters' key.  The output file name would be::

        loqfit_emdb_23061_vs_rcsb_7kx7.json

    The script will also write out a plot of the LoQFit score for each chain
    in the model. These can be saved as either vector graphics '.svg' files
    or as png images by changing the '--plot_format' flag. E.g. to save the
    LoQFit plots for the synthase example as png files, run::

        $ TEMPy.loqfit -p rcsb:7kx7 -m emdb:23061 -r 4.53 --plot_format png

    This produces this plot for chain A:

    .. figure:: _static/images/loqfit-chainA.png
        :scale: 75%
        :align: center

    And this (slightly silly) plot for chain B, which has just a few modelled
    residues:

    .. figure:: _static/images/loqfit-chainB.png
        :scale: 75%
        :align: center

    Finally, the LoQFit score can be normalised using the local resolution
    of the EM-map. TEMPy needs the half-maps to calculate the local resolution
    and these can be supplied with the '-hm1' and '-hm2' flags.
    If both half maps are supplied, the normalised LoQFit score is
    automatically calculated. We can get the half-maps from the EMDB, assuming
    they are deposited. So, to calculate the normalised LoQFit we can run::

        $ TEMPy.loqfit -p rcsb:7kx7 -m emdb:23061 -r 4.53 --plot_format png -hm1 emdb:23061 -hm2 emdb:23061

    Which gives us this plot for chain A:

    .. image:: _static/images/normalised-loqfit-chainA.png
        :scale: 75%
        :align: center

"""

import numpy as np
import os
import json
import matplotlib.pyplot as plt
import csv
import argparse
from TEMPy.protein.scoring_functions import ScoringFunctions
from TEMPy.cli import arg_parser


def write_tabular_scores(filename, residue_scores, delimiter):
    with open(filename, "w") as tabular_file:
        tabular_writer = csv.writer(tabular_file, delimiter=delimiter)
        for (k, v) in residue_scores.items():
            tabular_writer.writerow([k, v])


def write_json_scores(filename, parameters, chain_residue_scores):
    with open(filename, "w") as outfile:
        json.dump(
            {"chains": chain_residue_scores, "parameters": parameters},
            outfile,
            indent=4,
        )


def parse_format(format):
    format = format.lower()
    if format in ("tsv", "csv", "json", "pdf", "png"):
        return format
    raise argparse.ArgumentTypeError(
        "Expected format to be one of: tsv, csv, json, pdf or png"
    )


def plt_parse_format(format):
    format = format.lower()
    if format in ("png", ".svg", "pdf"):
        return format
    raise argparse.ArgumentTypeError(
        "Expected format to be one of: tsv, csv, json, pdf or png"
    )


def get_parser():
    return parser.parser


parser = arg_parser.TEMPyArgParser("Calculate LoQFit scores")
parser.add_map_arg()
parser.add_model_arg()
parser.add_resolution_arg()
parser.add_half_map_args(required=False)

loqfit_group = parser.parser.add_argument_group("LoQFit")
loqfit_group.add_argument(
    '--max_loqfit_score',
    required=False,
    type=float,
    default=18.,
    help='Maximum LoQFit value to be plotted'
    )

output_group = parser.parser.add_argument_group("output")
output_group.add_argument(
    '--output_prefix',
    required=False,
    type=str,
    help='Prefix for output files'
    )
output_group.add_argument(
    "-f",
    "--format",
    dest="format",
    help="Output format: CSV, TSV, JSON",
    required=False,
    default="tsv",
    type=parse_format,
)
output_group.add_argument(
    "--write_to_cif",
    help="Write the LoQFit scores to an mmcif file",
    required=False,
    action="store_true",
)
output_group.add_argument(
    "--plot_format",
    help="Output format for saved plots: svg, png, pdf",
    required=False,
    default="png",
)


class LoQFitScript:

    def __init__(self):
        args = parser.parser.parse_args()

        self.model = args.model
        self.map = args.map
        self.resolution = args.resolution
        self.max_res = args.max_loqfit_score
        self.output_prefix = args.output_prefix
        self.half_map1 = args.hmap1
        self.half_map2 = args.hmap2
        self.output_format = args.format
        self.plot_ext = args.plot_format
        self.write_to_cif = args.write_to_cif

        if self.half_map1 is not None and \
                self.half_map2 is not None:
            self.method = "normalised-LoQFit"
        else:
            self.method = "LoQFit"

        if args.output_prefix is not None:
            self.output_prefix = args.output_prefix
        else:
            self.output_prefix = "./loqfit_{}_vs_{}".format(
                os.path.basename(self.map.filename).split(".")[0],
                os.path.basename(self.model.filename).split(".")[0],
            )

    def run(self):

        scorer = ScoringFunctions()
        loqfit_score = scorer.LoQFit(self.model, self.map,
                                     self.resolution,
                                     max_res=self.max_res,
                                     half_map_1=self.half_map1,
                                     half_map_2=self.half_map2)

        chain_scores = self.split_scores_by_chain(loqfit_score)

        if self.output_format in ("tsv", "csv"):
            for chain in chain_scores:
                filename = f"{self.output_prefix}_chain{chain}." \
                           f"{self.output_format}"
                print(f"Writing scores for chain {chain} to file"
                      f" {filename}")
                delimiter = "\t"
                if self.output_format == "csv":
                    delimiter = ","
                write_tabular_scores(filename,
                                     chain_scores[chain], delimiter)
        else:
            filename = f"{self.output_prefix}.json"
            print("Writing scores to {}".format(filename))
            write_json_scores(
                filename,
                {
                    "method": self.method,
                    "resolution": self.resolution,
                },
                chain_scores,
            )

        for chain in chain_scores.keys():
            self.plot_chain_scores(chain, chain_scores[chain])

        if self.write_to_cif:
            filename = f"{self.model.filename[:-4]}_loqfit.cif"
            self.model.set_local_score(self.method, chain_scores)
            self.model.write_to_mmcif(filename)

    def plot_chain_scores(self, chain_name, loqfit_chain_scores):
        residues = []
        scores = []
        for res, score in loqfit_chain_scores.items():
            residues.append(res)
            scores.append(score)

        min = np.floor(np.min(scores))
        max = np.ceil(np.max(scores))

        filename = f"{self.output_prefix}loqfit_chain{chain_name}." \
                   f"{self.plot_ext}"
        print(f"Saving LoQFit plot for chain {chain_name} as {filename}")

        plt.plot(residues, scores)
        plt.xlabel("Residue Number")
        plt.ylabel(f"{self.method} Score")
        plt.title(f"{self.method} for chain {chain_name}")
        plt.ylim(min, max)
        plt.savefig(filename)
        plt.close()

    def split_scores_by_chain(self, loqfit_scores):
        loqfit_by_chain = {}

        for ((chain, res_no), score) in loqfit_scores.items():
            try:
                loqfit_by_chain[chain][res_no] = score
            except KeyError:
                loqfit_by_chain[chain] = {res_no: score}

        return loqfit_by_chain


def main():
    loqfit = LoQFitScript()
    try:
        loqfit.run()
    except Exception as e:
        raise e


if __name__ == "__main__":
    main()
