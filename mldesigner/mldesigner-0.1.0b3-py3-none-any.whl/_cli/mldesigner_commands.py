# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import sys
import argparse

from mldesigner import generate_package


def _entry(argv):
    """
    CLI tools for mldesigner.
    """
    parser = argparse.ArgumentParser(
        prog="mldesigner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="A CLI tool to generate component package.",
    )

    subparsers = parser.add_subparsers()

    # mldesigner generate package

    example_text = """
    Examples:

    # generate component functions for existing package
    mldesigner generate --assets components/**/*.yaml

    # generate component functions from workspace
    mldesigner generate --assets azureml://subscriptions/xxx/resourcegroups/xxx/workspaces/xxx

    # generate component functions from dynamic assets
    mldesigner generate --assets azureml://subscriptions/xxx/resourcegroups/xxx/workspaces/xxx, components/**/*.yml

    # generate component functions from dynamic assets, assets configured in assets.yml
    mldesigner generate --assets assets.yml

    # generate package from workspace
    mldesigner generate --assets azureml://subscriptions/xxx/resourcegroups/xxx/workspaces/xxx --package-name my-cool-package
    """
    generate_parser = subparsers.add_parser(
        "generate",
        description="A CLI tool to generate component package.",
        help="For a set of assets, generate a python module which contains component consumption functions and import it for use.",
        epilog=example_text,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    generate_parser.add_argument(
        "--assets",
        nargs="+",
        type=str,
        help="List of assets need to be genrated or path of assets config yaml.",
    )
    generate_parser.add_argument("--package_name", type=str, help="Name of the generated python package.")
    generate_parser.add_argument(
        "--force", action="store_true", help="If specified, will always regenerate package from given assets."
    )
    generate_parser.set_defaults(action="generate")

    args = parser.parse_args(argv)

    if args.action == "generate":
        generate_package(assets=args.assets, package_name=args.package_name, force_regenerate=args.force)


def main():
    """Entrance of mldesigner CLI."""
    _entry(sys.argv[1:])
