import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench('How are you?'), 'Comment es-tu?')  
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')  
        self.assertEqual(englishToFrench(''), '')  
        

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish('Comment es-tu?'), 'How are you?') 
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertEqual(frenchToEnglish(''), '')  
        
unittest.main()