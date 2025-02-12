# 11.02.2025
# vohidov
# so'z topish o'yini

# import random as r
# from wordlist import words  # To'g'ri import

# def get_word():
#     word = r.choice(words)
#     while "-" in word or ' ' in word:
#         word = r.choice(words)
#     return word.upper()

# def display(user_letters, word):
#     display_letter = ""
#     for letter in word:
#         if letter in user_letters:
#             display_letter += letter
#         else:
#             display_letter += "-"
#     return display_letter

# def play():
#     word = get_word()
#     word_letters = set(word)
#     user_letters = ""
#     print(f"Men {len(word)} xonali so'z o'yladim. Topa olasizmi?")
#     while len(word_letters) > 0:
#         print(display(user_letters, word))
#         if len(user_letters) > 0:
#             print(f"Shu vaqtgacha kiritgan hariflaringiz: {user_letters}")
            
#         letter = input("Harif kiriting: ").upper()  # To'g'ri yozish
#         if letter in user_letters:
#             print("Bu harifni oldin kiritgansiz. Boshqa harif kiriting!")
#             continue
#         elif letter in word:
#             word_letters.remove(letter)
#         else:
#             print("Bunday harif yo'q.")
#         user_letters += letter
#     print(f"Tabriklayman! {word} so'zini {len(user_letters)} ta urunishda topdingiz.")

