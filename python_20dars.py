# 02.02.2025
# vohidov
# *args, **kwargs

# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi
# a = summa(1,2,3,4,5,6,7,8,9)
# print(a)

# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     return sum(sonlar)

# print(summa(4,5,6,7))

# def summa(x,y,*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     return x+y+sum(sonlar)

# print(summa(4,5,6,7))

# def avto_info(kompaniya,model,**malumotlar):
#     """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
#     malumotlar['kompaniya']=kompaniya
#     malumotlar['model']=model
#     return malumotlar

# avto1 = avto_info("GM", "malibu", rang='qora', yil=2018)
# avto2 = avto_info("Kia", "K5", rang='qizil', narh=35000)

# print(avto2)

# def multiplication(*sonlar):
#     """Istalgancha son qabul qilib ko'paytmasini hisoblovchi function"""
#     result = 1
#     for son in sonlar:
#         result *= son
#     return result

# a = multiplication(5,6)
# print(a)

# def student_info(firstname,lastname,**datas):
#     """Information of students"""
#     datas['ism']=firstname
#     datas['familiya']=lastname
#     return datas

# student1 = student_info('shoxrux','vohidov',kurs=2,fakultet="IT")

# print(student1)