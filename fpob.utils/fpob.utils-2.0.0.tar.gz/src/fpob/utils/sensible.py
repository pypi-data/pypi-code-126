import os
import shlex
import shutil
import subprocess
import tempfile
import typing as t


def _get_editor() -> t.List[str]:
    editor = os.getenv('EDITOR')
    if editor:
        return shlex.split(editor)

    if shutil.which('sensible-editor'):
        return ['sensible-editor']

    for env in ['VISUAL', 'SELECTED_EDITOR']:
        editor = os.getenv(env)
        if editor:
            return shlex.split(editor)

    for cmd in ['vim', 'vi', 'nano', 'nano-tiny', 'editor']:
        if shutil.which(cmd):
            return [cmd]

    raise RuntimeError("Couldn't find an editor!")


def editor(file: t.Union[str, os.PathLike]) -> None:
    """Edit the file using an editor."""
    subprocess.run(_get_editor() + [str(file)], check=True)


def editor_text(text: str, extension: t.Optional[str] = '.txt') -> str:
    """
    Edit the text using an editor. Extension is `.txt` by default but changing
    it may change syntax highlighting in the editor. Returns the edited text.
    """
    _, file = tempfile.mkstemp(prefix='editor-', suffix=extension)

    try:
        if text is not None:
            with open(file, 'w') as f:
                f.write(text)

        editor(file)

        with open(file, 'r') as f:
            text = f.read()

        return text

    finally:
        os.unlink(file)


def _get_pager() -> t.List[str]:
    pager = os.getenv('PAGER')
    if pager:
        return shlex.split(pager)

    if shutil.which('sensible-pager'):
        return ['sensible-pager']

    for cmd in ['less', 'more', 'pager']:
        if shutil.which(cmd):
            return [cmd]

    raise RuntimeError("Couldn't find a pager!")


def pager(file: t.Union[str, os.PathLike]) -> None:
    """Display the file using a pager."""
    subprocess.run(_get_pager() + [str(file)], check=True)


def pager_text(text: str) -> None:
    """Display the text using a pager."""
    _, file = tempfile.mkstemp(prefix='pager-')

    try:
        if text is not None:
            with open(file, 'w') as f:
                f.write(text)

        pager(file)

    finally:
        os.unlink(file)
