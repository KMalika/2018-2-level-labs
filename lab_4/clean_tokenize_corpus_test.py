"""
Labour work #4
CleanTokenizeCorpus tests
"""

import unittest

from lab_4.main import clean_tokenize_corpus


class CleanTokenizeCorpusTest(unittest.TestCase):
    """Checks cleaning and tokenizing texts"""

    def test_clean_tokenize_corpus_ideal(self):
        """ideal case for clean_tokenize_corpus function"""
        texts = [
            'This is an example of test text. It contains two sentences.',
            'Das ist ein Testtext. Es ist auf deutsch geschrieben.'
        ]
        res_texts = clean_tokenize_corpus(texts)
        exp_res = [
            ['this', 'is', 'an', 'example', 'of', 'test', 'text', 'it', 'contains', 'two', 'sentences'],
            ['das', 'ist', 'ein', 'testtext', 'es', 'ist', 'auf', 'deutsch', 'geschrieben']
        ]
        self.assertEqual(res_texts, exp_res)

    def test_clean_tokenize_corpus_punctuation(self):
        """Text contains punctuation marks"""
        texts = [
            'This, is an example of test - text. It contains two: sentences.',
            'Das ist ein Testtext. Es ist auf deutsch geschrieben.'
        ]
        res_texts = clean_tokenize_corpus(texts)
        exp_res = [
            ['this', 'is', 'an', 'example', 'of', 'test', 'text', 'it', 'contains', 'two', 'sentences'],
            ['das', 'ist', 'ein', 'testtext', 'es', 'ist', 'auf', 'deutsch', 'geschrieben']
        ]
        self.assertEqual(res_texts, exp_res)

    def test_clean_tokenize_corpus_dirty(self):
        """Text is dirty"""
        texts = [
            'This* is an@ example>< of test - text! It cont&*ains two: sen#!tences.',
            'Das is()t ein Test^text. Es ist auf deu-tsch geschr=ieben.'
        ]
        res_texts = clean_tokenize_corpus(texts)
        exp_res = [
            ['this', 'is', 'an', 'example', 'of', 'test', 'text', 'it', 'contains', 'two', 'sentences'],
            ['das', 'ist', 'ein', 'testtext', 'es', 'ist', 'auf', 'deutsch', 'geschrieben']
        ]
        self.assertEqual(res_texts, exp_res)

    def test_clean_tokenize_corpus_line_breaks(self):
        """Text with linebreaks"""
        texts = [
            'This is an example of test text!<br /><br />It contains two sentences.',
            'Das ist ein Testtext.<br /><br />Es ist auf deutsch geschrieben.'
        ]
        res_texts = clean_tokenize_corpus(texts)
        exp_res = [
            ['this', 'is', 'an', 'example', 'of', 'test', 'text', 'it', 'contains', 'two', 'sentences'],
            ['das', 'ist', 'ein', 'testtext', 'es', 'ist', 'auf', 'deutsch', 'geschrieben']
        ]
        self.assertEqual(res_texts, exp_res)

    def test_clean_tokenize_corpus_one_none(self):
        """One of texts is none"""
        texts = [
            None,
            'Das ist ein Testtext.<br /><br />Es ist auf deutsch geschrieben.'
        ]
        res_texts = clean_tokenize_corpus(texts)
        exp_res = [
            ['das', 'ist', 'ein', 'testtext', 'es', 'ist', 'auf', 'deutsch', 'geschrieben']
        ]
        self.assertEqual(res_texts, exp_res)

    def test_clean_tokenize_corpus_all_none(self):
        """Both of texts is none"""
        texts = [
            None,
            None
        ]
        res_texts = clean_tokenize_corpus(texts)
        exp_res = [
        ]
        self.assertEqual(res_texts, exp_res)

    def test_clean_tokenize_corpus_all_not_str(self):
        """Both of texts is none"""
        texts = [
            123,
            [1, 2, 3]
        ]
        res_texts = clean_tokenize_corpus(texts)
        exp_res = [
        ]
        self.assertEqual(res_texts, exp_res)

    def test_clean_tokenize_corpus_one_not_str(self):
        """Both of texts is none"""
        texts = [
            'This is an example of test text. It contains two sentences.',
            [1, 2, 3]
        ]
        res_texts = clean_tokenize_corpus(texts)
        exp_res = [
            ['this', 'is', 'an', 'example', 'of', 'test', 'text', 'it', 'contains', 'two', 'sentences'],
        ]
        self.assertEqual(res_texts, exp_res)

    def test_clean_tokenize_corpus_texts_none(self):
        """Both of texts is none"""
        texts = None
        res_texts = clean_tokenize_corpus(texts)
        exp_res = []
        self.assertEqual(res_texts, exp_res)
