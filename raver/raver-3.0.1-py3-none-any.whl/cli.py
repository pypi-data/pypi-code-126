import re
import sys
from collections import defaultdict
from functools import partial
from pathlib import Path
from subprocess import CalledProcessError, check_output
from typing import Any, Dict, Optional, Union

import click
import tomli
from semver import VersionInfo

from raver import __version__

VERSION = re.compile(r"__version__\s*=\s*[\"\'](.*)[\"\']")


@click.command("raver")
@click.option(
    "--module",
    "-m",
    default=None,
    help="Path to Python module to check. Defaults to Poetry's value.",
    type=click.Path(
        exists=True, readable=True, dir_okay=True, file_okay=True, path_type=Path
    ),
)
@click.option(
    "--ref",
    "-r",
    default=None,
    help="Git reference to check changes and version increments against.",
)
@click.option(
    "--config",
    "-c",
    default="./pyproject.toml",
    show_default=True,
    help="TOML config file to read.",
    type=click.Path(
        exists=False, file_okay=True, dir_okay=False, readable=True, path_type=Path
    ),
)
@click.option(
    "--changelog",
    "-l",
    default=None,
    help="Optional changelog to check for version entry.",
    type=click.Path(
        exists=True, readable=True, dir_okay=True, file_okay=True, path_type=Path
    ),
)
@click.option(
    "--debug/--no-debug", "-d/", default=False, help="Toggle debugging output."
)
@click.option(
    "--version",
    "-v",
    default=False,
    is_flag=True,
    help="Print Raver's version and exit.",
)
@click.pass_context
def cli(
    ctx: click.Context,
    module: Optional[Path],
    ref: Optional[str],
    config: Optional[Path],
    changelog: Optional[Path],
    debug: bool,
    version: bool,
):
    """Ratio versioning checker."""
    info(f"Raver {__version__} 𓄿")
    ctx.obj = RaverContext(module, ref, config, changelog, debug, version)
    ctx.obj.parse()
    ctx.obj.report()


class RaverContext:
    """Raver context object."""

    TYPES = dict(module=Path, ref=str, config=Path, changelog=Path, debug=bool)

    def __init__(
        self,
        module: Optional[Path],
        ref: Optional[str],
        config: Optional[Path],
        changelog: Optional[Path],
        debug: bool,
        version: bool,
        success: bool = True,
    ):
        self.module = module
        self.module_path = None
        self.config = config
        self.changelog = changelog
        self.changelog_entry = False
        self.debug = debug
        self.version = version
        self.success = success

        # Git ref and current.
        self.ref = ref
        self.current_ref = None
        self.ref_changes = None
        self.ref_increment_ok = False

        # Version variables.
        self.module_version = None
        self.ref_version = None
        self.poetry_version = None

        self.toml = configdict()

    def parse(self):
        """Parse with current settings."""
        if self.config:
            with open(self.config, "rb") as f:
                self.toml = configdict(**tomli.load(f))

            # Fetch data already set for poetry.
            self.parse_poetry_toml(self.toml)

            # Override with raver specifics!
            self.parse_raver_toml(self.toml)

        if self.version:
            sys.exit(0)

        # Can't do anything without a module.
        if not self.module:
            return error("'module' needs to be set in order for Raver to work.")

        self.module_path = resolve_module_path(self.module)
        self.parse_module()
        if self.ref:
            self.parse_ref()

        if self.changelog:
            self.parse_changelog()

    def parse_poetry_toml(self, cdict: defaultdict):
        """Parse the poetry section of a config dictionary."""
        poetry_dict = cdict["tool"]["poetry"]
        if not poetry_dict:
            return
        poetry_module = poetry_dict["name"]
        if not self.module and poetry_module:
            base = self.config.parent if self.config else Path.cwd()
            self.module = base / poetry_module
        try:
            self.poetry_version = VersionInfo.parse(cdict["tool"]["poetry"]["version"])
        except Exception as e:
            error(f"Error while trying to parse Poetry package version: \n{e}")

    def parse_raver_toml(self, cdict: defaultdict):
        """Parse own TOML keys."""
        cfg = cdict["tool"]["raver"]
        if not cfg:
            return
        self.parse_section(cfg, self.TYPES, "")
        sections = [key for key, val in self.TYPES.items() if type(val) == dict]
        for section in sections:
            self.parse_section(cfg, self.TYPES, section)

    def parse_section(self, cdict: Any, types: Dict[str, Any], section: str):
        """Check a section on allowed keys and set config attributes."""
        parts = section.split(".") if section else []
        for p in parts:
            if not p:
                break
            cdict, types = cdict[p], types[p]
            if not cdict:
                return

        # Check for allowed keys
        specified = set(cdict.keys())
        allowed = set(types.keys())
        if not specified.issubset(allowed):
            invalid = specified.difference(allowed)
            error(
                f"Invalid Raver config key(s) {invalid} in '{self.config}'. "
                f"Allowed keys: {allowed}."
            )

        # Parse allowed keys. Attribute format: self.section_subsection_field
        for key, val in cdict.items():
            t = types[key] if isinstance(types[key], type) else type(types[key])
            try:
                val = t(val)
            except TypeError:
                error(
                    f"Config key '{key}' at 'tool.raver.{section}' in '{self.config}' "
                    f"should be of type {t}, got '{val}' of '{type(val)}'."
                )
            if t != dict:
                attr = "_".join(parts + [key])
                setattr(self, attr, t(val))

    def parse_module(self):
        """Parse module contents for version info."""
        self.module_version = get_module_version(self.module_path.read_text())

    def parse_ref(self):
        """Parse git ref for info."""
        self.current_ref = get_current_ref()
        self.ref_version = get_module_version(get_ref_text(self.module_path, self.ref))
        self.ref_changes = has_ref_changes(self.ref)
        self.ref_increment_ok = check_ref_increments(
            self.module_version, self.ref_version, self.ref_changes
        )

    def report(self):
        """Describe current status."""
        fn = (
            success
            if self.module_version and (self.ref_increment_ok or not self.ref)
            else warn
        )
        fn(f"Module version   : {self.module_version}")
        if self.poetry_version:
            fn = success if self.poetry_version == self.module_version else warn
            fn(f"Poetry version   : {self.poetry_version}")
        if self.ref:
            fn = success if self.ref_increment_ok else warn
            fn(f"Ref version      : {self.ref_version} ({self.ref})")
            fn(f"Committed changes: {self.ref_changes}")
        if self.changelog:
            fn = success if self.changelog_entry else warn
            fn(f"Changelog entry  : {self.changelog_entry}")
        if self.success:
            success("Satisfied raver version checking!")
        else:
            error("Raver found versioning mistakes!")

    def parse_changelog(self):
        """Check if a changelog entry exists for the current version."""
        self.changelog_entry = check_changelog(self.changelog, self.module_version)


def configdict(**kwargs) -> defaultdict:
    """Recursive defaultdict."""
    d: Any = defaultdict(configdict)
    for key, value in kwargs.items():
        if isinstance(value, dict):
            d[key] = configdict(**value)
        else:
            d[key] = value
    return d


info = partial(click.secho, err=False)
success = partial(click.secho, err=False, fg="green")


def error(message: str, exitcode: int = 1):
    """Print to stderr in red and exit with 1."""
    click.secho(message, err=True, bold=True, fg="red")
    sys.exit(exitcode)


def warn(message: str):
    """Print to stderr in yellow but do not exit, yet."""
    click.secho(message, err=False, bold=True, fg="yellow")
    try:
        obj = click.get_current_context().obj
        obj.success = False
    except RuntimeError:
        pass


def debug(message: str):
    """Only print debug messages if debug mode is set."""
    try:
        obj = click.get_current_context().obj
        if not obj.debug:
            return
    except RuntimeError:
        pass
    click.secho(message, err=False, fg="cyan")


def resolve_module_path(module: Path) -> Path:
    """Resolve a Python module to it's file Path."""
    if module is None:
        raise ValueError("Cannot resolve module path if it's set to None.")
    f: Optional[Path] = None
    if module.exists():
        if module.is_dir():
            f = module / "__init__.py"
        if module.is_file():
            f = module
    else:
        f = module.with_suffix(".py")
    if f and f.exists():
        return f.resolve()
    else:
        return error(f"Cannot find Python module '{module}'.")


def get_module_version(text: str) -> VersionInfo:
    """Get module version from it's text."""
    debug("Parsing version from text...")
    match = VERSION.search(text)
    if match is None:
        return error("__version__ statement could not be found in text contents.")
    try:
        version = VersionInfo.parse(match.groups()[0])
        debug(f"  => Found version {version}.")
        return version
    except Exception as e:
        return error(f"Module version could not be parsed:\n{e}")


def capture(cmd: str, **kwargs) -> str:
    """Run command and return decoded and stripped output."""
    output = check_output(cmd.split(" "), **kwargs).decode("utf-8").strip()
    return output


def resolve_git_path(path: Union[str, Path]) -> Path:
    """Resolve provided path relative to this git directory's root."""
    try:
        output = capture("git rev-parse --show-toplevel")
        root = Path(output)
        result = Path(path).absolute().relative_to(root)
    except CalledProcessError as e:
        error(f"Could not determine git repository root:\n{e}")
    except ValueError as e:
        error(f"Could not resolve path '{path}' relative to root '{root}':\n{e}")
    return result


def get_current_ref() -> Optional[str]:
    """Get current git reference."""
    debug("Getting current reference...")

    cur_ref = None
    try:
        output = capture("git status -b --porcelain")
        # First line looks like "## branchname...remote/branchname"
        cur_ref = output.split(" ")[1].split("...")[0].strip()
    except CalledProcessError as e:
        error(f"Could not determine current reference. Error when running git:\n{e}")
    except IndexError as e:
        error(
            "Could not determine current reference. "
            f"Could not parse git status output: \n{e}"
        )

    debug(f"  => Current reference is '{cur_ref}'.")
    return cur_ref


def fetch_git_ref(ref: str):
    try:
        if len(ref.split("/")) > 1:
            remote = ref.split("/")[0]
            debug(f"Fetching git remote '{remote}'...")
            capture(f"git fetch {remote}")
            debug(f"  => Fetched git remote '{remote}'.")
    except Exception as e:
        error(f"Error while fetching '{remote}':\n{e}")


def get_ref_text(path: Union[str, Path], ref: str = "master") -> str:
    fetch_git_ref(ref)
    debug(f"Getting text at '{path}' from '{ref}'...")
    try:
        path = resolve_git_path(path)
        txt = capture(f"git show {ref}:{path.as_posix()}")
    except CalledProcessError as e:
        error(f"Error while reading reference version file:\n{e}")
    debug(f"  => Got text from '{ref}'.")
    return txt


def has_ref_changes(ref: str) -> bool:
    fetch_git_ref(ref)
    debug("Checking for changes...")

    try:
        changes = capture(f"git diff {ref}")
    except Exception as e:
        error(f"Error while checking for changes using git diff:\n{e}")

    if changes:
        debug("  => Found committed changes.")
        return True

    else:
        debug("  => Did not find committed changes.")
        return False


def check_ref_increments(
    module_version: VersionInfo, ref_version: VersionInfo, changes: bool
) -> bool:
    """Check whether version has been properly incremented versus the git reference."""
    debug("Checking version increments with respect to git ref...")
    prefix = "  => Change: "
    if module_version == ref_version:
        debug(prefix + "NONE")
        if changes:
            warn(
                "Version has not been incremented for changes! "
                + "Consider bumping before merging."
            )
            return False
        else:
            debug("  => Good. No committed changes and no increment.")
    elif module_version < ref_version:
        debug(prefix + "DECREMENT")
        warn("Module version has been decremented! Consider bumping before merging.")
        return False
    else:
        major = module_version.major - ref_version.major
        minor = module_version.minor - ref_version.minor
        patch = module_version.patch - ref_version.patch
        pre_build = not any([major, minor, patch])
        if major > 0:
            debug(prefix + f"MAJOR ({major})")
        if minor > 0:
            debug(prefix + f"MINOR ({minor})")
        if patch > 0:
            debug(prefix + f"PATCH ({patch})")
        if pre_build:
            debug(prefix + "PRERELEASE")
        increments = (
            sum(part * (part > 0) for part in [major, minor, patch]) + pre_build
        )
        if increments > 1:
            warn("Incremented more than one digit!")
            return False
        else:
            debug("  => Good. Version has been bumped for committed changes!")
    return True


def check_changelog(changelog: Path, version: VersionInfo) -> bool:
    """Check whether semantic version exists in changelog path.

    Only checks for major.minor.patch, prereleases and builds are ignored.
    """
    mmp = f"{version.major}.{version.minor}.{version.patch}"
    debug(f"Checking changelog for version {mmp}...")

    if changelog.is_dir():
        vstr = f"v{mmp}*"
        if list(changelog.glob(vstr)):
            debug("  => Found entry in changelog for current version!")
        else:
            warn(
                f"Found no changelog entry for version {mmp}! "
                + f"Consider adding a file to '{changelog.resolve()}'."
            )
            return False
    else:
        VERSION = re.compile(f"(?<![0-9]){mmp}(?![0-9])")
        match = VERSION.search(changelog.read_text())
        if match:
            debug("  => Found entry in changelog for current version!")
        else:
            warn(
                f"Found no changelog entry for version {mmp}! "
                + f"Consider adding one to '{changelog.resolve()}'!"
            )
            return False
    return True


if __name__ == "__main__":
    cli()
