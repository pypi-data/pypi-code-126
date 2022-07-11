

from ebs.signagenode.app import SignageApplication
from .node import RsrtcNode


class RsrtcApplication(SignageApplication):
    _node_class = RsrtcNode
