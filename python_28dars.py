# 14.02.2025
# vohidov
# OBYKETLAR BILAN ISHLASH

# class Talaba:

#     def __init__(self,ism,familiya,tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1
    
#     def get_info(self):
#         return f"{self.ism.title()} {self.familiya.title()}. {self.bosqich}-bosqich talabasi "
    
#     def set_bosqich(self,bosqich):
#         self.bosqich = bosqich

#     def update_bosqich(self):
#         self.bosqich += 1
    
#     def get_name(self):
#         return self.ism

#     def get_lastname(self):
#         return self.familiya
    
#     def get_fullname(self):
#         return f"{self.ism} {self.familiya}"
    
#     def get_age(self, yil):
#         return yil-self.tyil


# talaba1 = Talaba("shoxrux","vohidov",2005)
# # print(talaba1.get_info())
# # talaba1.bosqich = 2
# # print(talaba1.bosqich)

# # talaba1.set_bosqich(3)
# # print(talaba1.get_info())

# # talaba1.update_bosqich()
# # # print(talaba1.get_info())

# # talaba1.update_bosqich()
# # print(talaba1.get_info())

# class Fan():
#     def __init__(self,nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []

#     def add_student(self,talaba):
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1
    
#     def get_name(self):
#         return self.nomi
    
#     def get_students(self):
#         return [talaba.get_info() for talaba in self.talabalar]

#     def get_students_num(self):
#         return self.talabalar_soni

# matematika = Fan("Oliy Matematika")
# talaba1 = Talaba("Alijon","Valiyev",2000)
# talaba2 = Talaba("Hasan","Alimov",2001)
# talaba3 = Talaba("Akrom","Boriyev",2001)

# matematika.add_student(talaba1)
# matematika.add_student(talaba2)
# matematika.add_student(talaba3)

# # print(matematika.talabalar_soni)

# # print(matematika.talabalar)

# mat_talabalar = matematika.get_students()
# # print(mat_talabalar)

# # print(dir(Talaba))

# def see_methods(klass):
#     return [method for method in dir(klass) if method.startswith('__') is False]

# # print(see_methods(Talaba))
# # print(see_methods(talaba1))
# # print(talaba1.__dict__)
# print(talaba1.__dict__.keys())