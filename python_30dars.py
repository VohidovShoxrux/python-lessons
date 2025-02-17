# 17.02.2025
# vohidov
# INKAPSULYATSIA, KLASSNING XUSUSIYAT VA METODLARI

# from transport import Avto, Bus, PI
# # import transport # modulni to'liq import qilish bunda modul nomi. bilan sihlatilinadi
# # from transport import * # bunday qilish tafsiya qilinmaydi kop hollarda

# avto = Avto("GM","Malibu","Qora",2020,40000)

# amaliyot
# from uuid import uuid4
# class Shaxs:
#     __odamlar_soni = 0
#     def __init__(self,ism,familiya,tyil,passport):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.__passport = passport
#         Shaxs.__odamlar_soni +=1
        
#     @classmethod
#     def get_odamlar_soni(cls):
#         return cls.__odamlar_soni

#     def get_passport(self):
#         return self.__passport
    
#     def set_passport(self,new_passport):
#         self.__passport = new_passport

#     def get_info(self):
#         return f"Ism: {self.ism}, Familiya: {self.familiya}, Tug'ilgan yil: {self.tyil}, Passport: {self.__passport}"


# class Talaba(Shaxs):
#     __talabalar_soni = 0
#     def __init__(self,ism,familiya,passport,tyil,manzil):
#         super().__init__(ism,familiya,tyil,passport)
#         self.__id = uuid4()
#         self.manzil = manzil
#         Talaba.__talabalar_soni += 1

#     @classmethod 
#     def get_talabalar_soni(cls):
#         return cls.__talabalar_soni
    
#     def get_id(self):
#         return self.__id

#     def get_manzil(self):
#         return self.manzil

#     def set_manzil(self, new_manzil):
#         self.manzil = new_manzil


# # Misol uchun ob'ekt yaratamiz
# shaxs1 = Shaxs("Shoxrux", "Vohidov", 2005, "AD0123456")
# print(shaxs1.get_info())
# print(shaxs1.get_passport())
# print("Odamlar soni:", Shaxs.get_odamlar_soni())

# # Talaba ob'ekti
# talaba1 = Talaba("Dilshod", "Sultonov", "AD1234567", 2004, "Toshkent")
# print(talaba1.get_info())
# print("Talaba ID:", talaba1.get_id())
# print("Talabalar soni:", Talaba.get_talabalar_soni())




