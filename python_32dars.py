# 22.02.2025
# vohidov
# FAYLLAR BILAN ISHLASH

# with open('pi.txt') as fayl:
#     pi = fayl.read() 

# print(pi)

# fayl = open('pi.txt')
# pi = fayl.read()
# # print(pi)
# fayl.close()

# pi = pi.rstrip() # qator ohiridagi bo'shliqlarni olib tashlaymiz
# pi = pi.replace('\n','') # qator tashlash belgisini almashtiramiz
# pi = float(pi)
# print(pi,type(pi))

# with open('data/pi.txt') as fayl:
#     pi = fayl.read()

# print(pi)

# faylnomi = 'data/math/numbers/salom.txt'

# with open(faylnomi) as fayl:
#     salom = fayl.read()
# print(salom)

# filename = 'data/talabalar.txt'
# # with open(filename) as file:
# #     for line in file:
# #         print(line)

# with open(filename) as file:
#     talabalar = file.readlines()
# print(talabalar)

# talabalar = [talaba.rstrip() for talaba in talabalar]
# print(talabalar)

# filename = 'data/ustozlar.txt'
# with open(filename,'w') as file:
#     file.write('Mahkam domla')

# faylnomi = 'data/new_file.txt'
# ism = 'Olimjon Hasanov'
# tyil = 2004
# with open(faylnomi,'w') as fayl:
#     fayl.write(ism+'\n')
#     fayl.write(str(tyil)+'\n')

# with open(faylnomi,'a') as fayl:
#     fayl.write('Alijon Valiyev\n')
#     fayl.write('2000')

# import pickle

# talaba1 = {'ism':'shoxrux','familiya':'vohidov','tiyil':2005,'kurs':0}
# talaba2 = {'ism':'jonibek','familiya':'najimov','tiyil':2004,'kurs':3}

# with open('info.txt','wb') as file:
#     pickle.dump(talaba1,file)
#     pickle.dump(talaba2,file)

# with open('info','rb') as file:
#     talaba1 = pickle.load(file)
#     talaba2 = pickle.load(file)

# print(talaba1)
# print(talaba2)

# amaliyot

# filename = 'data/example.txt'

# with open(filename) as file:
#     matn = file.read()
# print(matn)

# filename = 'pi_million_digits.txt'

# with open(filename) as file:
#     pi = file.read()

# pi = pi.rstrip()
# pi = pi.replace('\n','')
# pi = pi.replace(' ','')

# # print(pi)

# bdate = '022025'

# # print(bdate in pi)

# pi = float(pi)

# import pickle

# filename2 = 'pickle_file'

# with open(filename2,'wb') as file:
#     pickle.dump(pi,file)

# with open(filename2,'rb') as file:
#     plain_txt = pickle.load(file)

# print(plain_txt)

# filename = 'data/user_datas.txt'

# data = input("Assalomu alaykum, iltimos ismingizni kiriting: ")

# with open(filename,'a') as file:
#     file.write(data)

# with open(filename) as file:
#     print(file.read())