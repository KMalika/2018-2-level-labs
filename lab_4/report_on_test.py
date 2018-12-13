"""
Labour work #4
TfIdfCalculator class report_on function tests
"""

import unittest

import math

from lab_4.main import TfIdfCalculator


class ReportOnTest(unittest.TestCase):
    """Checks report on"""

    def test_report_on_ideal_case(self):
        """Check report_on ideal case"""
        clean_texts = [
            ['this', 'is', 'an', 'example', 'of', 'test', 'text', 'it', 'contains', 'two', 'sentences'],
            ['das', 'ist', 'ein', 'testtext', 'es', 'ist', 'auf', 'deutsch', 'geschrieben']
        ]
        tf_instance = TfIdfCalculator(clean_texts)
        tf_instance.tf_idf_values = [
            {
                'this': 10,
                'that': 9,
                'another': 5
            }
        ]

        tf_instance.calculate()

        res = tf_instance.report_on('this', 0)
        exp_res = (10, 0)
        self.assertEqual(res, exp_res)

    def test_report_on_index_bigger(self):
        """Check report_on invalid doc index"""
        clean_texts = [
            ['this', 'is', 'an', 'example', 'of', 'test', 'text', 'it', 'contains', 'two', 'sentences'],
            ['das', 'ist', 'ein', 'testtext', 'es', 'ist', 'auf', 'deutsch', 'geschrieben']
        ]
        tf_instance = TfIdfCalculator(clean_texts)
        tf_instance.tf_idf_values = [
            {
                'this': 10,
                'that': 9,
                'another': 5
            }
        ]

        tf_instance.calculate()

        res = tf_instance.report_on('this', 2)
        exp_res = ()
        self.assertEqual(res, exp_res)

    def test_report_on_empty_tf_idf(self):
        """Check report_on empty tf_idf"""
        clean_texts = [
            ['this', 'is', 'an', 'example', 'of', 'test', 'text', 'it', 'contains', 'two', 'sentences'],
            ['das', 'ist', 'ein', 'testtext', 'es', 'ist', 'auf', 'deutsch', 'geschrieben']
        ]
        tf_instance = TfIdfCalculator(clean_texts)
        tf_instance.tf_idf_values = []

        tf_instance.calculate()

        res = tf_instance.report_on('this', 0)
        exp_res = ()
        self.assertEqual(res, exp_res)

    def test_report_on_none_tf_idf(self):
        """Check report_on none tf_idf"""
        clean_texts = [
            ['this', 'is', 'an', 'example', 'of', 'test', 'text', 'it', 'contains', 'two', 'sentences'],
            ['das', 'ist', 'ein', 'testtext', 'es', 'ist', 'auf', 'deutsch', 'geschrieben']
        ]
        tf_instance = TfIdfCalculator(clean_texts)
        tf_instance.tf_idf_values = None

        tf_instance.calculate()

        res = tf_instance.report_on('this', 0)
        exp_res = ()
        self.assertEqual(res, exp_res)

    def test_report_on_word_not_in_tfidf(self):
        """Check report_on none tf_idf"""
        clean_texts = [
            ['this', 'is', 'an', 'example', 'of', 'test', 'text', 'it', 'contains', 'two', 'sentences'],
            ['das', 'ist', 'ein', 'testtext', 'es', 'ist', 'auf', 'deutsch', 'geschrieben']
        ]
        tf_instance = TfIdfCalculator(clean_texts)
        tf_instance.tf_idf_values = None

        tf_instance.calculate()

        res = tf_instance.report_on('wtf', 0)
        exp_res = ()
        self.assertEqual(res, exp_res)