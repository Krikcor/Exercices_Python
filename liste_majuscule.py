villes = ["Paris", "Strasbourg", "Lyon"]
villes_maj = []
villes_maj_2 = [v.upper() for v in villes]

for i in villes:
    villes_maj.append(i.upper())

print(villes_maj)
print(villes_maj_2)