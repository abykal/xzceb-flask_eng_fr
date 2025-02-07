import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')  
        self.assertEqual(englishToFrench(''), '')  
        self.assertNotEqual(englishToFrench('Bye'), 'Bonjour') 
        

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertEqual(frenchToEnglish(''), '')  
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Bye')
        
unittest.main()