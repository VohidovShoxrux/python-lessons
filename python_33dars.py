# 23.02.2025
# vohidov
# JSON

# import json

# # x = 10 
# # x_json = json.dumps(x)

# ism = "shoxrux"
# ism_json = json.dumps(ism)

# sonlar = [11,21,32,43,54]
# sonlar_json = json.dumps(sonlar)

# # print(type(sonlar_json))

# bemor = {
#   "ism": "Alijon Valiyev",
#   "yosh": 30,
#   "oila": True,
#   "farzandlar": ("Ahmad","Bonu"),
#   "allergiya": None,
#   "dorilar": [
#     {"nomi": "Analgin", "miqdori": 0.5},
#     {"nomi": "Panadol", "miqdori": 1.2}
#   ]
# }

# bemor_json = json.dumps(bemor, indent=4)
# # print(bemor_json)

# # with open('bemor.json','w') as f:
# #     json.dump(bemor,f)

# # sonlar = json.loads(sonlar_json)
# # bemor = json.loads(bemor_json)
# # print(bemor)

# # filename = 'bemor.json'

# # with open(filename) as f:
# #     bemor = json.load(f)

# # print(type(bemor),bemor)

# data = {
#     "address_components": [
#         {
#             "long_name": "Almazar District",
#             "short_name": "Almazar District",
#             "types": [
#                 "political",
#                 "sublocality",
#                 "sublocality_level_1"
#             ]
#         },
#         {
#             "long_name": "Tashkent",
#             "short_name": "Tashkent",
#             "types": [
#                 "locality",
#                 "political"
#             ]
#         },
#         {
#             "long_name": "Tashkent Region",
#             "short_name": "Tashkent Region",
#             "types": [
#                 "administrative_area_level_1",
#                 "political"
#             ]
#         },
#         {
#             "long_name": "Uzbekistan",
#             "short_name": "UZ",
#             "types": [
#                 "country",
#                 "political"
#             ]
#         }
#     ],
#     "formatted_address": "Almazar District, Tashkent, Uzbekistan",
#     "geometry": {
#         "bounds": {
#             "northeast": {
#                 "lat": 41.3954567,
#                 "lng": 69.269883
#             },
#             "southwest": {
#                 "lat": 41.3249733,
#                 "lng": 69.16497629999999
#             }
#         },
#         "location": {
#             "lat": 41.3645355,
#             "lng": 69.2281531
#         },
#         "location_type": "APPROXIMATE",
#         "viewport": {
#             "northeast": {
#                 "lat": 41.3954567,
#                 "lng": 69.269883
#             },
#             "southwest": {
#                 "lat": 41.3249733,
#                 "lng": 69.16497629999999
#             }
#         }
#     },
#     "place_id": "ChIJ195FnkeMrjgR3nkapKKdk7A",
#     "types": [
#         "political",
#         "sublocality",
#         "sublocality_level_1"
#     ]
# }

# kenglik = data['geometry']['location']['lat']
# uzunlik = data['geometry']['location']['lng']
# print(f"{kenglik},{uzunlik}")

# amaliyot
# 1-mashiq
import json

data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2025, "Narh":40000}

data_json = json.dumps(data)

# print(data_json)

talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""

# talaba = json.loads(talaba_json)
# print(talaba['ism'], talaba['familiya'])

# with open('amaliyot.json','w') as f:
#     json.dump(data_json,f)

# with open('students.json', 'r') as f:
#     talabalar = json.load(f)

# students = talabalar['student']

# for student in students:
#     ism = student['name']
#     familiya = student['lastname']
#     kurs = student['year']
#     fakultet = student['faculty']
#     print(f"{ism} {familiya}, {kurs}-kurs, {fakultet} talabasi")



    




