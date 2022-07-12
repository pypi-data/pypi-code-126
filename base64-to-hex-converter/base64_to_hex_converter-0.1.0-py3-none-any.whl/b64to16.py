import json
import base64


def base64_to_hex(data):
    return '0x' + base64.b64decode(data).hex()


def traverse_data(data):
    if isinstance(data, dict):
        return {
            k: traverse_data(v)
            for k, v in data.items()
        }
    elif isinstance(data, list):
        return [
            traverse_data(v)
            for v in data
        ]
    elif isinstance(data, str) and data.endswith('='):
        return base64_to_hex(data)
    else:
        return data


def process_json(json_file):
    with open(json_file) as fp:
        json_data = json.load(fp)
        return traverse_data(json_data)


# if __name__ == '__main__':
#     import argparse
#     about = ('Process JSON data and converts data in Base64 to Hexadecimal')
#     parser = argparse.ArgumentParser(
#         prog='base64_to_hex', description=about)
#     parser.add_argument(
#         'json_file',
#         type=str,
#         help='path to the JSON file')
#     args = parser.parse_args()
#     data = process_json(args.json_file)
#     json_data = json.dumps(data)
#     print(json_data)
