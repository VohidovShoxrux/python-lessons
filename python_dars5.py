# 20/10/2024
# vohidov
# LISTS

# mevalar = ["olma", "anjir", "nok", "shaftoli", "'orik"]
# narxlar = [1, 2, 3, 4]
# sonlar = ["bir", "ikki", "uch", 4, 5, 6, 7]
# ismlar = []

# print(sonlar[-1]) # oxiridai elementni ko'rish uchun index -1 ni bermaiz
# ismlar = narxlar[0]+narxlar[-1]
# print(ismlar)
# mevalar[-1] = "gilos"
# print(mevalar)
# mevalar.append("pineapple") # .append metodi doyim listga oxiridan element qo'shadi
# print(mevalar)
# narxlar.insert(0, sonlar) # .insert metodi yordamida listni istalgan joyiaga element hatta list qo'shish mumkun
# sonlar.insert(3, mevalar)
# sonlar.insert(4,narxlar)
# print(narxlar)

# cars = []
# cars.append("tahoe")
# cars.append("lacetti")
# cars.append("malibu")
# cars.append("tarverse")
# print(cars)
# del cars[0] # Inedks yordamida olib tashlash uchun del operatoridan foydalanamiz:
# print(cars)
# cars.insert(0, "kobalt")
# print(cars)
# cars.remove("malibu") # Element qiymati bo'yichi o'chirish uchun esa .remove(qiymat) metodidan foydalanamiz. 
# print(cars)

# hayvonlar = ['qoy', 'mol', 'echki', 'qoplon', 'bori', 'it', 'mol']
# print(hayvonlar)
# hayvonlar.remove('mol') # listda birixil elemntlarni .remove metdi yordamida o'chirganimizda listnig boshidan boshlab o'chiradi
# print(hayvonlar)

#Ba'zida biror elementni butunlay o'chirib tashlash emas, balki uni ro'yxatdan sug'urib olish va undan foydalanish talab qilinishi mumkin. Buning uchun Pythonda .pop(indeks) metodidan foydalanmiz.

# bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
# mahsulot = bozorlik.pop(3) # Ro'yxatdan banan ni sug'urib olamiz
# print("Men " + mahsulot + " sotib oldim")
# print("Olinmagan mahsulotlar: ", bozorlik)

# Amaliyot
# ismlar = ["humo", 'joniy', 'karl']
# print(f"Salom {ismlar[0]}, bugun choyxona bormi?\n{ismlar[2]}, choyxonaga borasanmi?")

# sonlar = [213, 12.75, -25, 0 ]
# print(sonlar)
# sonlar[-1] = 100
# sonlar[0] = sonlar[0]-13
# sonlar[2] = sonlar[2]+26
# sonlar[1] = sonlar[1]*100
# print(sonlar)

# t_shaxslar = ["Jaloliddin Manguberdi", "Temur Malik", "Sariq Logot", "Amir Temur"]
# z_shaxslar = ["Abror Muhtor ali", "Azimjon", "Muhammadali", "Abdulloh domla"]
# t = t_shaxslar.pop(0)
# z = z_shaxslar.pop(-1)
# print("Men tarixiy shaxslardan " + t +" bilan,\n" + "zamonaviy shaxslardan " + z + " bilan suhbat qilishni istardim.")
 
# friends = []
# friends.append("Abdulhakim")
# friends.append("KamronMuhammad")
# friends.append("Abdulatif")
# friends.append("Muhammadziyo")
# friends.append("Muhammadumar")
# print(friends)
# friends.remove("KamronMuhammad")
# friends.remove("Muhammadziyo")
# print(friends)
# friends.insert(0,"Hakimjon")
# friends.insert(-1,"Fuzayl")
# friends.insert(2,"Zokirjon")
# print(friends)

# mehmonlar = []
# mehmonlar.append(friends.pop(2))
# mehmonlar.append(friends.pop(-2))
# mehmonlar.append(friends.pop(0))
# print("\nKelgan mehmonlar: ", mehmonlar)