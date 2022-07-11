# Local package imports.
from tsofa.views.svals import mn
from tsofa.views._base_cmd import Command as Base


class Command(Base):

    module = mn
    tmpl = '%Y-%m-%dT%H:%M%z'


def main():
    Command.run()
