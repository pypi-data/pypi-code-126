from typing import List

from rdflib import Graph, Literal

from ..ns import *
from .declarations.Post import Post
from .UserAccount import UserAccount


class Post(Post):
    __type__ = SM["Post"]

    hasCreator: UserAccount = None
    postContent: Literal = None
    hasReply: List[Post] = None
    isReplyOf: List[Post] = None

    def _addProperties(self, g: Graph):
        if self.hasCreator:
            g.add((self.uriRef, SM["hasCreator"], self.hasCreator.uriRef))

        if self.postContent:
            g.add((self.uriRef, SM["postContent"], self.postContent))

        if self.hasReply:
            for hasReply in self.hasReply:
                g.add((self.uriRef, SM["hasReply"], hasReply.uriRef))

        if self.isReplyOf:
            for isReplyOf in self.isReplyOf:
                g.add((self.uriRef, SM["isReplyOf"], isReplyOf.uriRef))
