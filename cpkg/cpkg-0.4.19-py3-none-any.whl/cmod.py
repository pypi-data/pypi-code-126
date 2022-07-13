import argparse
from cpkg import __version__, CreateModule


def main():
    parser = argparse.ArgumentParser(prog='cpkg')
    parser.add_argument('-v', "--version", action="store_true",
                        help="echo the this version")
    parser.add_argument('-a', "--author",
                        help="author")
    parser.add_argument('-A', "--author_email",
                        help="author_email")
    parser.add_argument('-c', "--classifiers",
                        help="classifiers", type=list)
    parser.add_argument('-p', "--python_requires",
                        help="python_requires")
    args = parser.parse_args()
    if args.author and args.author_email and args.classifiers and args.python_requires:
        CreateModule(
            author=args.author,
            author_email=args.author_email,
            classifiers=args.classifiers,
            python_requires=args.python_requires,
        )
    elif args.author and args.author_email and args.classifiers:
        CreateModule(
            author=args.author,
            author_email=args.author_email,
            classifiers=args.classifiers,
        )
    if args.version:
        print('version:', __version__)
