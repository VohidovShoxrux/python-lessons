import unittest
from python_36dars_amaliyoti import Shaxs, Manzil, Talaba

class TestShaxs(unittest.TestCase):
    def setUp(self):
        # Test uchun ob'ektlarni tayyorlash
        self.shaxs = Shaxs("Shoxrux","Vohidov","AD1234567", 2005)
        self.manzil = Manzil(120,'Ziyokor','Izboskan','Andijon')
        self.talaba = Talaba("Jonibek","Najimov","CD1234567",2000,'T12345',self.manzil)
    
    def test_shaxs_get_info(self):
        expected = "Shoxrux Vohidov Passporti:AD1234567, 2005-yilda tug'ilgan"
        self.assertEqual(self.shaxs.get_info(),expected)

    def test_shaxs_get_age(self):
        self.assertEqual(self.shaxs.get_age(2025),20)

    def test_manzil_get_manzil(self):
        expected = "Andijon viloyati, Izboskan tumani, Ziyokor ko'chasi, 120-uy"
        self.assertEqual(self.manzil.get_manzil(),expected)

    def test_talaba_get_id(self):
        self.assertEqual(self.talaba.get_id(),"T12345")

    def test_talaba_get_bosqich(self):
        self.assertEqual(self.talaba.get_bosqich(),1)
    
    def test_talaba_get_info(self):
        expected = "Jonibek Najimov 1-bosqich. ID raqam:T12345"
        self.assertEqual(self.talaba.get_info(),expected)

    
unittest.main()