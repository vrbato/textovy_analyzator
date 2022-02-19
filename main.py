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
#statické veličiny

oddelovac = "-" * 49
oddelovac_rovnase = "=" * 49

# 1. Akční kod
# 1.1 úvod, zadání uživatele a ověření, zda je registrován a zadal správné heslo

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
elif not len(password) == len(users[username]["password"]) and password in users[username]["password"]:
    print("Wrong password! Terminating the program...")
    quit()
else:
    print(f"Welcome to the app, {username}",f"We have 3 texts to be analyzed.", sep='\n')

print(oddelovac)

# 1.2. práce s textem

text_choice = input("Enter a number btw. 1 and 3 to select: ")
if text_choice.isalpha():
    print("Wrong value! Should be only numerals! Terminating the program...")
    quit()
elif not int(text_choice) in range(1,4):
    print("Wrong range! Terminating the program...")
    quit()
else:
    print(oddelovac)
#počet slov
pocet_slov = {}
for slovo in TEXTS[int(text_choice)-1].split():
    if slovo not in pocet_slov:
        pocet_slov[slovo] = 1
    else:
        pocet_slov[slovo] = pocet_slov[slovo] + 1
print(f"There are {sum(pocet_slov.values())} words in the selected text.")

#počet slov s velkým písmenem
pocet_slov_title = {}
for slovo in TEXTS[int(text_choice)-1].split():
    if slovo.istitle():
        if slovo not in pocet_slov_title:
            pocet_slov_title[slovo] = 1
        else:
            pocet_slov_title[slovo] = pocet_slov_title[slovo] + 1
print(f"There are {sum(pocet_slov_title.values())} titlecase words.")

#počet slov BIG
pocet_slov_BIG = {}
for slovo in TEXTS[int(text_choice)-1].split():
    if slovo.isupper():
        if slovo not in pocet_slov_BIG:
            pocet_slov_BIG[slovo] = 1
        else:
            pocet_slov_BIG[slovo] = pocet_slov_BIG[slovo] + 1
print(f"There are {sum(pocet_slov_BIG.values())} uppercase words.")

#počet slov LOWER
pocet_slov_LOWER = {}
for slovo in TEXTS[int(text_choice)-1].split():
    if slovo.islower():
        if slovo not in pocet_slov_LOWER:
            pocet_slov_LOWER[slovo] = 1
        else:
            pocet_slov_LOWER[slovo] = pocet_slov_LOWER[slovo] + 1
print(f"There are {sum(pocet_slov_LOWER.values())} lowercase words.")

#počet slov NUMERIC
pocet_slov_num = {}
for slovo in TEXTS[int(text_choice)-1].split():
    if slovo.isnumeric():
        if slovo not in pocet_slov_num:
            pocet_slov_num[slovo] = 1
        else:
            pocet_slov_num[slovo] = pocet_slov_num[slovo] + 1
print(f"There are {sum(pocet_slov_num.values())} numeric strings.")

#suma čísel v textu
sum_numbers = []
for slovo in TEXTS[int(text_choice)-1].split():
    if slovo.isnumeric():
        sum_numbers.append(int(slovo))
print(f"The sum of all the numbers {sum(sum_numbers)}.")

print(oddelovac,
      f"LEN| {'OCCURENCES':^20} |NR.",
      oddelovac,
      sep="\n"
)

#četnost slov podle délky
cetnost_slov = {}
for slovo in TEXTS[int(text_choice)-1].split():
    delka = len(slovo.strip(",.!:").lower())
    cetnost_slov[delka] = cetnost_slov.get(delka,0) + 1

sorted_cetnost = sorted(list(cetnost_slov.items()), reverse=False)

for l, c in sorted_cetnost:
   print(
       f"{l:>3}|{'*'*c:<22}|{c}"
   )
