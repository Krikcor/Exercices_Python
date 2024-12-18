essai = 7

devine = 14



while True:
    nombre = int(input("devinez le nombre entre 0 et 20 "))

    if nombre == devine:
        print("bravo vous avez trouvé")
        break

    else:
        essai -= 1
        if essai == 0:
            print("Vous avez perdu")
            break