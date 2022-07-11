import click
from rich.console import Console
from rich.traceback import install

from openldap_schema_parser import __name__, __version__
from openldap_schema_parser.exceptions import SchemaParseError
from openldap_schema_parser.parser import parse

install(show_locals=True)


@click.command()
@click.version_option(version=__version__, package_name=__name__)
@click.help_option("-h", "--help")
@click.option("--expand-oid", is_flag=True, help="Expand ObjectIdentifier")
@click.argument("target", type=click.Path(exists=True))
def cli(target, expand_oid):
    console = Console()
    error_console = Console(stderr=True, style="bold red")
    try:
        result = parse(target)
        if expand_oid:
            result.expand_oid()
        console.log(result)
    except SchemaParseError as error:
        error_console.log(error)
