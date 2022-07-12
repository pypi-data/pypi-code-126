"""
# Get started

```python
from docopt import docopt
from magicli import magicli

args = magically(docopt(__doc__))
```
"""

import inspect


def magicli(args, glbls=None, entry_point='main'):
    """
    Calls all callable functions with all arguments.
    """
    # Get the `globals()` dict of the file from where the function is called.
    if not glbls:
        glbls = inspect.currentframe().f_back.f_globals 

    cleaned_args = clean_args(args)
    args = args_set_in_cli(cleaned_args)

    # Add main function to possible callable functions.
    # Main function will be called if it exists.
    if entry_point not in args:
        args[entry_point] = True

    for arg in args:
        if arg in glbls:
            func = glbls.get(arg)
            func_args = inspect.getargspec(func).args
            kwargs = {arg:args[arg] for arg in args if arg in func_args}
            func(**kwargs)

    return cleaned_args


def clean_args(args):
    """
    Creates a new dict of variables converted to correct function names.
    """
    return {parse_function_name(key): args[key] for key in args}


def parse_function_name(func):
    """
    Convert variables to valid python function names.
    """
    for char in ['<', '>', '-']:
        func = func.strip(char)
    return func.replace('-', '_')


def args_set_in_cli(args):
    """
    Returns a list of all dictionary entries that are specified in cli.
    """
    return {arg:args[arg] for arg in args if args[arg]}
