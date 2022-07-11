# Local package imports.
from tsofa.views.svals import dy
from tsofa.views._base_cmd import Command as Base


class Command(Base):

    module = dy
    tmpl = '%Y-%m-%d'


def main():
    Command.run()
