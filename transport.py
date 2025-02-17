# from uuid import uuid4
# class Avto:
#     """Avtomanil klassi"""
#     __num_avto = 0
#     def __init__(self,make,model,rang,yili,narh,km=0):
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yili = yili
#         self.narh = narh
#         self.__km = km
#         self.__id = uuid4()
#         Avto.__num_avto += 1

#     @classmethod
#     def get_num_avto(cls):
#         return cls.__num_avto

#     def get_km(self):
#         return self.__km

#     def get_id(self):
#         return self.__id

#     def add_km(self,km):
#         "Mashinaning km ga yana km qo'shish"
#         if km>=0:
#             self.__km += km
#         else:
#             return "Mashina km kamaytirib bo'lmaydi"




# # avto1 = Avto("GM","Malibu","Qora",2020,40000,100000)
# # # avto1.__km

# # print(f"ID: {avto1.get_id()}")

# # avto1.add_km(1500)
# # print(avto1.get_km())
# # avto1 = Avto("GM","Malibu","Qora",2020,40000)
# # avto2 = Avto("GM","Lacetti","Oq",2020,20000)
# # # print(avto1.num_avto)
# # avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
# # print(Avto.num_avto)

# # avto1 = Avto("GM","Malibu","Qora",2020,40000)
# # avto2 = Avto("GM","Lacetti","Oq",2020,20000)
# # avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
# # print(Avto.get_num_avto())

# class Bus:
#     pass

# class Train:
#     pass

# PI = 3.14159