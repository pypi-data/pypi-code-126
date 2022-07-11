# template.py
version = '1.74.0'

template = {
    'logo': '<n>   {●}<n>    ║SON<n>    ╠══╦══<n>  ══╝  ║<n>       ║REE VIEWER          v-' + str(version),
    'description': 'jtv, a command line utility for visualising JSON and YAML schemas as text trees',
    'synopsis': 'jtv -h|-j|-y [--mode first|union|distinct]',
    'sections': {
        'Flags': [
            {
                'flag': '-h',
                'help': 'Show this message'
            },
            {
                'flag': '-j',
                'help': 'Read JSON from stream'
            },
            {
                'flag': '-y',
                'help': 'Read YAML from stream'
            }
        ],
        'Options': [
            {
                'option': '--mode first|union|distinct',
                'help': 'Array evaluation mode.'
            }
        ],
        'Examples': [
            {
                'description': 'Read JSON from stream:',
                'command': '$ echo \'{"0": {"00": [{"000": "", "001": true, "002": []}]}, "1": {"10": []}}\' | jtv -j'
            },
            {
                'description': 'Read YAML from stream:',
                'command': '$ cat file.yml | jtv -y'
            }
        ],
        'Legend': [
            {
                'item': '{object_node}',
                'description': ''
            },
            {
                'item': '[array_node] ',
                'description': ''
            },
            {
                'item': '"string_node"',
                'description': ''
            },
            {
                'item': 'boolean_node ',
                'description': ''
            },
            {
                'item': 'null_node    ',
                'description': ''
            },
            {
                'item': 'int_node     ',
                'description': ''
            },
            {
                'item': 'float_node   ',
                'description': ''
            },
        ],
    },
    'theme': {
        'padding': {
            'bypass': False,
            'top': 2,
            'bottom': 2,
            'indent': 2
        },
        'colors': {
            'text': {
                'bypass': True,
                'fg': 'white',
                'bg': 'default'
            },
            'titles': {
                'bypass': True,
                'fg': 'orange',
                'bg': 'default'
            },
            'input_format': {
                'json': 'orange',
                'yaml': 'red'
            },
            'highlight': [
                {
                    'text': 'JSON',
                    'fg': 'orange',
                    'bg': 'default'
                },
                {
                    'text': 'YAML',
                    'fg': 'red',
                    'bg': 'default'
                },
                {
                    'text': 'file ',
                    'fg': 'green',
                    'bg': 'default'
                },
                {
                    'text': 'filename',
                    'fg': 'green',
                    'bg': 'default'
                },
                {
                    'text': 'first',
                    'fg': 'green',
                    'bg': 'default'
                },
                {
                    'text': 'union',
                    'fg': 'green',
                    'bg': 'default'
                },
                {
                    'text': 'Array',
                    'fg': 'blue',
                    'bg': 'default'
                },
                {
                    'text': 'Object',
                    'fg': 'orange',
                    'bg': 'default'
                },
                {
                    'text': 'distinct',
                    'fg': 'green',
                    'bg': 'default'
                },
                {
                    'text': 'file.json',
                    'fg': 'green',
                    'bg': 'default'
                },
                {
                    'text': 'file.yml',
                    'fg': 'red',
                    'bg': 'default'
                },
                {
                    'text': 'object_node',
                    'fg': 'orange',
                    'bg': 'default'
                },
                {
                    'text': 'array_node',
                    'fg': 'blue',
                    'bg': 'default'
                },
                {
                    'text': 'string_node',
                    'fg': 'green',
                    'bg': 'default'
                },
                {
                    'text': 'boolean_node',
                    'fg': 'magenta',
                    'bg': 'default'
                },
                {
                    'text': 'null_node',
                    'fg': 'grey',
                    'bg': 'default'
                },
                {
                    'text': 'int_node',
                    'fg': 'cyan',
                    'bg': 'default'
                },
                {
                    'text': 'float_node',
                    'fg': 'red',
                    'bg': 'default'
                },
                {
                    'text': '●',
                    'fg': 'orange',
                    'bg': 'default'
                },
                {
                    'text': '{"0": {"00": [{"000": "", "001": true, "002": []}]}, "1": {"10": []}}',
                    'fg': 'orange',
                    'bg': 'default'
                },
                {
                    'text': '$',
                    'fg': 'green',
                    'bg': 'default'
                }
            ]
        }
    }
}
