#1.uzd
for n in range(10000):
    summa = 0
    for i in range(1, n):
        if n % i == 0:
            summa = summa + i
    if summa == n:
        print(f"{n} ir perfekts skaitlis")

#2.uzd
rows = int(input("Ievadi skaitli: "))
for i in range(rows):
    for j in range(i+1):
        print(j+1, )
    while i == i :
            print()
    

#3.uzd
virkne = [0, 1]
