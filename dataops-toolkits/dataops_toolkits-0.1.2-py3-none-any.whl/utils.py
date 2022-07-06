#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Any, Dict, List
from uuid import uuid4

from airium import Airium


def inject_annotation_to_data(export_data: List[Dict]) -> List[Dict]:
    # TODO: solve multi type of tasks
    return export_data


def convert_data(datas: List[Dict], set_uuid=False) -> List[Dict]:
    converted = []
    for data in datas:
        if set_uuid:
            data.update({"_id": uuid4().hex})
        data = {"data": data}
        converted += [data]
    return converted


def load_dataset(name: str, branch="main") -> List[Any]:
    # TODO: use mysql client interface
    return []


def wrap_dialogs_to_html(dialogs, max_width=750):

    _mapping = {
        "client": {"name": "client", "side": "right", "color": "#F8F9F9"},
        "sales": {"name": "sales", "side": "left", "color": "#EAFAF1"},
    }

    a = Airium()
    with a.div(style=f"max-width: {max_width}px"):
        for dialog in dialogs:
            speaker = dialog["speaker"]
            content = dialog["log"]

            # speaker, *_ = list(dialog.keys())
            # content = dialog[speaker]

            side = _mapping[speaker]["side"]
            color = _mapping[speaker]["color"]
            with a.div(style="clear: both"):
                with a.div(
                    style=f"float: {side}; display: inline-block; border: 1px solid #F2F3F4; background-color: {color}; border-radius: 5px; padding: 7px; margin: 10px 0;"
                ):
                    with a.p():
                        a(f"<b>{speaker}</b>: {content}")

    return str(a)
