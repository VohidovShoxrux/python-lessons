# 8.11.2024
# vohidov
# NESTING
# car0 = {
#     'model':'gentra',
#     'rang':'qora',
#     'yil':2023,
#     'yurgan':130000,
#     'karobka':'avtomat',
#     'narh':15000
# }

# car1 = {
#     'model':'L9',
#     'rang':'olabula',
#     'yil':2024,
#     'yurgan':1001,
#     'karobka':'avtomat',
#     'narh':30000
# }

# car2 = {
#     'model':'L7',
#     'rang':'qizil',
#     'yil':2022,
#     'yurgan':1001001,
#     'karobka':'avtomat',
#     'narh':25000
# }

# cars = [car0, car1 ,car2]

# for car in cars:
#     print(f"{car['model'].title()}, " 
#           f"{car['rang']} rang, "
#           f"{car['yil']}-yil, {car['narh']}$"    
#     )

# print(cars[1]['model'])

# l9 = []

# for n in range(10):
#     new_car = {
#         'model':'L9',
#         'rang':None,
#         'yil':2024,
#         'narh':None,
#         'km':0,
#         'karobka':'avto'
#     }
#     l9.append(new_car)

# for l in l9:
#     print(l)

# for n in l9[:3]:
#     n['rang'] = 'qizil'

# for n in l9[3:6]:
#     n['rang'] = 'qora'

# for n in l9[6:]:
#     n['rang'] = 'qora'
#     n['karobka'] = 'mexanika'

# for n in l9:
#     if n['karobka'] == 'avto':
#         n['narh'] = 40000
#     else:
#         n['narh'] = 30000

# for l in l9:
#     print(l)

# dasturchilar = {
#     'ali':['c++','python'],
#     'vali':['c#','.NET'],
#     'hasan':['java','php'],
#     'husan':['js','css','html'],
#     'fuzayil':['kotlin','Ruby']
# }

# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quydagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(f"{til.upper()}")

# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quydagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(f"{til.upper()} ", end=' ')

# colleague = {
#     'ali':{
#         'familya':'valiyev',
#         'tyil':1995,
#         'malumot':'oliy',
#         'tillar':['python', 'c#']
#     },
#     'vali':{
#         'familya':'aliyev',
#         'tyil':1993,
#         'malumot':'o\'rta maxsus',
#         'tillar':['html','css','java']
#     },
#     'hasan':{
#         'familya':'husanov',
#         'tyil':1991,
#         'malumot':'maxsus',
#         'tillar':['python','php']
#     }
# }

# for ism, info in colleague.items():
#     print(
#         f"\n{ism.title()} {info['familya'].title()}, "
#         f"{info['tyil']}-yilda tug'ilgan. "
#         f"Ma'lumoti: {info['malumot']}. \n"
#         "Quydagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print(til.upper())

