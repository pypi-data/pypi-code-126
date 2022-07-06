"""Command line interface `aiida-wannier90-workflows`."""
import click

from aiida.cmdline.params import options, types


@click.group(
    "aiida-yambo-wannier90", context_settings={"help_option_names": ["-h", "--help"]}
)
@options.PROFILE(type=types.ProfileParamType(load_profile=True))
def cmd_root(profile):  # pylint: disable=unused-argument
    """CLI for the `aiida-yambo-wannier90` plugin."""
