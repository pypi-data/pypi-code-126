# -*- coding: utf-8 -*-
"""
    pygments.lexers.teal
    ~~~~~~~~~~~~~~~~~~~~

    Lexer for TEAL.

    :copyright: Copyright 2006-2021 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.lexer import RegexLexer
from pygments.lexer import bygroups
from pygments.lexer import include
from pygments.lexer import words
from pygments.token import Comment
from pygments.token import Keyword
from pygments.token import Name
from pygments.token import Number
from pygments.token import String
from pygments.token import Text

__all__ = ['TealLexer']

class TealLexer(RegexLexer):
    """
    For the `Transaction Execution Approval Language (TEAL)
    <https://developer.algorand.org/docs/reference/teal/specification/>`

    For more information about the grammar, see:
    https://github.com/algorand/go-algorand/blob/master/data/transactions/logic/assembler.go

    .. versionadded:: 2.9
    """
    name = 'teal'
    aliases = ['teal']
    filenames = ['*.teal']

    keywords = words({
        'Sender', 'Fee', 'FirstValid', 'FirstValidTime', 'LastValid', 'Note',
        'Lease', 'Receiver', 'Amount', 'CloseRemainderTo', 'VotePK',
        'SelectionPK', 'VoteFirst', 'VoteLast', 'VoteKeyDilution', 'Type',
        'TypeEnum', 'XferAsset', 'AssetAmount', 'AssetSender', 'AssetReceiver',
        'AssetCloseTo', 'GroupIndex', 'TxID', 'ApplicationID', 'OnCompletion',
        'ApplicationArgs', 'NumAppArgs', 'Accounts', 'NumAccounts',
        'ApprovalProgram', 'ClearStateProgram', 'RekeyTo', 'ConfigAsset',
        'ConfigAssetTotal', 'ConfigAssetDecimals', 'ConfigAssetDefaultFrozen',
        'ConfigAssetUnitName', 'ConfigAssetName', 'ConfigAssetURL',
        'ConfigAssetMetadataHash', 'ConfigAssetManager', 'ConfigAssetReserve',
        'ConfigAssetFreeze', 'ConfigAssetClawback', 'FreezeAsset',
        'FreezeAssetAccount', 'FreezeAssetFrozen',
        'NoOp', 'OptIn', 'CloseOut', 'ClearState', 'UpdateApplication',
        'DeleteApplication',
        'MinTxnFee', 'MinBalance', 'MaxTxnLife', 'ZeroAddress', 'GroupSize',
        'LogicSigVersion', 'Round', 'LatestTimestamp', 'CurrentApplicationID',
        'AssetBalance', 'AssetFrozen',
        'AssetTotal', 'AssetDecimals', 'AssetDefaultFrozen', 'AssetUnitName',
        'AssetName', 'AssetURL', 'AssetMetadataHash', 'AssetManager',
        'AssetReserve', 'AssetFreeze', 'AssetClawback',
    }, suffix = r'\b')

    identifier = r'[^ \t\n]+(?=\/\/)|[^ \t\n]+'
    newline = r'\r?\n'
    tokens = {
        'root': [
            include('whitespace'),
            # pragmas match specifically on the space character
            (r'^#pragma .*' + newline, Comment.Directive),
            # labels must be followed by a space,
            # but anything after that is ignored
            ('(' + identifier + ':' + ')' + '([ \t].*)',
                bygroups(Name.Label, Comment.Single)),
            (identifier, Name.Function, 'function-args'),
        ],
        'function-args': [
            include('whitespace'),
            (r'"', String, 'string'),
            (r'(b(?:ase)?(?:32|64) ?)(\(?[a-zA-Z0-9+/=]+\)?)',
                bygroups(String.Affix, String.Other)),
            (r'[A-Z2-7]{58}', Number), # address
            (r'0x[\da-fA-F]+', Number.Hex),
            (r'\d+', Number.Integer),
            (keywords, Keyword),
            (identifier, Name.Attributes),  # branch targets
            (newline, Text, '#pop'),
        ],
        'string': [
            (r'\\(?:["nrt\\]|x\d\d)', String.Escape),
            (r'[^\\\"\n]+', String),
            (r'"', String, '#pop'),
        ],
        'whitespace': [
            (r'[ \t]+', Text),
            (r'//[^\n]+', Comment.Single),
        ],
    }
