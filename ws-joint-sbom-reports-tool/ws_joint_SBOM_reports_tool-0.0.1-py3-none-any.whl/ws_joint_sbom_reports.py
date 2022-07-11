import json
import os
import argparse
import logging
from _version import __tool_name__

logger = logging.getLogger(__tool_name__)
logger.setLevel(logging.DEBUG)


def parse_args():
    parser = argparse.ArgumentParser(description='Utility to joint SBOM reports')
    parser.add_argument('-f1', '--first', help="First SPDX file", dest='first_file', default=os.environ.get("FIRST_FILE"), required=True )
    parser.add_argument('-f2', '--second', help="Second SPDX file", dest='second_file', default=os.environ.get("SECOND_FILE"), required=True )
    parser.add_argument('-o', '--output', help="Output SPDX file", dest='output_file', default=os.environ.get("OUTPUT_FILE"), required=True )
    parser.add_argument('-hf', '--head', help="Head from 1st file", dest='head_file', default=True)
    arguments = parser.parse_args()

    return arguments


def remove_duplicate_dict(src : list) -> list:
    res = []
    for i in range(len(src)):
        if src[i] not in src[i + 1:]:
            res.append(src[i])
    return res


def main():
    try:
        args = parse_args()
        with open(args.first_file) as f1:
            data = json.load(f1)

        with open(args.second_file) as f2:
            data_2 = json.load(f2)

        res = dict(data if args.head_file else data_2)
        res['documentDescribes'] = data['documentDescribes'] + data_2['documentDescribes']
        res['documentDescribes'] = list(set(res['documentDescribes']))

        res['packages'] = remove_duplicate_dict(data['packages'] + data_2['packages'])

        res['hasExtractedLicensingInfos'] = remove_duplicate_dict(data['hasExtractedLicensingInfos'] + data_2['hasExtractedLicensingInfos'])
        res['relationships'] = remove_duplicate_dict(data['relationships'] + data_2['relationships'])

        with open(f'{args.output_file}.json', 'w') as f:
            json.dump(res, f, indent=4 )
        f.close()
    except Exception as err:
        logger.error(f"Error running joint tool: {err}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


