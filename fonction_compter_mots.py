def nombre_mots(a):
    liste_mots = a.split(" ")
    compte = len(liste_mots)

    return compte
    
total = nombre_mots("Il fait beau")

print (f"Il y a {total} mots dans cette phrase")