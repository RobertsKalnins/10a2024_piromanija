# ievade =  input("Ievadiet transportlīdzekļa numur zīmi atdalot ar komatiem:")

# numuri =  ievade.split(',')

# for numurs in numuri:
#     numurs = numurs.strip()

#     if len(numurs) < 4 or'-' not in numurs:
#         print(f"{numurs}:Numurzīme nav derīga")
#         continue
    
#     burti, cipari = numurs.split('-')

import re
numurs = input("Ievadi tramsportlīdzekļa numurzīmi: ").strip().upper()

modelis = r"^[A-PR-UZ]{2}-[1-9]\d{0,3}$"

flag = re.match(modelis, numurs)

if flag:
    print("Numurs ir derīgs.")
else:
    print("Numurs nav derīgs.")