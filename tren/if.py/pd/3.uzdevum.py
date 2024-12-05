import os
os.system('cls')
print("\n")

gadi = int(input("Cik tev gadu? "))

if gadi <8:
    print("Biļete bez maksas")
if gadi >= 8 and gadi <= 18:
    print("Biļete maksā 5 eiro")
if gadi >= 18 and gadi <= 65:
   print("Biļete maksā 10 eiro")
if gadi >65:
    print("Biļete maksā 3 eiro")