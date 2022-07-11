# Local package imports.
from tsofa.views.sobjs import hr
from tsofa.views._base_cmd import Command as Base


class Command(Base):

    module = hr
    tmpl = '%Y-%m-%dT%H%z'


def main():
    Command.run()
