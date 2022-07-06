import configparser
import os
import pathlib
import shutil
import subprocess
import sys


def make_link(src, dest):
    try:
        os.symlink(src, dest)
    except OSError as err:
        print("Could not create symlink!")
        print("     Error: ", err)
        if sys.platform == "win32":
            # https://stackoverflow.com/questions/32877260/privlege-error-trying-to-create-symlink-using-python-on-windows-10
            print("Trying to create a junction instead of a symlink...")
            proc = subprocess.check_call(f"mklink /J {dest} {src}", shell=True)
            if proc != 0:
                print("Could not create link!")


def install_gdsdiff() -> None:
    home = pathlib.Path.home()
    git_config_path = home / ".gitconfig"
    git_attributes_path = home / ".gitattributes"

    if git_config_path.exists():
        git_config_str = open(git_config_path).read()
    else:
        git_config_str = "empty"

    git_attributes_str = (
        open(git_attributes_path).read() if git_attributes_path.exists() else "empty"
    )

    if "gds_diff" not in git_config_str:
        write_git_config(git_config_path)
    if "gds_diff" not in git_attributes_str:
        print("Appending the gdsdiff command to your ~/.gitattributes")

        with open(git_attributes_path, "a") as f:
            f.write("*.gds diff=gds_diff\n")


def write_git_config(git_config_path):
    print("gdsdiff shows boolean differences in Klayout")
    print("git diff FILE.GDS")
    print("Appending the gdsdiff command to your ~/.gitconfig")

    config = configparser.RawConfigParser()
    config.read(git_config_path)
    key = 'diff "gds_diff"'

    if key not in config.sections():
        config.add_section(key)
        config.set(key, "command", "python -m gdsfactory.gdsdiff.gds_diff_git")
        config.set(key, "binary", "True")

        with open(git_config_path, "w+") as f:
            config.write(f, space_around_delimiters=True)


def get_klayout_path() -> pathlib.Path:
    klayout_folder = "KLayout" if sys.platform == "win32" else ".klayout"
    home = pathlib.Path.home()
    return home / klayout_folder


def install_klive() -> None:
    dest_folder = get_klayout_path() / "pymacros"
    dest_folder.mkdir(exist_ok=True, parents=True)
    cwd = pathlib.Path(__file__).resolve().parent
    src = cwd / "klayout" / "pymacros" / "klive.lym"
    dest = dest_folder / "klive.lym"

    if dest.exists():
        print(f"removing klive already installed in {dest}")
        os.remove(dest)

    shutil.copy(src, dest)
    print(f"klive installed to {dest}")


def copy(src: pathlib.Path, dest: pathlib.Path) -> None:
    """overwrite file or directory"""
    dest_folder = dest.parent
    dest_folder.mkdir(exist_ok=True, parents=True)

    if dest.exists() or dest.is_symlink():
        print(f"removing {dest} already installed")
        if dest.is_dir():
            shutil.rmtree(dest)
        else:
            os.remove(dest)

    if src.is_dir():
        shutil.copytree(src, dest)
    else:
        shutil.copy(src, dest)
    print(f"{src} copied to {dest}")


def install_generic_tech() -> None:
    klayout_folder = "KLayout" if sys.platform == "win32" else ".klayout"
    cwd = pathlib.Path(__file__).resolve().parent
    home = pathlib.Path.home()
    src = cwd / "klayout" / "tech"
    dest = home / klayout_folder / "tech" / "generic"

    if not dest.exists():
        try:
            make_link(src, dest)
        except Exception:
            os.remove(dest)
            make_link(src, dest)
        print(f"layermap installed to {dest}")

    src = cwd / "klayout" / "drc" / "generic.lydrc"
    dest = home / klayout_folder / "drc" / "generic.lydrc"

    if not dest.exists():
        try:
            make_link(src, dest)
        except Exception:
            os.remove(dest)
            make_link(src, dest)


if __name__ == "__main__":
    cwd = pathlib.Path(__file__).resolve().parent
    home = pathlib.Path.home()
    src = cwd / "klayout" / "tech"

    install_gdsdiff()
    install_klive()
    install_generic_tech()
