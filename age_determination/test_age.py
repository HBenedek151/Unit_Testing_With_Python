import unittest
from age import categorise_by_age

class TestCategorizeByAge(unittest.TestCase):
    def test_child(self):
        self.assertEqual(categorise_by_age(5), "baba")
        self.assertEqual(categorise_by_age(7), "baba")

    def test_child(self):
        self.assertEqual(categorise_by_age(9), "baba")
        self.assertEqual(categorise_by_age(10), "gyerek")

    def test_child(self):
        self.assertEqual(categorise_by_age(18), "gyerek")
        self.assertEqual(categorise_by_age(19), "felnőtt")

    def test_child(self):
        self.assertEqual(categorise_by_age(65), "felnőtt")
        self.assertEqual(categorise_by_age(66), "idős")

    def test_child(self):
        self.assertEqual(categorise_by_age(-1), "hibás adat")
        self.assertEqual(categorise_by_age(130), "halott")