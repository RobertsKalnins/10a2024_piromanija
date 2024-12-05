#skolotajs = ["Gustava", "Ungure", "Deksne", "Gladčenko"]
#macibu_prieksmets = ["matematika", "matematika", "matematika", "fizika"]

# skolotaja = {
#     "Gustava": "matematika",
#     "Ungure": "matematika",
#     "Deksne": "matematika",
#     "Gladčenko": "fizika",
#              }

# print(skolotaja["Gladčenko"])\

# for skol in skolotaja:
#     print(skol, skolotaja[skol], sep="māca ")

# skolotaja = [
#     {"uzvards": "Gustava", "macibu prieksmets": "matematika", "kabinets": "27."},
#     {"uzvards": "Ungure", "macibu prieksmets": "matematika", "kabinets": "205."},
#     {"uzvards": "Deksne", "macibu prieksmets": "matematika", "kabinets": None},
#     {"uzvards": "Gladčenko", "macibu prieksmets": "fizika", "kabinets": "206."},
#     ]
# for skol in skolotaja:
#     print(skol["uzvards"], skol["macibu prieksmets"], skol["kabinets"], sep=",")


platums = int(input("platums- "))
augstums = int(input("Augstums- "))

for i in range(augstums):
    for j in range(platums):
        print("@", end="")
    print()