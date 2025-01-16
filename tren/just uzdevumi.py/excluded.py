import os
os.system('cls')

nosaukums = input("Ievadi tekstu: ")

burti="aāeēiīoAĀEĒIĪO"

if burti in nosaukums:
    print (nosaukums.strip(burti))
else:
    print()