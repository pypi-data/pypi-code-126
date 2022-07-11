"""Git 'commit-msg' hook management."""
import os
from pathlib import Path

from .exceptions import HookException


class HookHandler:
    """Class that handles git hook operations."""

    COMMAND = "clint --file $1"
    ROOT_DIR = os.path.abspath(os.getcwd()).split(os.sep)[0] + os.sep

    def __init__(self):
        self.path = self._get_repo_root()
        self.hook_filepath = Path(
            os.path.join(self.path, ".git", "hooks", "commit-msg")
        )

    @staticmethod
    def _get_repo_root() -> str:
        """
        Get repository root.

        Returns
        -------
        str:
            Root if inside git repository.

        Raises
        ------
        HookException
            If not inside git repository.
        """
        current = os.getcwd()
        while current != HookHandler.ROOT_DIR:
            if Path(os.path.join(current, ".git")).is_dir():
                break
            current = os.path.abspath(os.path.join(current, ".."))
        if current == HookHandler.ROOT_DIR:
            raise HookException("Not in a git repository.")
        return current

    @property
    def is_enabled(self) -> bool:
        """Indicate if the hook is enabled or not."""
        if not self.hook_filepath.is_file():
            return False
        with open(self.hook_filepath, mode="r", encoding="utf8") as hook_file:
            hook_content = hook_file.read()
        return self.COMMAND in hook_content

    def enable(self) -> str:
        """
        Enable hook for a specific git repository.

        Returns
        -------
        str:
            Message for the final user.
        """
        if self.is_enabled:
            return "Hook already enabled in this repository."
        if not self.hook_filepath.is_file():
            with open(self.hook_filepath, mode="w", encoding="utf8"):
                pass
            os.chmod(self.hook_filepath, 0o755)
        with open(self.hook_filepath, mode="a", encoding="utf8") as hook_file:
            hook_file.write(f"{self.COMMAND}\n")
        return f"Hook enabled at {self.hook_filepath}"

    def disable(self) -> str:
        """
        Disable hook for a specific git repository.

        Returns
        -------
        str:
            Message for the final user.
        """
        if not self.is_enabled:
            return "Hook it is not enabled in this repository."
        with open(self.hook_filepath, mode="r", encoding="utf8") as hook_file:
            hooks = hook_file.readlines()
        hooks.remove(f"{self.COMMAND}\n")
        if not hooks:
            os.remove(self.hook_filepath)
        else:
            with open(self.hook_filepath, mode="w", encoding="utf8") as hook_file:
                hook_file.write("".join(hooks))
        return f"Hook disabled at {self.hook_filepath}"
