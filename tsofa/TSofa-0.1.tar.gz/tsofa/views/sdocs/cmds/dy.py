# Local package imports.
from tsofa.views.sdocs import dy
from tsofa.views.sdocs.cmds._base import Command as Base


class Command(Base):

    module = dy
    tmpl = '%Y-%m-%d'


def main():
    Command.run()
