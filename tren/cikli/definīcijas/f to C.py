import os
os.system('cls')

def main():
    x = float(input("Ievadi grādus celsijā:"))
    parveidot(x)

def parveidot(x):
    print(x*9/5+32)


main()