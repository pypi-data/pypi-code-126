#!/usr/bin/env python3

import os
import shutil
import logging
import typing

from .model import ComparisonNode, DirectoryComparisonNode, ACTION, TYPE


class Synchronizer:

	def __init__(self, log: logging.Logger = logging.root) -> None:
		self.running = True
		self.log = log

	def sync(self, node: ComparisonNode) -> None:
		if not self.running:
			self.log.warning('aborting synchronization')
			return

		if node.action is ACTION.NONE:
			pass
		elif node.action is ACTION.IGNORE:
			self.log.info(f'ignoring {node}')
		elif isinstance(node, DirectoryComparisonNode):
			self.sync_dir(node)
		else:
			self.sync_file(node)
	
	def sync_file(self, node: ComparisonNode) -> None:
		if node.action is ACTION.CREATE:
			self.copy_file(node.path_src, node.path_dst)
		elif node.action is ACTION.DELETE:
			self.remove_file(node.path_dst)
		elif node.action is ACTION.UNDO_CREATE:
			self.remove_file(node.path_src)
		elif node.action is ACTION.UNDO_DELETE:
			self.copy_file(node.path_dst, node.path_src)

		# ComparisonNode only
		elif node.action is ACTION.UPDATE:
			self.copy_file(node.path_src, node.path_dst)
		elif node.action is ACTION.DOWNGRADE:
			self.copy_file(node.path_src, node.path_dst)
		elif node.action is ACTION.UNDO_UPDATE:
			self.copy_file(node.path_dst, node.path_src)
		elif node.action is ACTION.UNDO_DOWNGRADE:
			self.copy_file(node.path_dst, node.path_src)
		else:
			assert False

	def sync_dir(self, node: DirectoryComparisonNode) -> None:
		if node.action is ACTION.CREATE:
			self.copy_dir(node.path_src, node.path_dst, node.loaded_children)
		elif node.action is ACTION.DELETE:
			self.rmdir(node.path_dst)
			return
		elif node.action is ACTION.UNDO_CREATE:
			self.rmdir(node.path_src)
			return
		elif node.action is ACTION.UNDO_DELETE:
			self.copy_dir(node.path_dst, node.path_src, node.loaded_children)

		# DirectoryComparisonNode only
		elif node.action is ACTION.DIR_CHANGE_DESTINATION:
			pass
		elif node.action is ACTION.DIR_CHANGE_SOURCE:
			pass
		elif node.action is ACTION.DIR_CHANGE_BOTH:
			pass

		elif node.action is ACTION.CHANGE_DESTINATION_TYPE:
			if node.type_dst == TYPE.DIRECTORY:
				self.rmdir(node.path_dst)
				self.copy_file(node.path_src, node.path_dst)
				return
			else:
				self.remove_file(node.path_dst)
				self.copy_dir(node.path_src, node.path_dst, node.loaded_children)
		elif node.action is ACTION.CHANGE_SOURCE_TYPE:
			if node.type_src == TYPE.DIRECTORY:
				self.rmdir(node.path_src)
				self.copy_file(node.path_dst, node.path_src)
				return
			else:
				self.remove_file(node.path_src)
				self.copy_dir(node.path_dst, node.path_src, node.loaded_children)

		elif node.action is ACTION.CREATE_DIRECTORY_BUT_DELETE_SOME_CHILDREN:
			self.copy_dir(node.path_src, node.path_dst, node.loaded_children)
		elif node.action is ACTION.UNDO_DELETE_DIRECTORY_BUT_DELETE_SOME_CHILDREN:
			self.copy_dir(node.path_dst, node.path_src, node.loaded_children)
		elif node.action is ACTION.CHANGE_DESTINATION_TYPE_BUT_DELETE_SOME_CHILDREN:
			assert node.type_dst == TYPE.FILE
			self.remove_file(node.path_dst)
			self.copy_dir(node.path_src, node.path_dst, node.loaded_children)
		elif node.action is ACTION.CHANGE_SOURCE_TYPE_BUT_DELETE_SOME_CHILDREN:
			assert node.type_src == TYPE.FILE
			self.remove_file(node.path_src)
			self.copy_dir(node.path_dst, node.path_src, node.loaded_children)
		else:
			assert False

		for c in node.children:
			self.sync(c)


	def copy_file(self, path1: str, path2: str) -> None:
		'''
		copy2() uses copystat() to copy the file metadata.
		But: Even the higher-level file copying functions (shutil.copy(), shutil.copy2()) cannot copy all file metadata.
		On POSIX platforms, this means that file owner and group are lost as well as ACLs.
		On Mac OS, the resource fork and other metadata are not used. This means that resources will be lost and file type and creator codes will not be correct.
		On Windows, file owners, ACLs and alternate data streams are not copied.
		https://docs.python.org/3/library/shutil.html
		'''
		assert path1 != path2
		logging.info('cp %r %r', path1, path2)
		shutil.copy2(path1, path2)

	def remove_file(self, path: str) -> None:
		logging.info('rm %r', path)
		os.remove(path)


	def copy_dir(self, path1: str, path2: str, without_children: bool) -> None:
		if without_children:
			self.mkdir(path1, path2)
		else:
			self.copy_tree(path1, path2)

	def mkdir(self, path1: str, path2: str) -> None:
		'''
		create directory `path2` with same permissions like directory `path1`
		'''
		assert path1 != path2
		logging.info('mkdir %r  (with permissions from %r)', path2, path1)
		os.mkdir(path2)
		shutil.copystat(path1, path2)

	def copy_tree(self, path1: str, path2: str) -> None:
		'''
		copy directory `path1` to `path2` including all contained files and subdirectories. `path1` must not exist yet.
		'''
		shutil.copytree(path1, path2, dirs_exist_ok=False)

	def rmdir(self, path: str) -> None:
		'''
		remove directory `path` and all of it's content
		'''
		logging.info('rm -r %r', path)
		shutil.rmtree(path)
