import unittest
from uchson import uchson_katta
from matnlar import strings
from juftsonlar import juft_sonlar
from fibanachi import is_fibonacci

# class Son_Test(unittest.TestCase):
#     def test_son(self):
#         thing = uchson_katta(5,4,89)
#         self.assertAlmostEqual(thing,89)

# mevalar = ['olma','anor','anjir','nok','gilos']

# class Strings_Test(unittest.TestCase):
#     def test_string(self):
#         matnlar = strings(mevalar)
#         self.assertEqual(matnlar,['Olma', 'Anor', 'Anjir', 'Nok', 'Gilos'])

# class Juft_Sonlar_Test(unittest.TestCase):
#     def test_juftsonalr(self):
#         royxat = juft_sonlar(list(range(1,10)))
#         self.assertListEqual(royxat,[2,4,6,8])  

class Finbo_Test(unittest.TestCase):
    def test_fibo(self):
        self.assertTrue(is_fibonacci(7))

unittest.main()