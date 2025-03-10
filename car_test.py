import unittest
from python_36dars import Car

class CarTest(unittest.TestCase):
    """Car klassini tekshirish uchun test"""

    def setUp(self):
        make = "GM"
        model = "Maluba"
        year = 2025
        self.price = 40000
        self.km = 10000
        self.avto1 = Car(make,model,year)
        self.avto2 = Car(make,model,year,price=self.price)

    def test_create(self):
        # avto1 obyektini km va narhini bermasdan yaratamiz
        # avto1 = Car("gm","maluba",2025)
        # Qiymatlar mavjudligini assertIsNotNone metodi bilan tekshiramiz
        self.assertIsNotNone(self.avto1.make)
        self.assertIsNotNone(self.avto1.model)
        self.assertIsNotNone(self.avto1.year)
        # Qiymat mavjud emasligini assertIsNone metodi bilan tekshiramiz
        self.assertIsNone(self.avto1.price)
        # Qiymat tengligini assertEquals metodi bilan tekshiramiz
        self.assertEqual(0,self.avto1.get_km())
        # Yangi obyekt yaratamiz va narhini ham ko'rsatamiz
        # avto2 = Car("gm","onix",2023,price=23000)
        # self.assertEqual(23000,avto2.price)
        self.assertEqual(self.price,self.avto2.price)

    def test_set_price(self):
        self.avto2.set_price(self.price)
        self.assertEqual(self.price,self.avto2.price)
    
    def test_add_km(self):
        #1 musbat qiymat berib koramiz
        self.avto1.add_km(self.km)
        self.assertEqual(self.km,self.avto1.get_km())
        #2 manfiy qiymat berib koramiz
        new_km = -5000
        try:
            self.avto1.add_km(new_km)
        except ValueError as error:
            self.assertEqual(type(error),ValueError)

    def test_get_info(self):
        avto1_info = 'GM Maluba, 2025-yil, 0km yurgan. '
        self.assertEqual(avto1_info, self.avto1.get_info())
        # avto1 narhi va km o'zgartiramiz
        self.avto1.set_price(162718)
        self.avto1.add_km(250000)
        avto1_info = 'GM Maluba, 2025-yil, 250000km yurgan. Narhi: 162718'
        self.assertEqual(avto1_info,self.avto1.get_info())

unittest.main()
