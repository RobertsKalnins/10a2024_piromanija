import os
os.system('cls')

# def main():
#     x = float(input("Ievadi pirmo skaitli:"))
#     pirmais(x)

# def pirmais(skaitlis):


#     y = float(input("Ievadi otro skaitli:"))
#     otrais(y)

# def otrais(skaitlis):



#     z = float(input("Ievadi trešo skaitli:"))
#     trešais(z)

# def trešais(skaitlis):
#     print()


# main()
def aritmetiska_vidēja(a, b, c):
    return (a + b + c) / 3

# Iegūstam ievadi no lietotāja
a = float(input("Ievadi pirmo skaitli: "))
b = float(input("Ievadi otro skaitli: "))
c = float(input("Ievadi trešo skaitli: "))

# Aprēķinām un izvadām rezultātu
rezultāts = aritmetiska_vidēja(a, b, c)
print(f"Aritmētiskais vidējais ir: {rezultāts}")