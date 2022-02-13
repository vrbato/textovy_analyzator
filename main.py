'''
author = Tomáš Vrba
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
oddelovac = "-" * 49
oddelovac_rovnase = "=" * 49
# 1. úvod, zadání uživatele a ověření, zda je registrován a zadal správné heslo

print(oddelovac_rovnase)
print(f"{'-' * 17} {'TEXT Analysis':^10} {'-' * 17}")
print(oddelovac_rovnase)

#uživatel
user1 = {"name" : "bob", "password" : "123"}
user2 = {"name" : "ann", "password" : "pass123"}
user3 = {"name" : "mike", "password" : "password123"}
user4 = {"name" : "liz", "password" : "pass123"}

users = {}
users[user1["name"]] = user1
users[user2["name"]] = user2
users[user3["name"]] = user3
users[user4["name"]] = user4

username = input("Enter your username: ")
password = input("Enter your password: ")
print(oddelovac)

#ověření
if not username in users:
    print("Unregistered user, terminating the program..")
    quit()
elif username in users and password in users[username]["password"]:
    print(f"Welcome to the app, {username}",f"We have 3 texts to be analyzed.", sep='\n')
else:
    print("Wrong password! Terminating the program...")

print(oddelovac)

