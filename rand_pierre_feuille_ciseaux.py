import random

options = ['pierre', 'feuille', 'ciseaux']

selection_rand = random.choice(options)

choix = input("pierre feuille ciseaux? ")

if choix == selection_rand:
    print("Egalite!")
else:
    if (choix == "pierre" and selection_rand == "ciseaux") or (choix == "feuille" and selection_rand =="pierre") or (choix == "ciseaux" and selection_rand == "feuille"):
        print("Gagné")
    else:
        print("Perdu")