import random

mot = "Bonjour"
mot = list(mot)

random.shuffle(mot)

resultat = "".join(mot).capitalize()

print(resultat)