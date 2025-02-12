# 12.02.2025
# vohidov
# kiril lotiun telegram bot

from transliterate import to_cyrillic , to_latin

matn = input("Matn kiriting:")

if matn.isascii():
    print(to_cyrillic(matn))
else:
    print(to_latin(matn))


