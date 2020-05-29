import unittest

from .Are You Playing Banjo import areYouPlayingBanjo

class DNAToRNATestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(areYouPlayingBanjo("Adam"), "Adam does not play banjo")
        
    def test_equals_2(self):
        self.assertEqual(areYouPlayingBanjo("Paul"), "Paul does not play banjo")    
        
    def test_equals_3(self):
        self.assertEqual(areYouPlayingBanjo("Ringo"), "Ringo plays banjo") 
        
    def test_equals_4(self):
        self.assertEqual(areYouPlayingBanjo("bravo"), "bravo does not play banjo") 
       
 
