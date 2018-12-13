"""
Labour work #4
TfIdfCalculator class calculate_idf function tests
"""

import unittest

import math

from lab_4.main import TfIdfCalculator


class CalculateIdfTest(unittest.TestCase):
    """Checks calculating idf of a given texts"""

    def test_check_calculate_idf_ideal(self):
        """check idf calculation ideal case"""
        clean_texts = [
            ['this', 'is', 'an', 'example', 'of', 'test', 'text', 'text', 'contains', 'two', 'sentences'],
            ['this', 'is', 'test', 'text', 'text', 'is', 'written', 'on', 'english', 'text', 'is', 'simple'],
            ['third', 'one', 'there', 'is', 'no', 'much', 'sense']
        ]
        tf_instance = TfIdfCalculator(clean_texts)
        tf_instance.calculate_idf()
        expected_res = {
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

        self.assertEqual(tf_instance.idf_values, expected_res)

    def test_check_calculate_one_none(self):
        """check idf calculation one text is none case"""
        clean_texts = [
            None,
            ['this', 'is', 'test', 'text', 'text', 'is', 'written', 'on', 'english', 'text', 'is', 'simple']
        ]
        tf_instance = TfIdfCalculator(clean_texts)
        tf_instance.calculate_idf()
        expected_res = {
            'this': math.log(1 / 1),
            'is': math.log(1 / 1),
            'test': math.log(1 / 1),
            'text': math.log(1 / 1),
            'written': math.log(1 / 1),
            'on': math.log(1 / 1),
            'english': math.log(1 / 1),
            'simple': math.log(1 / 1)
        }
        self.assertEqual(tf_instance.idf_values, expected_res)

    def test_check_calculate_all_none(self):
        """check idf calculation all texts are none case"""
        clean_texts = [
            None,
            None
        ]
        tf_instance = TfIdfCalculator(clean_texts)
        tf_instance.calculate_idf()
        expected_res = {}
        self.assertEqual(tf_instance.idf_values, expected_res)

    def test_check_calculate_texts_none(self):
        """check idf calculation all texts are none case"""
        clean_texts = None
        tf_instance = TfIdfCalculator(clean_texts)
        tf_instance.calculate_idf()
        expected_res = {}
        self.assertCountEqual(tf_instance.idf_values, expected_res)

    def test_check_calculate_idf_elements_not_str(self):
        """check idf calculation with non str elements"""
        clean_texts = [
            ['this', 'is', 'an', 'example', 'of', 'test', 'text', 'text', 'contains', 'two', 'sentences', 123, (),
             [1, 2, 3], 2 * 4],
            ['this', 'is', 'test', 'text', 'text', 'is', 'written', 'on', 'english', 123, 'text', 'is', 'simple'],
            ['third', 'one', 'there', 'is', 'no', 'much', 'sense']
        ]
        tf_instance = TfIdfCalculator(clean_texts)
        tf_instance.calculate_idf()
        expected_res = {
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
