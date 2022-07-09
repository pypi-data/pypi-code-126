"""Oaf provides a simple means of storing artifacts in OCI registries"""

import pickle
from enum import Enum
import os
import shutil
import subprocess
import tempfile
from typing import Any, List, Optional, Dict
from os import listdir
from os.path import isfile, join

import jsonpickle


imgpkg_relpath = os.path.dirname(__file__)
imgpkg_abspath = os.path.abspath(imgpkg_relpath)
BIN_PATHNAME = os.path.join(imgpkg_abspath, "bin/imgpkg")


class ObjEncoderType(Enum):
    """Encoder to use to encode python objects for storage"""

    PICKLE = "pickle"
    JSON_PICKLE = "json_pickle"


def push(
    uri: str,
    file: Optional[str | List[str]] = None,
    obj: Optional[Any | List[Any]] = None,
    obj_map: Optional[Dict[str, Any]] = None,
    obj_encoder: ObjEncoderType = ObjEncoderType.JSON_PICKLE,
    labels: Optional[Dict[str, str]] = None,
) -> None:
    """Push data to registry"""

    args = [
        BIN_PATHNAME,
        "push",
        "-i",
        uri,
    ]
    fps = []

    temp_dir = ""
    if file is not None:
        if isinstance(file, str):
            fps = [file]
        else:
            fps = file

    if obj is not None:
        if obj_map is None:
            obj_map = {}
        if isinstance(obj, list):
            for i, o in enumerate(obj):
                name = type(o).__name__
                if name in obj_map:
                    name = f"{name}-{i}"
                obj_map[name] = o
        else:
            obj_map[type(obj).__name__] = obj

    if obj_map is not None:
        temp_dir = tempfile.mkdtemp()
        for filename, data in obj_map.items():
            filepath = os.path.join(temp_dir, filename)
            if isinstance(data, str):
                with open(filepath, "w", encoding="UTF-8") as f:
                    f.write(data)
                fps.append(filepath)
            else:
                if obj_encoder == ObjEncoderType.JSON_PICKLE:
                    if not filepath.endswith(".json"):
                        filepath = filepath + ".json"
                    with open(filepath, "w", encoding="UTF-8") as f:
                        f.write(jsonpickle.encode(data))
                    fps.append(filepath)
                elif obj_encoder == ObjEncoderType.PICKLE:
                    if not filepath.endswith(".pkl"):
                        filepath = filepath + ".pkl"
                    with open(filepath, "wb") as handle:
                        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
                    fps.append(filepath)

    if len(fps) == 0:
        raise ValueError("Nothing to upload. Must provide one of file, obj, or obj_map")

    for filepath in fps:
        args.append("-f")
        args.append(filepath)

    if labels is not None:
        for k, v in labels.items():
            args.append("-l")
            args.append(f"{k}={v}")

    try:
        subprocess.run(
            args=args,
            capture_output=True,
            check=True,
            text=True,
        )
    except subprocess.CalledProcessError as err:
        print(err.output)
        raise err

    if temp_dir != "":
        shutil.rmtree(temp_dir, ignore_errors=True)


def pull(uri: str, out_path: str) -> List[str]:
    """Pull files from registry"""

    args = [
        BIN_PATHNAME,
        "pull",
        "-i",
        uri,
        "-o",
        out_path,
    ]

    try:
        subprocess.run(
            args=args,
            capture_output=True,
            check=True,
            text=True,
        )
    except subprocess.CalledProcessError as err:
        print(err.output)
        raise err

    filepaths = [f for f in listdir(out_path) if isfile(join(out_path, f))]
    return filepaths


def pull_str(uri: str) -> Dict[str, str]:
    """Pull files from registry as strings"""
    with tempfile.TemporaryDirectory() as out_path:
        args = [
            BIN_PATHNAME,
            "pull",
            "-i",
            uri,
            "-o",
            out_path,
        ]

        try:
            subprocess.run(
                args=args,
                capture_output=True,
                check=True,
                text=True,
            )
        except subprocess.CalledProcessError as err:
            print(err.output)
            raise err

        str_files = {}
        for f in listdir(out_path):
            filepath = join(out_path, f)
            if isfile(filepath):
                with open(filepath, "r", encoding="UTF-8") as fr:
                    str_files[f] = fr.read()

        return str_files


def pull_bytes(uri: str) -> Dict[str, bytes]:
    """Pull files from registry as bytes"""
    with tempfile.TemporaryDirectory() as out_path:
        args = [
            BIN_PATHNAME,
            "pull",
            "-i",
            uri,
            "-o",
            out_path,
        ]

        try:
            subprocess.run(
                args=args,
                capture_output=True,
                check=True,
                text=True,
            )
        except subprocess.CalledProcessError as err:
            print(err.output)
            raise err

        byte_files = {}
        for f in listdir(out_path):
            filepath = join(out_path, f)
            if isfile(filepath):
                with open(filepath, "rb") as fr:
                    byte_files[f] = fr.read()

        return byte_files


# TODO: auto push; detect repo and python project
