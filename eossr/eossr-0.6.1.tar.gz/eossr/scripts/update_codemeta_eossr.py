import argparse
from pathlib import Path

from eossr import ROOT_DIR
from eossr import __version__ as eossr_version
from eossr.utils import update_codemeta


def build_argparser():
    """
    Construct main argument parser for the ``codemet2zenodo`` script

    :return:
    argparser: `argparse.ArgumentParser`
    """
    parser = argparse.ArgumentParser(description="Update Codemeta")

    parser.add_argument(
        '--codemeta_path',
        '-c',
        type=str,
        dest='codemeta_path',
        help='Path to codemeta.json',
        default=Path(ROOT_DIR).joinpath('codemeta.json'),
        required=False,
    )

    parser.add_argument(
        '--no-release',
        action='store_false',
        help="Use when making a release. Do not update the publication date, the zip archive URL and remove release notes."
    )

    return parser


if __name__ == '__main__':
    parser = build_argparser()
    args = parser.parse_args()

    if args.no_release:
        publication_date = False
        release_notes = ""
        download_url = ""
    else:
        publication_date = True
        release_notes = None
        download_url = f'https://gitlab.in2p3.fr/escape2020/wp3/eossr/-/archive/v{eossr_version}/eossr-v{eossr_version}.zip'

    html = update_codemeta(
        codemeta_path=args.codemeta_path,
        readme_path=Path(__file__).parent.joinpath('../../README.md').resolve(),
        version=eossr_version,
        download_url=download_url,
        publication_date=publication_date,
        release_notes=release_notes,
        overwrite=True,
    )
