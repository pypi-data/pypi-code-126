# -*- coding: utf-8 -*-

from functools import partial

import pytcm

from pygitm.options import (AddOptions, CheckoutOptions, CloneOptions,
                            CommitOptions, PullOptions, PushOptions)

git_command = partial(pytcm.execute, "git")


def clone(opts: CloneOptions, cwd: str = ...) -> pytcm.CommandResult:
    return git_command(opts.to_list(), cwd)


def add(opts: AddOptions, cwd: str = ...) -> pytcm.CommandResult:
    return git_command(opts.to_list(), cwd)


def push(opts: PushOptions, cwd: str = ...) -> pytcm.CommandResult:
    return git_command(opts.to_list(), cwd)


def pull(opts: PullOptions, cwd: str = ...) -> pytcm.CommandResult:
    return git_command(opts.to_list(), cwd)


def checkout(opts: CheckoutOptions, cwd: str = ...) -> pytcm.CommandResult:
    return git_command(opts.to_list(), cwd)


def commit(opts: CommitOptions, cwd: str = ...) -> pytcm.CommandResult:
    return git_command(opts.to_list(), cwd)
