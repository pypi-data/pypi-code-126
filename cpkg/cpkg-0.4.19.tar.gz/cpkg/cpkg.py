import argparse
from cpkg import __version__, create


def main():
    parser = argparse.ArgumentParser(prog='cpkg')
    parser.add_argument('-v', "--version", action="store_true",
                        help="echo the this version")
    parser.add_argument('-p', "--path",
                        help="path")
    parser.add_argument('-n', "--dirName",
                        help="dirName")
    parser.add_argument('-P', "--pkgName",
                        help="pkgName")
    parser.add_argument('-a', "--author",
                        help="author")
    parser.add_argument('-A', "--author_email",
                        help="author_email")
    parser.add_argument('-d', "--description",
                        help="description")
    parser.add_argument('-u', "--url",
                        help="url")
    parser.add_argument('-Pu', "--project_urls",
                        help="project_urls", type=dict)
    parser.add_argument('-c', "--classifiers",
                        help="classifiers", type=list)
    parser.add_argument('-Pr', "--python_requires",
                        help="python_requires")
    parser.add_argument('-i', "--install_requires",
                        help="install_requires")
    parser.add_argument('-m', '--module', type=str, help='.cpgmod file')
    parser.add_argument('-N', '--new', type=tuple, help='newElement')
    parser.add_argument('-e', '--entry_points', type=dict, help='entry_points')
    args = parser.parse_args()
    if args.module:
        if args.module.split('.')[-1] == 'cpgmod':
            create(
                ismod=True,
                modPath=args.module,
                path=args.path,
                dirName=args.dirName,
                pkgName=args.pkgName,
                description=args.description,
                url=args.url,
                project_urls=args.project_urls,
                python_requires=args.python_requires,
                install_requires=args.install_requires
            )
        elif args.file.split('.')[-1] != 'cpkg':
            print('The suffix of the -f parameter must be cpkg')
    if args.path and args.dirName and args.pkgName and args.author and args.author_email and args.description and args.url and args.project_urls and args.classifiers and args.python_requires and args.install_requires and args.entry_points and args.new:
        create(
            args.new,
            entry_points=args.entry_points,
            path=args.path,
            dirName=args.dirName,
            pkgName=args.pkgName,
            author=args.author,
            author_email=args.author_email,
            description=args.description,
            url=args.url,
            project_urls=args.project_urls,
            classifiers=args.classifiers,
            python_requires=args.python_requires,
            install_requires=args.install_requires
        )
    elif args.path and args.dirName and args.pkgName and args.author and args.author_email and args.description and args.url and args.project_urls and args.classifiers and args.python_requires and args.install_requires and args.entry_points:
        create(
            entry_points=args.entry_points,
            path=args.path,
            dirName=args.dirName,
            pkgName=args.pkgName,
            author=args.author,
            author_email=args.author_email,
            description=args.description,
            url=args.url,
            project_urls=args.project_urls,
            classifiers=args.classifiers,
            python_requires=args.python_requires,
            install_requires=args.install_requires
        )
    elif args.path and args.dirName and args.pkgName and args.author and args.author_email and args.description and args.url and args.project_urls and args.classifiers and args.python_requires and args.install_requires and args.entry_points:
        create(
            args.new,
            path=args.path,
            dirName=args.dirName,
            pkgName=args.pkgName,
            author=args.author,
            author_email=args.author_email,
            description=args.description,
            url=args.url,
            project_urls=args.project_urls,
            classifiers=args.classifiers,
            python_requires=args.python_requires,
            install_requires=args.install_requires
        )
    if args.version:
        print('version:', __version__)
