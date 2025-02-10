# 10.02.2025
# vohidov
# son topish o'yini

# import random as r

# def sontop(x=10):
#     son = r.randint(1,x)
#     print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?:")
#     qadam = 0
#     while True:
#         qadam += 1
#         taxmin = int(input(">>>"))
#         if taxmin < son:
#             print("Xato, men o'ylagan son bundan kattaroq. Yana harakat qiling:")
#         elif taxmin > son:
#             print("Xato, men o'ylagan son bundan kichikroq. Yana harakat qiling:")
#         else:
#             break

#     print(f"Tabriklayman! {qadam} ta taxmin bilan topdingiz.")
#     return qadam
     
# def sontop_pc(x=10):
#     input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
#     quyi = 1
#     yuqori = x
#     qadam = 0
#     while True:
#         qadam += 1
#         if quyi != yuqori:
#             taxmin = r.randint(quyi,yuqori)
#         else:
#             taxmin = quyi
#         javob = input(f"\nSiz {taxmin} sonni o'yladingiz: to'g'ri (t),"
#                       f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower())
#         if javob == "-":
#             yuqori = taxmin - 1
#         elif javob == "+":
#             quyi = taxmin + 1
#         else:
#             break
#     print(f"Men {qadam} ta taxminda bilan topdim!")
#     return qadam

# def play(x=10):
#     yana = True
#     while yana:
#         qadamlar_user = sontop(x)
#         qadamlar_pc = sontop_pc(x)
#         if qadamlar_user > qadamlar_pc:
#             print("Men yutdim!")
#         elif qadamlar_pc > qadamlar_user:
#             print("Siz yutdingiz!")
#         else:
#             print("Durrang!")
#         yana = int(input("Yana o'ynaysizmi? Ha(1)/Yo'q(0):"))

# play()
