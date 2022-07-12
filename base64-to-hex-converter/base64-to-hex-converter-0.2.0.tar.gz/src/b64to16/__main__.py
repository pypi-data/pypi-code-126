import argparse
import json

from .version import __version__
from .b64to16 import process_json


if __name__ == '__main__':
    about = 'Converts data in Base64 to Hexadecimal'
    parser = argparse.ArgumentParser(
        prog='b64to16', description=about)
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version=__version__)
    parser.add_argument(
        'json_file',
        type=str,
        help='path to a JSON file')
    args = parser.parse_args()
    data = process_json(args.json_file)
    json_data = json.dumps(data)
    print(json_data)
