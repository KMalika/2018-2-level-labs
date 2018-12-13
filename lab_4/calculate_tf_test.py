"""
Labour work #4
TfIdfCalculator class calculate_tf function tests
"""

import unittest

from lab_4.main import TfIdfCalculator


class CalculateTfTest(unittest.TestCase):
    """Checks calculating tf of given texts"""

    def test_check_initialization(self):
        """check instance of TfIdfCalculator initialization"""
        clean_texts = [
            ['this', 'is', 'an', 'example', 'of', 'test', 'text', 'it', 'contains', 'two', 'sentences'],
            ['das', 'ist', 'ein', 'testtext', 'es', 'ist', 'auf', 'deutsch', 'geschrieben']
        ]
        tf_instance = TfIdfCalculator(clean_texts)
        self.assertEqual(tf_instance.corpus, clean_texts)
        self.assertEqual(tf_instance.tf_values, [])
        self.assertEqual(tf_instance.idf_values, {})
        self.assertEqual(tf_instance.tf_idf_values, [])

    def test_check_calculate_tf_ideal(self):
        """check tf calculation ideal case"""
        clean_texts = [
            ['this', 'is', 'an', 'example', 'of', 'test', 'text', 'text', 'contains', 'two', 'sentences'],
            ['this', 'is', 'test', 'text', 'text', 'is', 'written', 'on', 'english', 'text', 'is', 'simple']
        ]
        tf_instance = TfIdfCalculator(clean_texts)
        tf_instance.calculate_tf()
        expected_res = [
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
        ]
        self.assertCountEqual(tf_instance.tf_values, expected_res)

    def test_check_calculate_one_none(self):
        """check tf calculation one text is none case"""
        clean_texts = [
            None,
            ['this', 'is', 'test', 'text', 'text', 'is', 'written', 'on', 'english', 'text', 'is', 'simple']
        ]
        tf_instance = TfIdfCalculator(clean_texts)
        tf_instance.calculate_tf()
        expected_res = [
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
        ]
        self.assertCountEqual(tf_instance.tf_values, expected_res)

    def test_check_calculate_all_none(self):
        """check tf calculation all texts are none case"""
        clean_texts = [
            None,
            None
        ]
        tf_instance = TfIdfCalculator(clean_texts)
        tf_instance.calculate_tf()
        expected_res = []
        self.assertCountEqual(tf_instance.tf_values, expected_res)

    def test_check_calculate_texts_none(self):
        """check tf calculation all texts are none case"""
        clean_texts = None
        tf_instance = TfIdfCalculator(clean_texts)
        tf_instance.calculate_tf()
        expected_res = []
        self.assertCountEqual(tf_instance.tf_values, expected_res)

    def test_check_calculate_tf_elements_not_str(self):
        """check tf calculation with non str elements"""
        clean_texts = [
            ['this', 'is', 'an', 'example', 'of', 'test', 'text', 'text', 'contains', 'two', 'sentences', 123, (),
             [1, 2, 3], 2 * 4],
            ['this', 'is', 'test', 'text', 'text', 'is', 'written', 'on', 'english', 123, 'text', 'is', 'simple']
        ]
        tf_instance = TfIdfCalculator(clean_texts)
        tf_instance.calculate_tf()
        expected_res = [
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
        ]
        self.assertCountEqual(tf_instance.tf_values, expected_res)
