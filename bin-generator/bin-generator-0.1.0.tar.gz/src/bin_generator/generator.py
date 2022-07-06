#!/usr/bin/env python3
import argparse
from typing import Any, Callable, Optional
import os
import shutil
import logging
from logging import debug
import sys
import traceback
# pip modules
import yaml
import munch
# local files
from .config_loader import parse_config, ConfigEntry, ConfigOption, Config, SchemaError
from .bin_writer import OutputFileManager, CONFLICT_ASK, CONFLICT_KEEP, CONFLICT_OVERWRITE


def check_multiple(values: list[str], fn_validator: Callable[[str], bool]) -> bool:
    # This could be optimized, but is currently better for debugging
    all_ok = True
    for value in values:
        ok = fn_validator(value)
        debug(f"      {value}: {ok}")
        all_ok &= ok
    return bool(all_ok)


def check_binary(name: str) -> bool:
    return bool(shutil.which(name))


def check_file(path: str) -> bool:
    return os.path.isfile(path)


def check_dir(path: str) -> bool:
    return os.path.isdir(path)


class TracebackAlreadyPrintedException(Exception):
    pass


class Generator:
    def __init__(self, config: Config, output_manager: OutputFileManager, data: Any):
        self.config = config
        self.output_manager = output_manager
        self.data = data

    def handle_entry(self, entry) -> None:
        debug("")
        debug(f"Entry {entry.name}")
            
        for opt in entry.options:
            debug("  Option")
            ok = True
            debug("    Checking bins")
            ok &= check_multiple(opt.required_binaries, check_binary)
            debug("    Checking files")
            ok &= check_multiple(opt.required_files, check_file)
            debug("    Checking dirs")
            ok &= check_multiple(opt.required_dirs, check_dir)
            debug(f"    Requirements met: {ok}")

            if ok:
                logging.info(f"Generating '{entry.name}'")
                self.generate_bin(entry, opt)
                # Return after the first match has been found and used
                return

    def generate_bin(self, entry: ConfigEntry, option: ConfigOption) -> None:
        output_path = os.path.join(self.config.output_dir, entry.name)
        if option.contents_str:
            self.output_manager.write_file(entry.name, option.contents_str)
        elif option.contents_file:
            self.output_manager.copy_file(entry.name, option.contents_file)
        elif option.contents_mako:
            try:
                text = self.process_mako_template(option.contents_mako)
                self.output_manager.write_file(entry.name, text)
            except (KeyError, AttributeError) as e:
                logging.error(f"Failed processing template: undefined variable '{e}'\n -> Hint: Have you passed the correct file via the --data flag?")
                logging.debug(f"====== Template =======\n{option.contents_mako}\n===== End Template =====")
                raise TracebackAlreadyPrintedException() from None
        else:
            logging.debug(f"Faulty entry: {entry}")
            raise Exception("No script contents were defined")

    def process_mako_template(self, template_str: str) -> str:
        # requires mako
        from mako.template import Template

        mytemplate = Template(template_str)
        output = mytemplate.render(data=self.data)
        return output


def load_data_file(data_file: Optional[str]) -> dict:
    try:
        with open(data_file, "r") as f:
            tmp_data = yaml.safe_load(f)
        logging.info(f"Loaded data file: {data_file}")
        return tmp_data
    except Exception:
        logging.error(f"Failed to data file: {data_file}")
        logging.debug(traceback.format_exc())
        raise TracebackAlreadyPrintedException() from None


def generate_bins_using_config(path: str, clean: bool, conflict_choice: str, data: dict):
    try:
        config = parse_config(path)
    except SchemaError as e:
        logging.error("Config file schema validation failed")
        logging.debug(traceback.format_exc())
        sys.exit(1)

    if clean:
        logging.info(f"Removing directory '{config.output_dir}'")
        shutil.rmtree(config.output_dir, ignore_errors=True)

    # Make sure the folder exists
    os.makedirs(config.output_dir, exist_ok=True)

    # Make it accessible using dot notation (outer.inner.leaf)
    data = munch.munchify(data)

    try:
        with OutputFileManager(config.output_dir, path, conflict_choice) as output_manager:
            generator = Generator(config, output_manager, data)
            for entry in config.entries.values():
                try:
                    generator.handle_entry(entry)
                except Exception as ex:
                    logging.error("Error while processing entry '%s': %s", entry.name, ex)
                    logging.debug(traceback.format_exc())
    except Exception:
        logging.error("Failed to load state file")
        logging.warning("Hint: Running this script with the --clean option may fix the issue")
        logging.debug(traceback.format_exc())
        raise TracebackAlreadyPrintedException() from None


def main(args: list[int]) -> None:
    ap = argparse.ArgumentParser(description="This script can be used to conditionaly create/copy scripts to a target directory. Example use case: wrapper scripts")
    ap.add_argument("input_file", nargs="+", help=f"YAML file describing the binaries to generate")
    ap.add_argument("-d", "--data", help="path to the data file to use for the templates")
    conflict_group = ap.add_mutually_exclusive_group()
    conflict_group.add_argument("-k", "--keep", action="store_true", help="In case of conflict, keep the current file (default: ask user)")
    conflict_group.add_argument("-f", "--force", action="store_true", help="In case of conflict, overwrite the current file (default: ask user)")
    ap.add_argument("-v", "--verbose", action="count", default=0, help="Increase verbosity. Using it two times (-vv) will enable debug outputs and stacktraces")
    ap.add_argument("-c", "--clean", action="store_true", default=0, help="Delete the output directory before running. May help solve some errors")
    args = ap.parse_args(args)

    verbosity = args.verbose
    if verbosity > 2:
        logging.warn("Maximum verbosity is 2")
        verbosity = 2

    log_level = [logging.WARNING, logging.INFO, logging.DEBUG][verbosity]
    logging.basicConfig(format="[%(levelname)s] %(message)s",level=log_level)

    if args.data:
        data_file = os.path.expanduser(args.data)
        data = load_data_file(data_file)
    else:
        data = {}

    if args.keep:
        conflict_choice = CONFLICT_KEEP
    elif args.force:
        conflict_choice = CONFLICT_OVERWRITE
    else:
        conflict_choice = CONFLICT_ASK

    for input_file in args.input_file:
        logging.info("Processing input file: %s", input_file)
        try:
            generate_bins_using_config(input_file, args.clean, conflict_choice, data)
        except TracebackAlreadyPrintedException:
            logging.error("Exited because of previous error")
            sys.exit(1)
