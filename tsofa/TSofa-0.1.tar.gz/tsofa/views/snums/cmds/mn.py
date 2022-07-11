# Local package imports.
from tsofa.views.snums import mn
from tsofa.views.snums.cmds._base import Command as Base


class Command(Base):

    module = mn
    tmpl = '%Y-%m-%dT%H:%M%z'


def main():
    Command.run()
