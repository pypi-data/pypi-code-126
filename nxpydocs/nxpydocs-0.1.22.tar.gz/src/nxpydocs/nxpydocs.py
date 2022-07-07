import sys
import os
import json
import logging
import click
import yaml
from cli import *
import pprint
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

class NxPyDocs():
    def __init__(self,
                command,
                filetype):
        self.command = command
        self.filetype = filetype
        self.supported_templates = [
                            # 'show access-lists',
                            # 'show bgp process vrf all',
                            # 'show bgp sessions',
                            # 'show cdp neighbors',
                            # 'show cdp neighbors detail',
                            # 'show environment',
                            # 'show interface',
                            # 'show interface status',
                            # 'show interface transceiver',
                            # 'show inventory',
                            # 'show ip arp vrf all',
                            # 'show ip interface brief',
                            # 'show ip ospf',
                            # 'show ip ospf interface',
                            # 'show ip ospf interface vrf all',
                            # 'show ip ospf neighbors detail',
                            # 'show ip ospf neighbors detail vrf all',
                            # 'show ip route',
                            # 'show ip route vrf all',
                            # 'show mac address-table',
                            # 'show port-channel summary',
                            'show version',
                            #'show vlan'
                            ]

    def nxpydocs(self):
        pp = pprint.PrettyPrinter(indent=4)
        if self.command == "all":
            for single_command in self.supported_templates:
                self.command = single_command
                command_output = clid( '%s' % self.command )
                parsed_json = json.loads(command_output)
                pp.pprint(parsed_json)
                if "Cannot" in parsed_json:
                    click.secho("No Data To Create File", fg='red')
                else:
                    if self.filetype:
                        self.pick_filetype(parsed_json)
        else:
            if self.command in self.supported_templates:
                command_output = clid( '%s' % self.command )
                parsed_json = json.loads(command_output)
                pp.pprint(parsed_json)
                if "Cannot" in parsed_json:
                    click.secho("No Data To Create File", fg='red')
                else:
                    if self.filetype:
                        self.pick_filetype(parsed_json)
            else:
                click.secho("Show Command Not Yet Templated", fg='red')

    def pick_filetype(self, parsed_json):
        if self.filetype == "none":
            pass
        elif self.filetype == 'json':
            self.json_file(parsed_json)
        elif self.filetype == 'yaml':
            self.yaml_file(parsed_json)
        elif self.filetype == 'html':
            self.html_file(parsed_json)
        elif self.filetype == 'markdown':
            self.markdown_file(parsed_json)
        elif self.filetype == 'csv':
            self.csv_file(parsed_json)
            self.mindmap_file(parsed_json)           
        elif self.filetype == 'all':
            self.all_files(parsed_json)

    def json_file(self, parsed_json):
        with open(' %s.json' % self.command, 'w') as f:
            f.write(parsed_json)
        click.secho("JSON file created at %s / %s.json" % (sys.path[0],self.command),
        fg='green')

    def yaml_file(self, parsed_json):
        clean_yaml = yaml.dump(json.loads(parsed_json), default_flow_style=False)
        with open(' %s.yaml' % self.command, 'w') as f:
            f.write(clean_yaml)
        click.secho("YAML file created at %s / %s.yaml" % (sys.path[0],self.command),
        fg='green')

    def html_file(self, parsed_json):
        template_dir = Path(__file__).resolve().parent
        env = Environment(loader=FileSystemLoader(str(template_dir)))
        html_template = env.get_template('html.j2')
        html_output = html_template.render(command = self.command,
            data_to_template=json.loads(parsed_json))
        with open('%s.html' % self.command, 'w') as f:
            f.write(html_output)
        click.secho("HTML file created at %s / %s.html" % (sys.path[0],self.command),
            fg='green')

    def markdown_file(self, parsed_json):
        template_dir = Path(__file__).resolve().parent
        env = Environment(loader=FileSystemLoader(str(template_dir)))
        markdown_template = env.get_template('md.j2')
        markdown_output = markdown_template.render(command = self.command,
            data_to_template=json.loads(parsed_json))
        with open('%s.md' % self.command, 'w') as f:
            f.write(markdown_output)
        click.secho("Markdown file created at %s / %s.md" % (sys.path[0],self.command),
            fg='green')

    def csv_file(self, parsed_json):
        template_dir = Path(__file__).resolve().parent
        env = Environment(loader=FileSystemLoader(str(template_dir)))
        csv_template = env.get_template('csv.j2')
        csv_output = csv_template.render(command = self.command,
            data_to_template=json.loads(parsed_json),
            hostname=self.hostname)
        with open('%s.csv' % self.command, 'w') as f:
            f.write(csv_output)
        click.secho("CSV file created at %s / %s.csv" % (sys.path[0],self.command),
            fg='green')

    def mindmap_file(self, parsed_json):
        template_dir = Path(__file__).resolve().parent
        env = Environment(loader=FileSystemLoader(str(template_dir)))
        mindmap_template = env.get_template('mindmap.j2')
        mindmap_output = mindmap_template.render(command = self.command,
            data_to_template=json.loads(parsed_json),
            hostname=self.hostname)
        with open('%s mindmap.md' % self.command, 'w') as f:
            f.write(mindmap_output)
        click.secho(
            "Mindmap file created at %s / %s.md" % (sys.path[0],self.command),
            fg='green')

    def all_files(self, parsed_json):
        self.json_file(parsed_json)
        self.yaml_file(parsed_json)
        self.html_file(parsed_json)
        self.markdown_file(parsed_json)
        self.csv_file(parsed_json)
        self.mindmap_file(parsed_json)

@click.command()
@click.option('--command',
    prompt='Command',
    help=('''A valid Show Command (i.e. "show ip interface brief")'''),
    required=True)
@click.option('--filetype',
    prompt='Filetype',
    type=click.Choice(['none',
                        'json',
                        'yaml',
                        'html',
                        'csv',
                        'markdown',
                        'mindmap',
                        'all'],
        case_sensitive=True),
    help='Filetype to output captured network state to',
    required=False,
    default='none')
def cli(command,
        filetype,
        ):
    invoke_class = NxPyDocs(command,
                            filetype,
                        )
    invoke_class.nxpydocs()

if __name__ == "__main__":
    cli()
