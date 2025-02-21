# 18.10.2025
# vohidov
# DUNDER METODLAR

# class Avto:
#     __num_avto = 0
#     """Avtomobil klassi"""
#     def __init__(self,make,model,rang,yil,narh):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         Avto.__num_avto += 1

#     def __repr__(self):
#         return f"Avto: {self.rang} {self.make} {self.model}"

#     def __eq__(self,boshqa_avto):
#         return self.narh == boshqa_avto.narh

#     def __lt__(self,boshqa_avto):
#         return self.narh<boshqa_avto.narh

#     def __le__(self,boshqa_avto):
#         return self.narh <= boshqa_avto.narh
    
# # # avto1 = Avto("GM","Malibu","Qora",2020,40000)
# # # print(avto1) # obyekt haqida ma'lumot

# # # x,y = 5,10
# # # print(x>y)

# # avto1 = Avto("GM","Malibu","Qora",2020,40000)
# # avto2 = Avto("GM","Lacetti","Oq",2020,40000)
# # print(avto1==avto2)

# class AvtoSalon:
#     """Avtosalon klassi"""
#     def __init__(self,name):
#         self.name = name
#         self.avtolar = []

#     def __repr__(self):
#         return f"{self.name} avtosaloni"
    
#     def __len__(self):
#         return len(self.avtolar)

#     def __getitem__(self,index):
#         return self.avtolar[index]

#     def __setitem__(self,index,value):
#         if isinstance(value,Avto):
#             self.avtolar[index]=value
    
#     def add_avto(self,*qiymat):
#         for avto in qiymat:
#             if isinstance(avto,Avto):
#                 self.avtolar.append(avto)
#             elif isinstance(qiymat.Avto):
#                 self.add_avto(qiymat)
#             else:
#                 print(f"AvtoSalon ga {type(qiymat)} qo'shib bo'lmaydi")
    
#     def __add__(self,qiymat):
#         if isinstance(qiymat,AvtoSalon):
#             yangi_salon = AvtoSalon(f"{self.name}  {qiymat.name}")
#             yangi_salon.avtolar = self.avtolar + qiymat.avtolar
#             return yangi_salon
    
#     def __call__(self, *param):
#         if param:
#             for avto in  param:
#                 self.add_avto(avto)
#         else:
#             return [avto for avto in self.avtolar]

# salon1 = AvtoSalon("MaxAvto")
# salon2 = AvtoSalon("Avto Lider")

# avto1 = Avto("GM","Malibu","Qora",2020,40000)
# avto2 = Avto("GM","Lacetti","Oq",2020,20000)
# avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
# avto4 = Avto("Mazda", "6", 'Qizil',2015,35000)
# avto5 = Avto("Volkswagen","Polo",'Qora',2015,30000)
# avto6 = Avto("Honda","Accord","Oq",2017,42000)

# salon1.add_avto(avto1, avto2, avto3)
# salon2.add_avto(avto4, avto5, avto6)

# salon3 = salon1 + salon2
# # print(salon3)
# # print(salon3[:])

# avto7 = Avto("BMW", 'X7','Qora',2015,75000)
# salon1 + avto7
# print(salon1())

# avto_new = Avto("Mercedes-Benz", 'E200','Silver',2015,80000)
# salon1(avto_new) # Yangi avto qo'shamiz
# salon1() # salondagi mashinalarni ko'ramiz

# amaliyot
# (21.02.2025)

# class Shaxs:
#     def __init__(self, ism, familiya, tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil

#     def get_info(self):
#         return f"{self.ism} {self.familiya} {self.tyil}-yilda tug'ilgan."
        
#     def get_age(self, yil):
#         return yil - self.tyil
    
#     def __str__(self):
#         return f"{self.ism} {self.familiya} {self.tyil}"
    
#     def __repr__(self):
#         return f"Shaxs('{self.ism}', '{self.familiya}', {self.tyil})"
    
#     def __eq__(self, other):
#         return (self.ism, self.familiya, self.tyil) == (other.ism, other.familiya, other.tyil)


# class Manzil:
#     def __init__(self, uy, kocha, tuman, viloyat):
#         self.uy = uy
#         self.kocha = kocha
#         self.tuman = tuman
#         self.viloyat = viloyat

#     def get_manzil(self):
#         return f"{self.viloyat} viloyati, {self.tuman} tumani, {self.kocha} ko'chasi, {self.uy}-uy "
    
#     def __str__(self):
#         return self.get_manzil()
    
#     def __repr__(self):
#         return f"Manzil({self.uy}), '{self.kocha}', '{self.tuman}', '{self.viloyat}' "
        
       


# class Talaba(Shaxs):
#     def __init__(self, ism, familiya, tyil, manzil, bosqich, idraqam):
#         super().__init__(ism, familiya, tyil)
#         self.idraqam = idraqam
#         self.bosqich = bosqich  # 1 bo'lmasligi kerak
#         self.manzil = manzil
#         self.fanlar = []  # Fanlar ro'yxati bo'sh boshlanadi
    
#     def get_info(self):
#         return f"{self.ism} {self.familiya}, {self.bosqich}-bosqich. ID: {self.idraqam}"

#     def __str__(self):
#         return f"Talaba: {self.ism} {self.familiya}, {self.bosqich}-bosqich"

#     def __repr__(self):
#         return f"Talaba('{self.ism}', '{self.familiya}', {self.tyil}, {self.bosqich}, '{self.idraqam}')"

#     def __eq__(self, other):
#         return self.idraqam == other.idraqam  # Talabalarni ID orqali solishtiramiz
        
        
# # Obyektlar yaratamiz
# # shaxs1 = Shaxs("Ali", "Valiyev", 1995)
# # shaxs2 = Shaxs("Ali", "Valiyev", 1995)
# # manzil1 = Manzil(23, "Bog‘bon", "Yunusobod", "Toshkent")
# # talaba1 = Talaba("Hasan", "Aliyev", 2003, manzil1, 2, "T123456")
# # talaba2 = Talaba("Hasan", "Aliyev", 2003, manzil1, 2, "T123457")

# # __str__ va __repr__ ishlashini tekshiramiz
# # print(shaxs1)  # Ali Valiyev (1995)
# # print(repr(shaxs1))  # Shaxs('Ali', 'Valiyev', 1995)

# # print(talaba1)  # Talaba: Hasan Aliyev, 2-bosqich
# # print(repr(talaba1))  # Talaba('Hasan', 'Aliyev', 2003, 2, 'T123456')

# # print(manzil1)  # Toshkent viloyati, Yunusobod tumani, Bog‘bon ko‘chasi, 23-uy
# # print(repr(manzil1))  # Manzil(23, 'Bog‘bon', 'Yunusobod', 'Toshkent')

# # # __eq__ (==) metodini tekshiramiz
# # print(shaxs1 == shaxs2)  # True (bir xil ism, familiya va tug'ilgan yil)
# # print(talaba1 == talaba2)  # False (ID lar har xil)

# # # __lt__, __le__ metodlarini qo'shish mumkin, masalan, yoshi bo'yicha solishtirish uchun
# # print(shaxs1.get_age(2025))  # 30 yosh

# class Fan:
#     def __init__(self,nomi):
#         self.nomi = nomi
#         self.talabalar = []
    
#     def add_student(self, talaba):
#         """Fanga talaba qo'shish"""
#         if isinstance(talaba, Talaba):
#             self.talabalar.append(talaba)
#         else:
#             raise ValueError("Faqat Talaba obyektlarini qo'shish mumkin!")

#     def remove_student(self,idraqam):
#         """Talabani ID raqam orqali olib tashlash"""
#         for talaba in self.talabalar:
#             if talaba.idraqam == idraqam:
#                 self.talabalar.remove(talaba)
#                 return True
#         return False # agar talab topilmasa hechnarsa o'chirilmaydi
    
#     def __add__(self,talaba):
#         """+ operatori yordamifa talaba qo'shish"""
#         self.add_student(talaba)
#         return self # Obyekt qaytarish

#     def __sub__(self,idraqam):
#         """- operatori yordamida talabani ID raqam bo'yicha o'chirish"""
#         self.remove_student(idraqam) 
#         return self 

#     def __call__(self, talaba=None):
#         """Obyektni chaqiriladigan qilish:
#         - Agar argument berilmasa -> barcha talabalarni qaytaradi
#         - Agar argument berilsa -> talabani qo'shadi"""
#         if talaba is None:
#             return [str(t) for t in self.talabalar]  # Barcha talabalarni qaytarish
#         else:
#             self.add_student(talaba)  # Talabani qo'shish

#         def __getitem__(self,index):
#             """Index orqali talaba olish"""
#             return self.talabalar[index]
    
#     def __setitem__(self,index,talaba):
#         """Index orqali talaba almashtirish"""
#         if isinstance(talaba,Talaba):
#             self.talabalar[index] = talaba
#         else:
#             raise ValueError("Faqat Talaba obyektlarini qo'shish mumkin!")

#     def __repr__(self):
#         return f"Fan('{self.nomi}')"   
    
#     def __len__(self):
#         """Fan talabalarining umumiy sonini qaytarish"""
#         return len(self.talabalar)  
    
#     def __str__(self):
#         return f"{self.nomi} fanida {len(self)} ta talaba bor."

     
#  # Manzil obyektini yaratamiz
# manzil1 = Manzil(23, "Bog‘bon", "Yunusobod", "Toshkent")

# # Shaxs obyektlarini yaratamiz
# shaxs1 = Shaxs("Ali", "Valiyev", 1995)
# shaxs2 = Shaxs("Ali", "Valiyev", 1995)

# # Talaba obyektlarini yaratamiz
# talaba1 = Talaba("Hasan", "Aliyev", 2003, manzil1, 2, "T123456")
# talaba2 = Talaba("Hasan", "Aliyev", 2003, manzil1, 2, "T123457")

# # Shaxslar haqida ma'lumot
# print(shaxs1)  # Ali Valiyev 1995
# print(repr(shaxs1))  # Shaxs('Ali', 'Valiyev', 1995)

# # Talaba haqida ma'lumot
# print(talaba1)  # Talaba: Hasan Aliyev, 2-bosqich
# print(repr(talaba1))  # Talaba('Hasan', 'Aliyev', 2003, 2, 'T123456')

# # Manzilni chiqarish
# print(manzil1)  # Toshkent viloyati, Yunusobod tumani, Bog‘bon ko‘chasi, 23-uy
# print(repr(manzil1))  # Manzil(23, 'Bog‘bon', 'Yunusobod', 'Toshkent')

# # Shaxslar tengligini tekshiramiz
# print(shaxs1 == shaxs2)  # True (bir xil ism, familiya va tug'ilgan yil)

# # Talabalar tengligini tekshiramiz
# print(talaba1 == talaba2)  # False (ID lar har xil)

# # Shaxsning yoshini hisoblash
# print(shaxs1.get_age(2025))  # 30 yosh

# # Fan obyektini yaratamiz
# fan1 = Fan("Matematika")

# # Talabalarni fanga qo'shish
# fan1 + talaba1
# fan1 + talaba2

# # Fandagi talabalarni tekshiramiz
# print(fan1)  # Matematika fanida 2 ta talaba bor.
# print(fan1())  # ['Talaba: Hasan Aliyev, 2-bosqich', 'Talaba: Hasan Aliyev, 2-bosqich']

# # Talabani ID orqali o'chirish
# fan1 - "T123456"

# # Fandagi talabalarni yana tekshiramiz
# print(fan1)  # Matematika fanida 1 ta talaba bor.
