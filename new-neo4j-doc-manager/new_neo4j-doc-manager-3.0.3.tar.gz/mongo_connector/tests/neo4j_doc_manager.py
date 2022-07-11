# -*- coding: utf-8 -*-
# @Time    : 2022/4/29 上午10:53
# @Author  : kyq
# @Software: PyCharm

"""Unit tests - Neo4j DocManager."""
import sys
import unittest2 as unittest
import logging
import os
import time

sys.path[0:0] = [""]

from gridfs import GridFS
from pymongo import MongoClient
from bson.objectid import ObjectId
from py2neo import Graph, Node

from mongo_connector.tests import doc,doc1,doc2,doc3,doc5,doc6,doc7,doc8,doc9,doc10,doc11,doc12,doc13,doc14
from mongo_connector.command_helper import CommandHelper
from mongo_connector.compat import u
from mongo_connector.connector import Connector
from mongo_connector.doc_managers.new_neo4j_doc_manager import DocManager
from mongo_connector.util import retry_until_ok


class Neo4jTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.docman = DocManager('bolt://182.92.157.151:30070', auto_commit_interval=0)
        self.graph = self.docman.graph

    # def setUp(self):
    #     self.graph.delete_all()
    #     return
    #
    # def tearDown(self):
    #     self.docman.graph.delete_all()
    #     self.graph.delete_all()
    #     self.docman = DocManager('http://192.168.3.215:7474/db/data', auto_commit_interval=0)
    #     self.graph = self.docman.graph



    # def test_bulk_test_upsert(self):
    #     self.docman.bulk_upsert([], 'tests.talksbulk', 1)
    #     docs = ({"_id": i} for i in range(1000))
    #     self.docman.bulk_upsert(docs, 'tests.talksbulk', 1)
    #     result = self.graph.node_labels
    #     self.assertIn("talksbulk", result)
    #     nodes = self.graph.find("talksbulk")
    #     total_nodes = 0
    #     for i, node in enumerate(nodes):
    #         self.assertEqual(node['_id'], str(i))
    #         total_nodes += 1
    #     self.assertEqual(total_nodes, 1000)
    #     self.tearDown()

    def test_upsert(self):
        docc = doc8
        self.docman.upsert(docc,'actor_director',1)
        print('Success')
        # result = self.docman.graph.node_labels



    # def test_upsert_with_json_array(self):
    #     docc = doc
    #     self.docman.upsert(docc, 'tests.talks', 1)
    #     result = self.graph.node_labels
    #     self.assertIn("talks", result)
    #     self.assertIn("tracks0", result)
    #     self.assertIn("tracks1", result)
    #     self.assertIn("speaker", result)
    #     self.assertIn("session", result)
    #     self.assertIn("Document", result)
    #     self.assertEqual(self.graph.size, 4)
    #     self.tearDown()
    #
    # def test_upsert_json_array_with_null_element(self):
    #     docc = {'_id': "abc12213bbb", 'session': {'title': '12 Years of Spring: An Open Source Journey'},
    #             'room': 'Auditorium', 'topics': ['keynote', 'spring'],
    #             "tracks": [{"main": "Java"}, {"second": "Languages"}, None],
    #             'speaker': {'twitter': 'https://twitter.com/springjuergen', 'name': 'Juergen Hoeller'},
    #             'timeslot': 'Wed 29th, 09:30-10:30'}
    #     self.docman.upsert(docc, 'tests.jsonarray', 1)
    #     result = self.graph.node_labels
    #     self.assertIn("jsonarray", result)
    #     self.assertIn("tracks0", result)
    #     self.assertIn("tracks1", result)
    #     self.assertIn("speaker", result)
    #     self.assertIn("session", result)
    #     self.assertIn("Document", result)
    #     self.assertEqual(self.graph.size, 4)
    #     self.tearDown()
    #
    #
    #
    # def test_search(self):
    #     """Test the search method.
    #     Make sure we can retrieve documents last modified within a time range.
    #     """
    #     docc = {'_id': '1', 'name': 'John'}
    #     self.docman.upsert(docc, 'tests.search', 5767301236327972865)
    #     docc2 = {'_id': '2', 'name': 'John Paul'}
    #     self.docman.upsert(docc2, 'tests.search', 5767301236327972866)
    #     docc3 = {'_id': '3', 'name': 'Paul'}
    #     self.docman.upsert(docc3, 'tests.search', 5767301236327972870)
    #     search = list(self.docman.search(5767301236327972865,
    #                                      5767301236327972866))
    #     self.assertEqual(len(search), 2)
    #     for result in search:
    #         result_ids = [result[0]["_id"] for result in search]
    #     self.assertIn('1', result_ids)
    #     self.assertIn('2', result_ids)

    @unittest.skip("Not implmented yet")
    def test_get_last_doc(self):
        """Test the get_last_doc method.
        Make sure we can retrieve the document most recently modified from ES.
        """

    @unittest.skip("Not implmented yet")
    def test_commands(self):
        return


if __name__ == '__main__':
    unittest.main()