from typing import NamedTuple
import hashlib
from datetime import datetime
import os
import logging
import shutil
# pip dependencies
import yaml
from schema import Optional as Nullable, Schema, SchemaError, Or
from termcolor import colored, cprint

STATE_SCHEMA = Schema({
    # Not really used, but may be useful for the user
    "timestamp": str,
    # To allow a user to understand where the binaries came from.
    "config": str,
    # Also allow an empty dict
    "hashes": Or({str: str}, {}),
})

CONFLICT_ASK = "?"
CONFLICT_KEEP = "K"
CONFLICT_OVERWRITE = "O"

class State(NamedTuple):
    """
    A state file stores the hashes of the files created during the last run.
    This allows detecting external file changes and removing only the files created by this config.
    Thus, multiple configs can use one target output directory.
    """
    timestamp: str
    config: str
    hashes: dict[str, str]


def parse_state_file(path: str):
    with open(path, "rb") as f:
        data = yaml.safe_load(f)
    STATE_SCHEMA.validate(data)

    return State(
        timestamp=data["timestamp"],
        config=data["config"],
        hashes=data["hashes"],
    )


def file_hash_hex(path: str) -> str:
    with open(path, "rb") as f:
        return create_hash_hex(f.read())


def create_hash_hex(contents: bytes) -> str:
    return hashlib.sha3_512(contents).hexdigest()


class OutputFileManager:
    def __init__(self, output_dir: str, config_path: str, conflict_choice: str):
        self.output_dir = output_dir
        # The filename without the file extension
        self.config_name = os.path.basename(config_path).split(".", 1)[0]
        self.conflict_choice = conflict_choice

        self.state_file_path = self.path(f"{self.config_name}-state.txt")
        if os.path.exists(self.state_file_path):
            self.old_state = parse_state_file(self.state_file_path)
            if self.old_state.config != config_path:
                logging.warning("State file may have been created by a different config")
        else:
            self.old_state = State(timestamp="never", config=config_path, hashes={})

        logging.debug("Old state: %s", self.old_state)

        now = f"{datetime.now()}"
        self.new_state = State(timestamp=now, config=config_path, hashes={})

    def __enter__(self):
        logging.debug("OutputFileManager::__enter__ for '%s'", self.state_file_path)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        logging.debug("OutputFileManager::__exit__ for '%s'", self.state_file_path)
        new = self.new_state
        old = self.old_state

        # delete old files
        for name in old.hashes:
            if name not in new.hashes:
                path = self.path(name)
                try:
                    os.remove(path)
                    cprint(f"Removed: {name}", 'red', attrs=['bold'])
                except Exception as ex:
                    logging.warning(path)

        if new.hashes == old.hashes and new.config == old.config:
            logging.info("All important values are equal. Skipping writing the state file")
        else:
            logging.info("Writing state file with %d hashes", len(new.hashes))
            # write new state file
            with open(self.state_file_path, "w") as f:
                data = {
                    "timestamp": new.timestamp,
                    "config": new.config,
                    "hashes": new.hashes,
                }
                yaml.safe_dump(data, f)

        return True

    def write_file(self, name: str, contents: str):
        hash_hex = create_hash_hex(contents.encode("utf-8"))
        if self.file_needs_update(name, hash_hex):
            path = self.path(name)
            with open(path, "w") as f:
                f.write(contents)
        self._after_file_written(name, hash_hex)

    def copy_file(self, name: str, source_path: str):
        hash_hex = file_hash_hex(source_path)
        if self.file_needs_update(name, hash_hex):
            path = self.path(name)
            shutil.copyfile(source_path, path)
        self._after_file_written(name, hash_hex)

    def file_needs_update(self, name: str, new_hash: str) -> bool:
        old_hash = self.old_state.hashes.get(name)
        if old_hash:
            path = self.path(name)
            try:
                current_hash = file_hash_hex(path)
            except:
                cprint(f"Could not compare: {name}", "yellow", attrs=["bold"])
                return True

            if current_hash != old_hash:
                conflict_choice = self.conflict_choice
                while True:
                    if conflict_choice == CONFLICT_OVERWRITE:
                        cprint(f"Overwrote (conflict): {name}", "yellow", attrs=["bold"])
                        return True
                    elif conflict_choice == CONFLICT_KEEP:
                        cprint(f"Keeping original (conflict): {name}", "blue", attrs=["bold"])
                        return False
                    else:
                        cprint(f"Conflict: {path} was modified by an external program.", "magenta")
                        conflict_choice = input("[K]eep current or [O]verwrite? (default: keep) ")
                        conflict_choice = conflict_choice.strip()[:1].upper() or CONFLICT_KEEP

            if old_hash == new_hash:
                # The old file is the same as the current file
                if logging.root.isEnabledFor(logging.INFO):
                    cprint(f"Unchanged: {name}", attrs=["bold"])
                return False
            else:
                cprint(f"Modified: {name}", "yellow", attrs=["bold"])
                return True
        else:
            cprint(f"Added: {name}", "green", attrs=["bold"])
            return True

    def path(self, name: str) -> str:
        return os.path.join(self.output_dir, name)

    def _after_file_written(self, name: str, new_hash: str):
        if name in self.new_state.hashes:
            raise Exception(f"File already created: '{name}'")
        
        self.new_state.hashes[name] = new_hash
        # Make the file executeable
        os.chmod(self.path(name), 0o755)


    


