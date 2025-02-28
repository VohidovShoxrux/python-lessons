# 26.02.2025
# vohidov
# FUNKSIYANI TEKSHIRISH

def get_full_name(ism,familiya,otasi=''):
    if otasi:
        return f"{ism} {otasi} {familiya}".title()
    else:
        return f"{ism} {familiya}".title()

# print(get_full_name("shoxrux","vohidov"))
