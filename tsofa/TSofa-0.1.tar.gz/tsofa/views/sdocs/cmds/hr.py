# Local package imports.
from tsofa.views.sdocs import hr
from tsofa.views.sdocs.cmds._base import Command as Base


class Command(Base):

    module = hr
    tmpl = '%Y-%m-%dT%H%z'


def main():
    Command.run()
