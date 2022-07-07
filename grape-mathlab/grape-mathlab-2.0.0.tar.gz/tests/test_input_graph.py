"""TestInputGraph to check input of GeneralGraph"""

from unittest import TestCase
from grape.general_graph import GeneralGraph


class TestInputGraph(TestCase):
    """
	Class TestInputGraph to check input of GeneralGraph
	"""

    def test_Mark(self):
        """
		Unittest check for mark attribute of GeneralGraph:
		correct input reading.
		"""
        g = GeneralGraph()
        g.load("tests/TOY_graph.csv")

        mark_dict = {
            '1': '1',
            '2': '2',
            '3': '3',
            '4': '4',
            '5': '5',
            '6': '6',
            '7': '7',
            '8': '8',
            '9': '9',
            '10': '10',
            '11': '11',
            '12': '12',
            '13': '13',
            '14': '14',
            '15': '15',
            '16': '16',
            '17': '17',
            '18': '18',
            '19': '19'
        }

        self.assertDictEqual(mark_dict, g.mark, msg="Wrong MARK in input")

    def test_init_status(self):
        """
		Unittest check for init_status attribute of GeneralGraph:
		correct input reading.
		"""
        g = GeneralGraph()
        g.load("tests/TOY_graph.csv")

        init_status_dict = {'2': True, '3': True}

        self.assertDictEqual(init_status_dict, g.init_status,
            msg="Wrong INIT STATUS in input")

    def test_description(self):
        """
		Unittest check for description attribute of GeneralGraph:
		correct input reading.
		"""
        g = GeneralGraph()
        g.load("tests/TOY_graph.csv")

        description_dict = {
            '1': '',
            '2': '',
            '3': '',
            '4': '',
            '5': '',
            '6': '',
            '7': '',
            '8': '',
            '9': '',
            '10': '',
            '11': '',
            '12': '',
            '13': '',
            '14': '',
            '15': '',
            '16': '',
            '17': '',
            '18': '',
            '19': ''
        }

        self.assertDictEqual(description_dict, g.description,
            msg=" Wrong DESCRIPTION in input ")

    def test_type(self):
        """
		Unittest check for type attribute of GeneralGraph:
		correct input reading.
		"""
        g = GeneralGraph()
        g.load("tests/TOY_graph.csv")

        type_dict = {
            '1': 'SOURCE',
            '2': 'SWITCH',
            '3': 'SWITCH',
            '4': 'HUB',
            '5': 'HUB',
            '6': 'HUB',
            '7': 'HUB',
            '8': 'HUB',
            '9': 'HUB',
            '10': 'HUB',
            '11': 'HUB',
            '12': 'HUB',
            '13': 'HUB',
            '14': 'HUB',
            '15': 'SOURCE',
            '16': 'HUB',
            '17': 'HUB',
            '18': 'USER',
            '19': 'HUB'
        }

        self.assertDictEqual(type_dict, g.type, msg="Wrong TYPE in input")

    def test_weight(self):
        """
		Unittest check for Weight attribute of GeneralGraph:
		correct input reading.
		"""
        g = GeneralGraph()
        g.load("tests/TOY_graph.csv")

        weight_dict = {
			('1', '2'): 1.0,
			('1', '3'): 1.0,
			('2', '4'): 1.0,
			('3', '5'): 1.0,
			('4', '6'): 1.0,
			('5', '11'): 1.0,
			('6', '7'): 1.0,
			('6', '8'): 1.0,
			('7', '6'): 1.0,
			('8', '6'): 1.0,
			('8', '9'): 1.0,
			('9', '16'): 1.0,
			('15', '9'): 1.0,
			('16', '17'): 1.0,
			('17', '16'): 1.0,
			('17', '10'): 1.0,
			('10', '11'): 1.0,
			('11', '19'): 1.0,
			('19', '12'): 1.0,
			('19', '14'): 1.0,
			('12', '19'): 1.0,
			('12', '13'): 1.0,
			('14', '19'): 1.0,
			('14', '13'): 1.0,
			('14', '18'): 1.0,
			('13', '12'): 1.0,
			('13', '14'): 1.0
        }

        self.assertDictEqual(weight_dict, g.weight, msg="Wrong WEIGHT in input")

    def test_initial_service(self):
        """
		Unittest check for initial_service attribute of GeneralGraph:
		correct input reading.
		"""
        g = GeneralGraph()
        g.load("tests/TOY_graph.csv")

        initial_service_dict = {
            '1': 1.0,
            '2': 0.0,
            '3': 0.0,
            '4': 0.0,
            '5': 0.0,
            '6': 0.0,
            '7': 0.0,
            '8': 0.0,
            '9': 0.0,
            '10': 0.0,
            '11': 0.0,
            '12': 0.0,
            '13': 0.0,
            '14': 0.0,
            '15': 2.0,
            '16': 0.0,
            '17': 0.0,
            '18': 0.0,
            '19': 0.0
        }

        self.assertDictEqual(initial_service_dict, g.initial_service,
            msg=" Wrong INITIAL SERVICE in input ")

    def test_initial_sources(self):
        """
        Unittest check for sources of GeneralGraph: correct input reading.
        """
        g = GeneralGraph()
        g.load("tests/TOY_graph.csv")

        self.assertEqual(['1', '15'], g.sources, msg=" Wrong SOURCES in input ")

    def test_initial_hubs(self):
        """
        Unittest check for hubs of GeneralGraph: correct input reading.
        """
        g = GeneralGraph()
        g.load("tests/TOY_graph.csv")

        self.assertEqual(['4', '5', '6', '7', '8', '9', '16', '17', '10', '11',
            '19', '12', '14', '13'], g.hubs, msg=" Wrong HUBS in input ")

    def test_initial_users(self):
        """
        Unittest check for users of GeneralGraph: correct input reading.
        """
        g = GeneralGraph()
        g.load("tests/TOY_graph.csv")

        self.assertEqual(['18'], g.users, msg=" Wrong USERS in input ")

    def test_initial_switches(self):
        """
        Unittest check for switches of GeneralGraph: correct input reading.
        """
        g = GeneralGraph()
        g.load("tests/TOY_graph.csv")

        self.assertEqual(['2', '3'], g.switches,
            msg=" Wrong SWITCHES in input ")
