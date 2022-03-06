""" this modules tests the functionality of language translation methods """
import unittest

from machinetranslation.translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    """ this class contains method to test the english to french translation functionality """
    def test1(self):
        """ this methods contains the unit test case for english to french translation """
        self.assertEqual(englishToFrench("hello"),"Bonjour")
        self.assertNotEqual(englishToFrench("hello"),"xyz")
        self.assertIsNotNone(englishToFrench("Hello"))

class TestFrenchToEnglish(unittest.TestCase):
    """ this class contains method to test the french to english translation functionality """
    def test1(self):
        """ this methods contains the unit test case for french to english translation """
        self.assertEqual(frenchToEnglish("bonjour"),"Hello")
        self.assertNotEqual(frenchToEnglish("bonjour"),"xyz")
        self.assertIsNotNone(frenchToEnglish("Bonjour"))

unittest.main()
