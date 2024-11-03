# 3.11.2024
# vohidov
# Dictionary (lu'gat)

# lugat = {'model':'tahoe', 'rang':'qora', 'yili':'2024' }
# print(lugat['model'])
# print(lugat['rang'])

# eng_uz = {'apple':'olma', 'banana':'banan', 'pineapple':'ananas'}
# print(eng_uz)

# mevalar = {'olma':10000, 'nok':12000, 'gilos':40000}
# print(f"Olma narhi {mevalar['olma']}")

# student = {'ism':'jonibek', 'age':19, 'year':2005}
# print(f"{student['ism'].title()},\
#     {student['year']}-yilda tug'ulgan.\
#     {student['age']} yoshda" )

# student['car'] = 'tahoe'
# student['meal'] = 'hotlunch'
# student['ism'] = 'najim'

# print(student)

# student = {}
# student['ism'] = 'Jonibek Najimov'
# student['kurs'] = 2
# student['yo\'nalish'] = 'kampyuter xakkerligi'
# # print(student)
# # student['kurs'] = 3
# # print(f"Talaba {student['ism'].title()} {student['kurs']}-kurs ")
# print(student)

# del student['yo\'nalish']
# print(student)

# telefonlar = {
#     'olim':'iphone 12',
#     'dolim':'iphone se',
#     'men':'samsung tab a9',
#     'karl':'iphone 16 pro max ultra 5HZ' 
# }
# # print(telefonlar['karl'])
# phone = telefonlar.get('john')
# print(phone)

# Amaliyot 

# otam =  {'ism':'Ravshanbek', 'yil':1971, 'viloyat':'Andijon', 'kasb':'o\'qtuvchi'}
# print(f"Otamning ismi {otam['ism']}, {otam['yil']}-yilda, {otam['viloyat']} viloyatida tug'ilgan kasbi {otam['kasb']}!")

# taomlar = {
#     'Akam':'manti',
#     'Men':'mastava',
#     'Opam':'sho\'rva',
#     'Jiyanim':'lagmon'
# }

# print(f"Mening sevimli taomim {taomlar['Men']}!")

# lugatpy = {
#     'integer':'butun sonlar',
#     'float':'o\'nlik sonlar',
#     'string':'matn',
#     'boolean':'mantiqiy qiymat true false',
#     'if':'shart operatori',
#     'for':'bu loop',
#     'del':'o\'chirish',
#     'title':'boshharif katta qilish',
#     'len':'funksiya list uzunligini',
#     'range':'fubksiya berilgan oraliqdasonlar ketma ketligini yaratadi',
#     'list':'ro\'yxat',
# }    

# key = input("Kalit so'zni kiriting:").lower()
# # print(lugatpy.get(key, "Bunday so'z mavjud emas!"))

# tarjima = lugatpy.get(key)

# if tarjima == None:
#     print("Bunday so'z mavjud emas!")
# else:
#     print(f"{key.title()} so'zi {tarjima} deb nomlanadi" )