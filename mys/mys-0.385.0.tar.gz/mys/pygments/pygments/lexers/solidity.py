"""
    pygments.lexers.solidity
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Lexers for Solidity.

    :copyright: Copyright 2006-2021 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re

from pygments.lexer import RegexLexer
from pygments.lexer import bygroups
from pygments.lexer import include
from pygments.lexer import words
from pygments.token import Comment
from pygments.token import Keyword
from pygments.token import Name
from pygments.token import Number
from pygments.token import Operator
from pygments.token import Punctuation
from pygments.token import String
from pygments.token import Text
from pygments.token import Whitespace

__all__ = ['SolidityLexer']


class SolidityLexer(RegexLexer):
    """
    For Solidity source code.

    .. versionadded:: 2.5
    """

    name = 'Solidity'
    aliases = ['solidity']
    filenames = ['*.sol']
    mimetypes = []

    flags = re.MULTILINE | re.UNICODE

    datatype = (
        r'\b(address|bool|(?:(?:bytes|hash|int|string|uint)(?:8|16|24|32|40|48|56|64'
        r'|72|80|88|96|104|112|120|128|136|144|152|160|168|176|184|192|200|208'
        r'|216|224|232|240|248|256)?))\b'
    )

    tokens = {
        'root': [
            include('whitespace'),
            include('comments'),
            (r'\bpragma\s+solidity\b', Keyword, 'pragma'),
            (r'\b(contract)(\s+)([a-zA-Z_]\w*)',
             bygroups(Keyword, Whitespace, Name.Entity)),
            (datatype + r'(\s+)((?:external|public|internal|private)\s+)?' +
             r'([a-zA-Z_]\w*)',
             bygroups(Keyword.Type, Whitespace, Keyword, Name.Variable)),
            (r'\b(enum|event|function|struct)(\s+)([a-zA-Z_]\w*)',
             bygroups(Keyword.Type, Whitespace, Name.Variable)),
            (r'\b(msg|block|tx)\.([A-Za-z_][a-zA-Z0-9_]*)\b', Keyword),
            (words((
                'block', 'break', 'constant', 'constructor', 'continue',
                'contract', 'do', 'else', 'external', 'false', 'for',
                'function', 'if', 'import', 'inherited', 'internal', 'is',
                'library', 'mapping', 'memory', 'modifier', 'msg', 'new',
                'payable', 'private', 'public', 'require', 'return',
                'returns', 'struct', 'suicide', 'throw', 'this', 'true',
                'tx', 'var', 'while'), prefix=r'\b', suffix=r'\b'),
             Keyword.Type),
            (words(('keccak256',), prefix=r'\b', suffix=r'\b'), Name.Builtin),
            (datatype, Keyword.Type),
            include('constants'),
            (r'[a-zA-Z_]\w*', Text),
            (r'[!<=>+*/-]', Operator),
            (r'[.;:{}(),\[\]]', Punctuation)
        ],
        'comments': [
            (r'//(\n|[\w\W]*?[^\\]\n)', Comment.Single),
            (r'/(\\\n)?[*][\w\W]*?[*](\\\n)?/', Comment.Multiline),
            (r'/(\\\n)?[*][\w\W]*', Comment.Multiline)
        ],
        'constants': [
            (r'("(\\"|.)*?")', String.Double),
            (r"('(\\'|.)*?')", String.Single),
            (r'\b0[xX][0-9a-fA-F]+\b', Number.Hex),
            (r'\b\d+\b', Number.Decimal),
        ],
        'pragma': [
            include('whitespace'),
            include('comments'),
            (r'(\^|>=|<)(\s*)(\d+\.\d+\.\d+)',
             bygroups(Operator, Whitespace, Keyword)),
            (r';', Punctuation, '#pop')
        ],
        'whitespace': [
            (r'\s+', Whitespace),
            (r'\n', Whitespace)
        ]
    }
