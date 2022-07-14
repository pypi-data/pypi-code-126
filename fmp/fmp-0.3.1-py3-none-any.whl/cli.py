#!/usr/bin/env python
# coding: utf-8

from rich.console import Console

from fmp.fmp import main, opts


def _cli():
    args = opts()
    
    for file in args.files:
        if len(args.files) > 1:
            print()
            Console().rule(file)

        main(file, **vars(args))
