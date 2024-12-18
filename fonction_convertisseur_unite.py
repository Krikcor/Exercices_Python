def convertisseur(distance, unite):
    resultat = 0
    if unite == "km":
        resultat = distance/1000
    elif unite == "cm":
        resultat = distance*100
    else :
        resultat = distance*1000

    print (f"{distance} m équivaut à {resultat} {unite}")

convertisseur(10, "km")