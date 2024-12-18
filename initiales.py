nom_complet = input("Entrez votre nom et prénom séparé d'un espace ")

scinder = nom_complet.split(" ")

initiales = str(scinder[0][0] + scinder[1][0])

print(initiales)