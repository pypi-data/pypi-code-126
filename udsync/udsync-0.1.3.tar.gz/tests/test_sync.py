#!/usr/bin/env pytest

import os
import time
import logging

from udsync.model import ComparisonNode, DirectoryComparisonNode, STATE, ACTION
from udsync.sync import Synchronizer

from test_model import PATH_SRC, PATH_DST, create_test_dir, create_dir, create_file, copy_file


def assert_file(*path: str, content: str) -> None:
	ffn = os.path.sep.join(path)
	assert os.path.isfile(ffn)
	with open(ffn, 'rt') as f:
		assert f.read() == content

def assert_no_file(*path: str) -> None:
	ffn = os.path.sep.join(path)
	assert not os.path.exists(ffn)


# ------- src -> dst -------

def test_files() -> None:
	data = ''
	create_file(PATH_DST, 'newer', content='this is the old version from dst' + data)
	create_file(PATH_SRC, 'older', content='this is the old version from src')
	# wait a sec so that older is recognized as older (and not newer)
	time.sleep(1)

	fn = create_file(PATH_SRC, 'same', content='unchanged')
	copy_file(fn, PATH_DST, 'same')

	create_file(PATH_SRC, 'new', content='a new file')
	create_file(PATH_DST, 'deleted', content='a deleted file')

	create_file(PATH_SRC, 'newer', content='this is the new version from src')
	create_file(PATH_DST, 'older', content='this is the new version from dst' + data)


	n = ComparisonNode('test', PATH_SRC, PATH_DST)
	assert n.state == STATE.MODIFIED_DIR
	Synchronizer().sync(n)

	n.update()
	assert n.state == STATE.SAME

	assert_file(PATH_SRC, 'newer', content='this is the new version from src')
	assert_file(PATH_DST, 'newer', content='this is the new version from src')

	assert_file(PATH_SRC, 'older', content='this is the old version from src')
	assert_file(PATH_DST, 'older', content='this is the old version from src')

	assert_file(PATH_SRC, 'same', content='unchanged')
	assert_file(PATH_DST, 'same', content='unchanged')

	assert_file(PATH_SRC, 'new', content='a new file')
	assert_file(PATH_DST, 'new', content='a new file')

	assert_no_file(PATH_SRC, 'deleted')
	assert_no_file(PATH_DST, 'deleted')



def test_dir() -> None:
	create_dir (PATH_SRC, 'changed-to-dir')
	create_file(PATH_SRC, 'changed-to-dir', 'f', content='this is now a file in a directory')
	create_file(PATH_DST, 'changed-to-dir', content='this used to be a file')

	create_file(PATH_SRC, 'changed-to-file', content='this is now a file')
	create_dir (PATH_DST, 'changed-to-file')
	create_file(PATH_DST, 'changed-to-file', 'f', content='this used to be a file in a directory')

	create_dir(PATH_SRC, 'empty')
	create_dir(PATH_DST, 'empty')

	fns = []
	p = create_dir(PATH_SRC, 'same')
	fns.append(p)
	fns.append(create_dir (p, 'subdir-a'))
	fns.append(create_file(p, 'subdir-a', 'f0', content='a0'))
	fns.append(create_file(p, 'subdir-a', 'f1', content='a1'))
	fns.append(create_file(p, 'subdir-a', 'f2', content='a2'))
	fns.append(create_dir (p, 'subdir-b'))
	fns.append(create_file(p, 'subdir-b', 'f0', content='b0'))
	fns.append(create_file(p, 'subdir-b', 'f1', content='b1'))
	fns.append(create_file(p, 'subdir-b', 'f2', content='b2'))

	p = create_dir (PATH_SRC, 'different')
	fns.append(p)
	fns.append(create_dir (p, 'subdir-a'))
	fns.append(create_file(p, 'subdir-a', 'f0', content='a0'))
	fns.append(create_file(p, 'subdir-a', 'f1', content='a1'))
	fns.append(create_file(p, 'subdir-a', 'f2', content='a2'))
	fns.append(create_dir (p, 'subdir-b'))
	fns.append(create_file(p, 'subdir-b', 'f0', content='b0'))
	fns.append(create_file(p, 'subdir-b', 'f1', content='b1'))
	fns.append(create_file(p, 'subdir-b', 'f2', content='b2'))
	fns.append(create_dir (p, 'subdir-different'))

	for fn in fns:
		fn_dst = PATH_DST + fn.removeprefix(PATH_SRC)
		if os.path.isdir(fn):
			create_dir(fn_dst)
		else:
			copy_file(fn, fn_dst)

	create_file(PATH_SRC, 'different', 'subdir-different', 'foo', content='foo')
	create_file(PATH_DST, 'different', 'subdir-different', 'bar', content='bar')


	n = ComparisonNode('test', PATH_SRC, PATH_DST)
	assert n.state == STATE.MODIFIED_DIR
	Synchronizer().sync(n)

	n.update()
	assert n.state == STATE.SAME

	assert_file(PATH_SRC, 'different', 'subdir-different', 'foo', content='foo')
	assert_file(PATH_DST, 'different', 'subdir-different', 'foo', content='foo')
	assert_no_file(PATH_SRC, 'different', 'subdir-different', 'bar')
	assert_no_file(PATH_DST, 'different', 'subdir-different', 'bar')

def test__changed_to_dir__after_expand() -> None:
	create_dir (PATH_SRC, 'changed-to-dir')
	create_file(PATH_SRC, 'changed-to-dir', 'f', content='this is now a file in a directory')
	create_file(PATH_DST, 'changed-to-dir', content='this used to be a file')

	n = ComparisonNode('test', PATH_SRC, PATH_DST)
	assert n.state == STATE.MODIFIED_DIR
	nc, = n.children
	assert isinstance(nc, DirectoryComparisonNode)
	nc.set_expanded(True)
	Synchronizer().sync(n)

	n.update()
	assert n.state == STATE.SAME

	create_file(PATH_SRC, 'changed-to-dir', 'f', content='this is now a file in a directory')
	create_file(PATH_DST, 'changed-to-dir', 'f', content='this is now a file in a directory')


def test__create_directory_but_delete_some_children() -> None:
	p = create_dir (PATH_SRC, 'new-dir')
	create_file(p, 'a', content='a')
	create_file(p, 'b', content='b')

	n = ComparisonNode('test', PATH_SRC, PATH_DST)
	nd, = n.children
	assert isinstance(nd, DirectoryComparisonNode)
	nd.set_expanded(True)
	na, nb = nd.children
	nb.toggle_direction()
	assert nb.action == ACTION.UNDO_CREATE
	assert na.action == ACTION.CREATE
	assert nd.action == ACTION.CREATE_DIRECTORY_BUT_DELETE_SOME_CHILDREN
	assert n.action == ACTION.DIR_CHANGE_BOTH
	Synchronizer().sync(n)

	n.update()
	assert n.state == STATE.SAME

	for p in (PATH_SRC, PATH_DST):
		assert_file(p, 'new-dir', 'a', content='a')
		assert_no_file(p, 'new-dir', 'b')

def test__change_destination_type_but_delete_some_children() -> None:
	create_file(PATH_DST, 'changed-to-dir')
	p = create_dir (PATH_SRC, 'changed-to-dir')
	create_file(p, 'a', content='a')
	create_file(p, 'b', content='b')

	n = ComparisonNode('test', PATH_SRC, PATH_DST)
	nd, = n.children
	assert isinstance(nd, DirectoryComparisonNode)
	nd.set_expanded(True)
	na, nb = nd.children
	nb.toggle_direction()
	assert nb.action == ACTION.UNDO_CREATE
	assert na.action == ACTION.CREATE
	assert nd.action == ACTION.CHANGE_DESTINATION_TYPE_BUT_DELETE_SOME_CHILDREN
	assert n.action == ACTION.DIR_CHANGE_BOTH
	Synchronizer().sync(n)

	n.update()
	assert n.state == STATE.SAME

	for p in (PATH_SRC, PATH_DST):
		assert_file(p, 'changed-to-dir', 'a', content='a')
		assert_no_file(p, 'changed-to-dir', 'b')

def test__change_destination_type() -> None:
	create_file(PATH_SRC, 'changed-to-file', content='this is a file')
	p = create_dir (PATH_DST, 'changed-to-file')
	create_file(p, 'a', content='a')
	create_file(p, 'b', content='b')

	n = ComparisonNode('test', PATH_SRC, PATH_DST)
	nd, = n.children
	assert isinstance(nd, DirectoryComparisonNode)
	nd.set_expanded(True)
	na, nb = nd.children
	assert nb.action == ACTION.DELETE
	assert na.action == ACTION.DELETE
	assert nd.action == ACTION.CHANGE_DESTINATION_TYPE
	assert n.action == ACTION.DIR_CHANGE_DESTINATION
	Synchronizer().sync(n)

	n.update()
	assert n.state == STATE.SAME

	for p in (PATH_SRC, PATH_DST):
		assert_file(p, 'changed-to-file', content='this is a file')


# ------- ignore -------

def test__ignore() -> None:
	create_file(PATH_SRC, 'a', content='a file')
	create_file(PATH_SRC, 'b', content='b file')

	n = ComparisonNode('test', PATH_SRC, PATH_DST)
	assert n.state == STATE.MODIFIED_DIR
	na, nb = n.children
	nb.ignore()
	Synchronizer().sync(n)

	n.update()
	assert n.state == STATE.MODIFIED_DIR
	na, nb = n.children
	assert na.state == STATE.SAME
	assert nb.state == STATE.NEW

	assert_file(PATH_SRC, 'a', content='a file')
	create_file(PATH_DST, 'a', content='a file')
	assert_file(PATH_SRC, 'b', content='b file')
	assert_no_file(PATH_DST, 'b')


# ------- dst -> src -------

def test__dst_to_src__file() -> None:
	data = ''
	create_file(PATH_DST, 'newer', content='this is the old version from dst' + data)
	create_file(PATH_SRC, 'older', content='this is the old version from src')
	# wait a sec so that older is recognized as older (and not newer)
	time.sleep(1)

	fn = create_file(PATH_SRC, 'same', content='unchanged')
	copy_file(fn, PATH_DST, 'same')

	create_file(PATH_SRC, 'new', content='a new file')
	create_file(PATH_DST, 'deleted', content='a deleted file')

	create_file(PATH_SRC, 'newer', content='this is the new version from src')
	create_file(PATH_DST, 'older', content='this is the new version from dst' + data)


	n = ComparisonNode('test', PATH_SRC, PATH_DST)
	n.toggle_direction()
	assert n.state == STATE.MODIFIED_DIR
	Synchronizer().sync(n)

	n.update()
	assert n.state == STATE.SAME

	assert_file(PATH_SRC, 'newer', content='this is the old version from dst' + data)
	assert_file(PATH_DST, 'newer', content='this is the old version from dst' + data)

	assert_file(PATH_SRC, 'older', content='this is the new version from dst' + data)
	assert_file(PATH_DST, 'older', content='this is the new version from dst' + data)

	assert_file(PATH_SRC, 'same', content='unchanged')
	assert_file(PATH_DST, 'same', content='unchanged')

	assert_no_file(PATH_SRC, 'new')
	assert_file(PATH_DST, 'deleted', content='a deleted file')



def test__dst_to_src__dir() -> None:
	create_dir (PATH_SRC, 'changed-to-dir')
	create_file(PATH_SRC, 'changed-to-dir', 'f', content='this is now a file in a directory')
	create_file(PATH_DST, 'changed-to-dir', content='this used to be a file')

	create_file(PATH_SRC, 'changed-to-file', content='this is now a file')
	create_dir (PATH_DST, 'changed-to-file')
	create_file(PATH_DST, 'changed-to-file', 'f', content='this used to be a file in a directory')

	create_dir(PATH_SRC, 'empty')
	create_dir(PATH_DST, 'empty')

	fns = []
	p = create_dir(PATH_SRC, 'same')
	fns.append(p)
	fns.append(create_dir (p, 'subdir-a'))
	fns.append(create_file(p, 'subdir-a', 'f0', content='a0'))
	fns.append(create_file(p, 'subdir-a', 'f1', content='a1'))
	fns.append(create_file(p, 'subdir-a', 'f2', content='a2'))
	fns.append(create_dir (p, 'subdir-b'))
	fns.append(create_file(p, 'subdir-b', 'f0', content='b0'))
	fns.append(create_file(p, 'subdir-b', 'f1', content='b1'))
	fns.append(create_file(p, 'subdir-b', 'f2', content='b2'))

	p = create_dir (PATH_SRC, 'different')
	fns.append(p)
	fns.append(create_dir (p, 'subdir-a'))
	fns.append(create_file(p, 'subdir-a', 'f0', content='a0'))
	fns.append(create_file(p, 'subdir-a', 'f1', content='a1'))
	fns.append(create_file(p, 'subdir-a', 'f2', content='a2'))
	fns.append(create_dir (p, 'subdir-b'))
	fns.append(create_file(p, 'subdir-b', 'f0', content='b0'))
	fns.append(create_file(p, 'subdir-b', 'f1', content='b1'))
	fns.append(create_file(p, 'subdir-b', 'f2', content='b2'))
	fns.append(create_dir (p, 'subdir-different'))

	for fn in fns:
		fn_dst = PATH_DST + fn.removeprefix(PATH_SRC)
		if os.path.isdir(fn):
			create_dir(fn_dst)
		else:
			copy_file(fn, fn_dst)

	create_file(PATH_SRC, 'different', 'subdir-different', 'foo', content='foo')
	create_file(PATH_DST, 'different', 'subdir-different', 'bar', content='bar')


	n = ComparisonNode('test', PATH_SRC, PATH_DST)
	n.toggle_direction()
	assert n.state == STATE.MODIFIED_DIR
	Synchronizer().sync(n)

	n.update()
	assert n.state == STATE.SAME

	assert_file(PATH_SRC, 'different', 'subdir-different', 'bar', content='bar')
	assert_file(PATH_DST, 'different', 'subdir-different', 'bar', content='bar')
	assert_no_file(PATH_SRC, 'different', 'subdir-different', 'foo')
	assert_no_file(PATH_DST, 'different', 'subdir-different', 'foo')

def test__dst_to_src__changed_to_dir__after_expand() -> None:
	create_dir (PATH_SRC, 'changed-to-dir')
	create_file(PATH_SRC, 'changed-to-dir', 'f', content='this is now a file in a directory')
	create_file(PATH_DST, 'changed-to-dir', content='this used to be a file')

	n = ComparisonNode('test', PATH_SRC, PATH_DST)
	n.toggle_direction()
	assert n.state == STATE.MODIFIED_DIR
	nc, = n.children
	assert isinstance(nc, DirectoryComparisonNode)
	nc.set_expanded(True)
	Synchronizer().sync(n)

	n.update()
	assert n.state == STATE.SAME

	create_file(PATH_SRC, 'changed-to-dir', content='this used to be a file')
	create_file(PATH_DST, 'changed-to-dir', content='this used to be a file')


def test__undo_delete_directory_but_delete_some_children() -> None:
	p = create_dir (PATH_DST, 'new-dir')
	create_file(p, 'a', content='a')
	create_file(p, 'b', content='b')

	n = ComparisonNode('test', PATH_SRC, PATH_DST)
	n.toggle_direction()
	nd, = n.children
	assert isinstance(nd, DirectoryComparisonNode)
	nd.set_expanded(True)
	na, nb = nd.children
	nb.toggle_direction()
	assert nb.action == ACTION.DELETE
	assert na.action == ACTION.UNDO_DELETE
	assert nd.action == ACTION.UNDO_DELETE_DIRECTORY_BUT_DELETE_SOME_CHILDREN
	assert n.action == ACTION.DIR_CHANGE_BOTH
	Synchronizer().sync(n)

	n.update()
	assert n.state == STATE.SAME

	for p in (PATH_SRC, PATH_DST):
		assert_file(p, 'new-dir', 'a', content='a')
		assert_no_file(p, 'new-dir', 'b')

def test__change_source_type_but_delete_some_children() -> None:
	create_file(PATH_SRC, 'changed-to-file')
	p = create_dir (PATH_DST, 'changed-to-file')
	create_file(p, 'a', content='a')
	create_file(p, 'b', content='b')

	n = ComparisonNode('test', PATH_SRC, PATH_DST)
	n.toggle_direction()
	nd, = n.children
	assert isinstance(nd, DirectoryComparisonNode)
	nd.set_expanded(True)
	na, nb = nd.children
	nb.toggle_direction()
	assert nb.action == ACTION.DELETE
	assert na.action == ACTION.UNDO_DELETE
	assert nd.action == ACTION.CHANGE_SOURCE_TYPE_BUT_DELETE_SOME_CHILDREN
	assert n.action == ACTION.DIR_CHANGE_BOTH
	Synchronizer().sync(n)

	n.update()
	assert n.state == STATE.SAME

	for p in (PATH_SRC, PATH_DST):
		assert_file(p, 'changed-to-file', 'a', content='a')
		assert_no_file(p, 'changed-to-file', 'b')

def test__change_source_type() -> None:
	create_file(PATH_DST, 'changed-to-dir', content='this is a file')
	p = create_dir (PATH_SRC, 'changed-to-dir')
	create_file(p, 'a', content='a')
	create_file(p, 'b', content='b')

	n = ComparisonNode('test', PATH_SRC, PATH_DST)
	n.toggle_direction()
	nd, = n.children
	assert isinstance(nd, DirectoryComparisonNode)
	nd.set_expanded(True)
	na, nb = nd.children
	assert nb.action == ACTION.UNDO_CREATE
	assert na.action == ACTION.UNDO_CREATE
	assert nd.action == ACTION.CHANGE_SOURCE_TYPE
	assert n.action == ACTION.DIR_CHANGE_SOURCE
	Synchronizer().sync(n)

	n.update()
	assert n.state == STATE.SAME

	for p in (PATH_SRC, PATH_DST):
		assert_file(p, 'changed-to-dir', content='this is a file')
