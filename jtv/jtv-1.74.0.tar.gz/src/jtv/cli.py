# cli.py
import sys
from click import command, option, echo
from .jsontree import JSONTree
from .app import _help, usage_error, validate_buffer


CONTEXT_SETTINGS = dict(help_option_names=[], ignore_unknown_options=True)


@command(context_settings=CONTEXT_SETTINGS)
@option('-j', is_flag=True)
@option('-y', is_flag=True)
@option('-h', is_flag=True)
@option('--mode', is_flag=False, default='distinct')
@option('--debug', is_flag=True)
def cli(j, y, h, mode, debug):
    if mode not in ['union', 'first', 'distinct']:
        _help.display()
        sys.exit(0)

    json_tree = JSONTree()
    if j:
        echo(json_tree.tree(validate_buffer(sys.stdin, _format='json'), mode=mode))
        sys.exit(0)

    elif y:
        echo(json_tree.tree(validate_buffer(sys.stdin, _format='yaml'), mode=mode))
        sys.exit(0)

    else:
        _help.display()
        sys.exit(0)


usage_error(cli)
