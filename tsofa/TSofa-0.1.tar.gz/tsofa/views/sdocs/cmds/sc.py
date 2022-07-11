# Local package imports.
from tsofa.views.sdocs import sc
from tsofa.views.sdocs.cmds._base import Command as Base


class Command(Base):
    module = sc


def main():
    Command.run()
