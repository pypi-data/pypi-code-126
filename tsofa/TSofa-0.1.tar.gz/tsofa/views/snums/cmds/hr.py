# Local package imports.
from tsofa.views.snums import hr
from tsofa.views.snums.cmds._base import Command as Base


class Command(Base):

    module = hr
    tmpl = '%Y-%m-%dT%H%z'


def main():
    Command.run()
