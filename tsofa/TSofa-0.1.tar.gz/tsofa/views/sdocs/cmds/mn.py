# Local package imports.
from tsofa.views.sdocs import mn
from tsofa.views.sdocs.cmds._base import Command as Base


class Command(Base):

    module = mn
    tmpl = '%Y-%m-%dT%H:%M%z'


def main():
    Command.run()
