



import random

#for i in range(dice_rolls):
        #roll = random.randit(1, 6)
rezultati =[]
skaits_6 = 0
metienu_skaits = 0

while metienu_skaits < 50:
    metiens = random.randint(1, 6)
    #rezultati.append(metiens)
    if metiens ==6:
        skaits_6 += 1
    metienu_skaits += 1

print(f"Sešinieku skaits uzmests {skaits_6} reizes")

