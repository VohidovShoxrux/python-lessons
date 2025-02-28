import unittest
from tubSonmi import tubSonmi

class tubSonmiTest(unittest.TestCase):
    def test_ture(self):
        self.assertTure(tubSonmi(7))
        self.assertTrue(tubSonmi(193))
        self.assertTrue(tubSonmi(547))
    
    def test_false(self):
        self.assertFalse(tubSonmi(6))
        self.assertFalse(tubSonmi(265))
        self.assertFalse(tubSonmi(489))
    
unittest.main()