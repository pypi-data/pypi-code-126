import unittest
import pyutils.fsext as fs
import os


class TestShortHand(unittest.TestCase):
    def test_to_base64(self):
        cwd = os.getcwd()
        if not cwd.endswith('tests'):
            os.chdir('tests')
        self.assertEqual(fs.to_base64('abs'), '')
        self.assertNotEqual(fs.to_base64('./data/to_base64.png'), '')
        content = fs.to_base64('./data/to_base64.png', './output/to_base64')
        with open('./output/to_base64', 'r+', encoding='utf-8') as f:
            self.assertEqual(f.readline(), content)
