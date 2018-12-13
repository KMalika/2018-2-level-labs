"""
Labour work #4
TfIdfCalculator class calculate function tests
"""

import unittest

import math

from lab_4.main import TfIdfCalculator


class CalculateTfIdfTest(unittest.TestCase):
    '''Checks calculating tf-idf of a given texts'''

    def test_check_calculate_tf_idf_ideal(self):
        """check tf_idf calculation ideal case"""
        clean_texts = []
        tf_instance = TfIdfCalculator(clean_texts)
        tf_instance.tf_values = [
            {
                'this': 1 / 11,
                'is': 1 / 11,
                'an': 1 / 11,
                'example': 1 / 11,
                'of': 1 / 11,
                'test': 1 / 11,
                'text': 2 / 11,
                'contains': 1 / 11,
                'two': 1 / 11,
                'sentences': 1 / 11
            },
            {
                'this': 1 / 12,
                'is': 3 / 12,
                'test': 1 / 12,
                'text': 3 / 12,
                'written': 1 / 12,
                'on': 1 / 12,
                'english': 1 / 12,
                'simple': 1 / 12
            },
            {
                'there': 1 / 5,
                'is': 1 / 5,
                'no': 1 / 5,
                'much': 1 / 5,
                'sense': 1 / 5
            }
        ]
        tf_instance.idf_values = {
            'this': math.log(3 / 2),
            'is': math.log(3 / 3),
            'an': math.log(3 / 1),
            'example': math.log(3 / 1),
            'of': math.log(3 / 1),
            'test': math.log(3 / 2),
            'text': math.log(3 / 2),
            'contains': math.log(3 / 1),
            'two': math.log(3 / 1),
            'sentences': math.log(3 / 1),
            'written': math.log(3 / 1),
            'on': math.log(3 / 1),
            'english': math.log(3 / 1),
            'simple': math.log(3 / 1),
            'third': math.log(3 / 1),
            'one': math.log(3 / 1),
            'there': math.log(3 / 1),
            'no': math.log(3 / 1),
            'much': math.log(3 / 1),
            'sense': math.log(3 / 1),
        }
        expected_res = [
            {
                'this': (1 / 11) * math.log(3 / 2),
                'is': (1 / 11) * math.log(3 / 3),
                'an': (1 / 11) * math.log(3 / 1),
                'example': (1 / 11) * math.log(3 / 1),
                'of': (1 / 11) * math.log(3 / 1),
                'test': (1 / 11) * math.log(3 / 2),
                'text': (2 / 11) * math.log(3 / 2),
                'contains': (1 / 11) * math.log(3 / 1),
                'two': (1 / 11) * math.log(3 / 1),
                'sentences': (1 / 11) * math.log(3 / 1)
            },
            {
                'this': 1 / 12 * math.log(3 / 2),
                'is': 3 / 12 * math.log(3 / 3),
                'test': 1 / 12 * math.log(3 / 2),
                'text': 3 / 12 * math.log(3 / 2),
                'written': 1 / 12 * math.log(3 / 1),
                'on': 1 / 12 * math.log(3 / 1),
                'english': 1 / 12 * math.log(3 / 1),
                'simple': 1 / 12 * math.log(3 / 1)
            },
            {
                'there': 1 / 5 * math.log(3 / 1),
                'is': 1 / 5 * math.log(3 / 3),
                'no': 1 / 5 * math.log(3 / 1),
                'much': 1 / 5 * math.log(3 / 1),
                'sense': 1 / 5 * math.log(3 / 1)
            }
        ]

        tf_instance.calculate()
        self.assertCountEqual(tf_instance.tf_idf_values, expected_res)

    def test_check_calculate_tf_idf_no_tf(self):
        """check tf_idf calculation no tf"""
        clean_texts = []
        tf_instance = TfIdfCalculator(clean_texts)
        tf_instance.tf_values = [

        ]
        tf_instance.idf_values = {
            'this': math.log(3 / 2),
            'is': math.log(3 / 3),
            'an': math.log(3 / 1),
            'example': math.log(3 / 1),
            'of': math.log(3 / 1),
            'test': math.log(3 / 2),
            'text': math.log(3 / 2),
            'contains': math.log(3 / 1),
            'two': math.log(3 / 1),
            'sentences': math.log(3 / 1),
            'written': math.log(3 / 1),
            'on': math.log(3 / 1),
            'english': math.log(3 / 1),
            'simple': math.log(3 / 1),
            'third': math.log(3 / 1),
            'one': math.log(3 / 1),
            'there': math.log(3 / 1),
            'no': math.log(3 / 1),
            'much': math.log(3 / 1),
            'sense': math.log(3 / 1),
        }
        expected_res = []

        tf_instance.calculate()
        self.assertCountEqual(tf_instance.tf_idf_values, expected_res)

    def test_check_calculate_tf_idf_no_idf(self):
        """check tf_idf calculation no idf"""
        clean_texts = []
        tf_instance = TfIdfCalculator(clean_texts)
        tf_instance.tf_values = [
            {
                'this': 1 / 11,
                'is': 1 / 11,
                'an': 1 / 11,
                'example': 1 / 11,
                'of': 1 / 11,
                'test': 1 / 11,
                'text': 2 / 11,
                'contains': 1 / 11,
                'two': 1 / 11,
                'sentences': 1 / 11
            },
            {
                'this': 1 / 12,
                'is': 3 / 12,
                'test': 1 / 12,
                'text': 3 / 12,
                'written': 1 / 12,
                'on': 1 / 12,
                'english': 1 / 12,
                'simple': 1 / 12
            },
            {
                'there': 1 / 5,
                'is': 1 / 5,
                'no': 1 / 5,
                'much': 1 / 5,
                'sense': 1 / 5
            }
        ]
        tf_instance.idf_values = {}
        expected_res = []

        tf_instance.calculate()
        self.assertCountEqual(tf_instance.tf_idf_values, expected_res)

    def test_check_calculate_tf_idf_no_idf_no_tf(self):
        """check tf_idf calculation no idf and tf"""
        clean_texts = []
        tf_instance = TfIdfCalculator(clean_texts)
        tf_instance.tf_values = []
        tf_instance.idf_values = {}
        expected_res = []

        tf_instance.calculate()
        self.assertCountEqual(tf_instance.tf_idf_values, expected_res)

    def test_check_calculate_tf_idf_none_idf(self):
        """check tf_idf calculation none idf"""
        clean_texts = []
        tf_instance = TfIdfCalculator(clean_texts)
        tf_instance.idf_values = None
        expected_res = []

        tf_instance.calculate()
        self.assertCountEqual(tf_instance.tf_idf_values, expected_res)

    def test_check_calculate_tf_idf_none_tf(self):
        """check tf_idf calculation none tf_none"""
        clean_texts = []
        tf_instance = TfIdfCalculator(clean_texts)
        tf_instance.tf_values = None
        expected_res = []

        tf_instance.calculate()
        self.assertCountEqual(tf_instance.tf_idf_values, expected_res)

    def test_check_calculate_tf_idf_none_both(self):
        """check tf_idf calculation none both none"""
        clean_texts = []
        tf_instance = TfIdfCalculator(clean_texts)
        tf_instance.tf_values = None
        tf_instance.idf_values = None
        expected_res = []

        tf_instance.calculate()
        self.assertCountEqual(tf_instance.tf_idf_values, expected_res)
