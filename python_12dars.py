# 17.01.2025
# vohidov
# lug'at

# car = {'model':"gentra",'rang':"qora"}
# print(car['model'].title())
# print(car['rang'].capitalize())

# talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
# print(f"{talaba_0['ism'].title()},\
#  {talaba_0['t_yil']}-yilda tu'gilgan,\
#  {talaba_0['yosh']} yoshda")

# talaba_0['kurs'] = 2
# talaba_0['fakultet'] = 'informatika'

# print(talaba_0)

# talaba_1 = {}
# talaba_1['ism'] = 'qobil rasulov'
# talaba_1['kurs'] = 3
# talaba_1['yosh'] = 20
# # print(talaba_1)
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")
# talaba_1['kurs'] = 4 # 'kurs' ni 4 ga o'zgartiramiz.
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
# print(talaba_0)
# del talaba_0['yosh'] # yosh degan kalit so'z (va qiymatni) o'chiramiz
# print(talaba_0)

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }

# phone = telefonlar['ali']
# print(f"Alining telefoni {phone}")
# # phone = telefonlar['hasan']
# # print(f"Hasanning telefoni {phone}")
# # phone = telefonlar.get('hasan','Bunday ism mavjud emas')
# # print(phone)
# phone = telefonlar.get('hasan')
# print(phone)

# amaliyot

# onam = {
#     'ism':'Abdujabborova Mohidil',
#     't_yil':1974,
#     'viloyat':'Andijon'
# }
# tyil = onam['t_yil']
# vil = onam['viloyat']
# print(f"Onamning ismi {onam['ism']}, {tyil}-yilda, {vil} viloyatida tug'ilgan")

# taomlar = {
#     'men':'osh',
#     'onam':'mastava',
#     'jiyanim':'somsa',
#     'akam':'dimlama'
# }
# taom = taomlar['men']
# print(f"Mening sevimli taomim {taom}")

# python_izohli_lugati = {
#     'integer':"Butun son",
#     'float':"O'nlik son",
#     'string':"Matn",
#     'list':"Ro'yxat",
#     'tuple':"O'zgarmas ro'yxat"}
# soz = input("Kalit so'z kiriting:")
# qiymat = python_izohli_lugati.get(soz,"bunday so'z mavjud emas")
# print(qiymat)

# python_izohli_lugati = {
#     'integer':"Butun son",
#     'float':"O'nlik son",
#     'string':"Matn",
#     'list':"Ro'yxat",
#     'tuple':"O'zgarmas ro'yxat"}
# soz = input("Kalit so'z kiriting:")
# qiymat = python_izohli_lugati.get(soz)
# if qiymat:
#     print(f"{soz.title()} so'zi {qiymat.capitalize()} deb tarjima qilinadi")
# else:
#     print("Bunday so'z mavjud emas")