import unittest

from .index import DNAtoRNA

class DNAToRNATestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(DNAtoRNA('TTTT'), 'UUUU')

    def test_equals_2(self):
        self.assertEqual(DNAtoRNA('GCAT'), 'GCAU')

    def test_equals_3(self):
        self.assertEqual(DNAtoRNA('GACCGCCGCC'), 'GACCGCCGCC')
