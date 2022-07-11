# Local package imports.
from tsofa.views.sobjs import sc
from tsofa.views._base_cmd import Command as Base


class Command(Base):
    module = sc


def main():
    Command.run()
