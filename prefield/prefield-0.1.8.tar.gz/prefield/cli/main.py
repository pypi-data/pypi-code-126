import click
from dotenv import load_dotenv

from prefield.cli.agent_commands import agent
from prefield.cli.flow_commands import flow
from prefield.cli.project_commands import project


@click.group(help="CLI for running/registering Prefect flows, projects and agents")
@click.pass_context
def entry_point(ctx):
    pass


entry_point.add_command(project)
entry_point.add_command(agent)
entry_point.add_command(flow)


def main():
    load_dotenv()
    entry_point()


if __name__ == "__main__":
    main()
