# 05.03.2025
# vohidov
# fuzzywuzzy

from fuzzywuzzy import fuzz

satr1 = "salom dunyo"
satr2 = "salo dunya"
print(fuzz.ratio(satr1, satr2))  # Umumiy o‘xshashlik
print(fuzz.partial_ratio(satr1, satr2))  # Qisman o‘xshashlik