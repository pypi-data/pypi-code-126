""" A simple implementation of the Blueplate Special class which can generate scripts from template
>>> m = Main("")
>>> isinstance(m, Main)
True
"""

import os
import sys
import shutil
import logging
from jinja2 import Environment, FileSystemLoader, Template

import requests

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

from .blueplate.special import Special
from .blueplate.version import version

log = logging.getLogger()


def get_toml(filename):
    with open(filename, "rb") as f:
        toml = tomllib.load(f)

    return toml


def flatten_dict(*args):
    args = list(args)
    flattened = args.pop(0)

    while args:
        overlay = args.pop()
        log.debug(f"Merging dictionaries: {overlay.keys()} -> {flattened.keys()}")

        for k, v in overlay.items():
            if k in flattened.keys():
                if isinstance(v, dict) and isinstance(flattened[k], dict):
                    log.debug(f"Merging dicts in field: {k}")
                    flattened[k] = flatten_dict(flattened[k], v)
                elif isinstance(v, list) and isinstance(flattened[k], list):
                    log.debug(f"Concatenating lists in field: {k}")
                    flattened[k] = flattened[k] + v
                else:
                    log.debug(f"Overwriting simple value: {v} -> {flattened[k]}")
                    flattened[k] = v
            else:
                log.debug(f"Adding new key: {k} = {v}")
                flattened[k] = v

    return flattened


def recursive_jinja_render(root_path, config):
    recursive_jinja_file_render(root_path, config)
    recursive_jinja_path_rename(root_path, config)
    recursive_jinja_file_rename(root_path, config)


def recursive_jinja_file_render(root_path, config):
    # Prep templating environment
    file_loader = FileSystemLoader(root_path)
    env = Environment(loader=file_loader)

    # Render all files as jinja
    for root, dirs, files in os.walk(root_path):
        for filename in files:
            relative_path = os.path.relpath(root, root_path)
            relative_file = os.path.join(relative_path, filename)
            log.info(f"Rendering {relative_file}")
            template = env.get_template(relative_file)
            rendered = template.render(config)

            log.warning(f"Overwriting file {os.path.join(root, filename)}")
            with open(os.path.join(root, filename), "w") as f:
                f.write(rendered)


def recursive_jinja_path_rename(root_path, config):
    # Check all paths for jinja markup and rename if necessary
    for root, dirs, files in os.walk(root_path):
        for path in dirs:
            path_template = Template(path)
            rendered_path = path_template.render(config)

            if rendered_path != path:
                log.warning(f"Renaming rendered path: {path} -> {rendered_path}")
                shutil.move(os.path.join(root, path), os.path.join(root, rendered_path))


def recursive_jinja_file_rename(root_path, config):
    # Check all filenames for jinja markup and rename if necessary
    for root, dirs, files in os.walk(root_path):
        for filename in files:
            filename_template = Template(filename)
            rendered_filename = filename_template.render(config)

            if rendered_filename != filename:
                log.warning(
                    f"Renaming rendered file: {filename} -> {rendered_filename}"
                )
                os.rename(
                    os.path.join(root, filename), os.path.join(root, rendered_filename)
                )


class Main(Special):
    """main: A simple implementation of the Blueplate Special class which can generate scripts from template
    >>> isinstance(script, Main)
    True
    >>> isinstance(script, Special)
    True
    >>> issubclass(script.__class__, Special)
    True
    """

    def fn(self):
        if self.args.template:
            self.generate_script_toml()

        if self.args.template and self.args.generate:
            input("Press enter when to proceed.")

        if self.args.generate:
            config = self.get_merged_config()
            self.generate_project(config)

        return

        super().fn()

    def test(self, mock_test=False):
        """Run local tests and tests on other mods
        >>> script.test(True)
        Called doctest.testmod(
            <module 'blueplate.__main__' from '.../blueplate/__main__.py'>,
        ...
        Called doctest.testmod(
            <module 'blueplate.blueplate.special' from '.../blueplate/blueplate/special.py'>,
        ...
        Called doctest.testmod(
            <module 'blueplate.blueplate.logger' from '.../blueplate/blueplate/logger.py'>,
        ...
        """
        from blueplate import logger, special

        super().test(mock_test)
        response = special.Special().test(mock_test)
        special.test_module(logger, mock_test=mock_test)

    def get_merged_config(self):
        project_toml = get_toml(self.args.toml)
        personal_toml = get_toml(os.path.expanduser("~/.tomlrc"))
        merged_toml = flatten_dict(personal_toml, project_toml)

        config = merged_toml["tool"]["blueplate"]["generator"]

        # Inject current version
        config["version"] = version

        # Inject full license
        if "url" not in config["license"].keys():
            config["license"][
                "url"
            ] = f"https://raw.githubusercontent.com/OpenSourceOrg/licenses/master/texts/plain/{config['license']['spdx']}"

        log.info(f"Fetching license text from {config['license']['url']}")
        response = requests.get(config["license"]["url"])

        if response.status_code == 200:
            config["license"]["text"] = response.text
        else:
            log.warn(
                f"Failed to retrieve license text: received {response.status_code} from {config['license']['url']}"
            )
            config["license"]["text"] = config["license"]["spdx"]

        return config

    def generate_script_toml(self):
        file_loader = FileSystemLoader(project_path)
        env = Environment(loader=file_loader)
        template = env.get_template("project.toml.jinja")
        rendered_toml = template.render(details)

        if os.path.exists(self.args.toml) and not self.args.force:
            raise RuntimeError(
                f"The specified TOML file '{self.args.toml}' already exists, use --force to overwrite"
            )
        elif os.path.exists(self.args.toml) and self.args.force:
            log.warning(f"Overwriting existing TOML '{self.args.toml}'")

        with open(self.args.toml, "w") as f:
            f.write(rendered_toml)

        print(
            f"Complete the TOML file '{self.args.toml}' with your project details, then use --generate to create the project"
        )

    def generate_project(self, config):
        project = config["package"]["project"]

        # Define paths
        project_path = os.path.join(config["path"], project)
        template_path = os.path.join(os.path.dirname(__file__), "templates")
        blueplate_path = os.path.join(os.path.dirname(__file__), "blueplate")

        # Check if project already exists
        if os.path.exists(project_path) and not self.args.force:
            raise RuntimeError(
                f"The specified project directory '{project_path}' already exists, use --force to overwrite"
            )
        elif os.path.exists(project_path) and self.args.force:
            log.warning(f"Removing existing directory '{project_path}'")
            shutil.rmtree(project_path)

        # Copy the project template to the new directory
        shutil.copytree(
            os.path.join(template_path, "blueplate"), os.path.join(project_path)
        )

        # Rename and render all files and paths
        recursive_jinja_render(project_path, config)

        # Copy in the blueplate module from src/blueplate/blueplate
        shutil.copytree(
            blueplate_path, os.path.join(project_path, "src", project, "blueplate")
        )

        # Remove all __pycache__ paths
        for root, dirs, files in os.walk(project_path):
            for path in dirs:
                if path == "__pycache__":
                    log.warning(f"Removing __pycache__ from {os.path.join(root, path)}")
                    shutil.rmtree(os.path.join(root, path))

        # Rename and render all files and paths
        recursive_jinja_render(project_path, config)

        print(
            f"Run `PYTHONPATH={project_path}/src python3 -m {project} --help` to confirm"
        )


if __name__ == "__main__":
    script = Main()
    script.main()
