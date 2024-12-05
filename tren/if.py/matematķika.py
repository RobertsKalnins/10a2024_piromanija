import os
os.system('cls')#attīra termināla logu sākumā
print("\n")#ieleik tukšu rindu pirms izdrukas (:. formatēšanas string)
import math


a = float(input("Kāds ir a? "))
b = float(input("Kāds ir b? "))
c = float(input("Kāds ir c? "))


d = (math.sqrt(b ** 2 - 4 * a * c))
d = d.real

if d > 0:
    print("Ir 2 saknes")
elif d < 0:
    print("Ir 0 saknes")
else:
    print("Ir viena sakne")


x_1 = (-b + d) / (2*a)
x_2 = (-b - d) / (2*a)

if d == 0:
    print(f"Ir tikai viena sakne un ta ir {x_1}")
else:
    print(f"x1 is {x_1:.2f}")
    print(f"x2 is {x_2:.2f}")