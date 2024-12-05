import os
os.system('cls')
print("\n")

skaitlis =int (input("Ievadi skaitli: "))

if skaitlis > 0:
    print("Skaitlis ir pozitīvs")
elif skaitlis == 0:
    print("skaitlis ir nulle")
elif skaitlis < 0:
    print("Skaitlis ir negatīvs")
if skaitlis % 2 == 0:
    print("Šis ir pāra skaitlis")
else:
    print("Skaitlis ir nepāra")

