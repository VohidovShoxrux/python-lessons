import unittest
from name import get_full_name

class NameTest(unittest.TestCase):
    def test_toliq_ism(self):
        formatted_name = get_full_name('shoxrux','vohidov')
        self.assertEqual(formatted_name,'Shoxrux Vohidov')

    def test_toliq_ism_otasi(self):
        name = get_full_name('shoxrux','vohidov','ravshanbekov')
        self.assertEqual(name,'Shoxrux Ravshanbekov Vohidov')
    
unittest.main()