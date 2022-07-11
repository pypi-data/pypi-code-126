# Local package imports.
from tsofa.views.snums import sc
from tsofa.views.snums.cmds._base import Command as Base


class Command(Base):
    module = sc


def main():
    Command.run()
