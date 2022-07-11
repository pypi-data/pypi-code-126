# app.py
import sys
import json
import yaml
from colr import color
from click import echo, exceptions
from .template import template


INVALID_YAML_ERROR = 'Error: expecting {} format.\n'.format(color('YAML', template['theme']['colors']['input_format']['yaml']))
INVALID_JSON_ERROR = 'Error: expecting {} format.\n'.format(color('JSON', template['theme']['colors']['input_format']['json']))


def validate_buffer(stdin, _format='json'):
    root_node = None
    input_buffer = ''.join([line for line in stdin])
    if (_format == 'json'):
        try:
            root_node = json.loads(input_buffer)
        except:
            echo(INVALID_JSON_ERROR)
            sys.exit(0)
    elif (_format == 'yaml'):
        try:
            root_node = yaml.load(input_buffer, Loader=yaml.FullLoader)
        except:
            echo(INVALID_YAML_ERROR)
            sys.exit(0)
    return root_node


def usage_error(cli):
    def show(self):
        _help.display()
    exceptions.UsageError.show = show


class Help:
    def __init__(self):
        self.template = template
        self.padding_top = ''
        self.padding_bottom = ''
        self.padding_indent = ''
        self.padding_bypass = False
        self.__set_format__()

    def __set_format__(self):
        try:
            self.padding_bypass = self.template['theme']['padding']['bypass']
            if not self.padding_bypass:
                try:
                    self.padding_top = '\n' * self.template['theme']['padding']['top']
                except:
                    pass
                try:
                    self.padding_bottom = '\n' * self.template['theme']['padding']['bottom']
                except:
                    pass
                try:
                    self.padding_indent = ' ' * self.template['theme']['padding']['indent']
                except:
                    pass
        except:
            pass

    def display(self):
        body = ''
        for i in self.template['logo'].split('<n>'):
            body += i + '\n'

        body += '\n'
        body += self.padding_indent + 'Description:\n'
        body += 2 * self.padding_indent + self.template['description'] + '\n'

        body += '\n'
        body += self.padding_indent + 'Synopsis:\n'
        body += 2 * self.padding_indent + self.template['synopsis'] + '\n'

        body += '\n'
        body += self.padding_indent + 'Flags:\n'
        for flag in self.template['sections']['Flags']:
            body += self.padding_indent * 2 + flag['flag'] + ': ' + flag['help'] + '\n'

        body += '\n'
        body += self.padding_indent + 'Options:\n'
        for option in self.template['sections']['Options']:
            body += self.padding_indent * 2 + option['option'] + ': ' + option['help'] + '\n'

        body += '\n'
        body += self.padding_indent + 'Examples:\n'
        for option in self.template['sections']['Examples']:
            body += self.padding_indent * 2 + option['description'] + '\n' + 2 * self.padding_indent + option['command'] + self.padding_top

        body += self.padding_indent + 'Legend:\n'
        for option in self.template['sections']['Legend']:
            body += self.padding_indent * 2 + option['item'] + '\n'

        echo(self.__colourise__(body))

    def __colourise__(self, body):
        r = body
        for title in ['Flags', 'Options', 'Description', 'Examples', 'Legend', 'Synopsis']:
            r = r.replace(title, color(title, fore=self.template['theme']['colors']['titles']['fg'], style='bright'))

        for highlight in self.template['theme']['colors']['highlight']:
            r = r.replace(highlight['text'], color(highlight['text'], fore=highlight['fg'], style='bright'))

        return r


_help = Help()
