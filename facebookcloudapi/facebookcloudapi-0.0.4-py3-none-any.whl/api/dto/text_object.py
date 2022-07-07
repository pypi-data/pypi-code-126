from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TextObject:
    body: str
    preview_url: bool = False

    def to_dict(self):
        return {
            "body": self.body,
            "preview_url": self.preview_url
        }
