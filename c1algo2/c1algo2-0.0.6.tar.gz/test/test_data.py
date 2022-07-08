import unittest
from c1algo2 import data

class TestData(unittest.TestCase):

    empty_input_data = []
    empty_progression_data = []

    minimal_input_data = [
        {
            "term": "201601",
            "subject": "CSC",
            "courseNumber": "110",
            "sequenceNumber": "A01",
            "maximumEnrolment": 400,
            "enrolment": 250
        }
    ]
    minimal_progression_data = {
        "1": 0,
        "2": 0,
        "2T": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0
    }

    def test_parse_input_empty(self):
        output = data.parse_input(
            self.empty_input_data,
            self.empty_progression_data
        )
        self.assertEqual(output, {})
    
    def test_parse_input_minimal(self):
        output = data.parse_input(
            self.minimal_input_data,
            self.minimal_progression_data
        )