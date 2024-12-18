vies = 7
mot_mystere = "dqslkj"
taille_mot = len(mot_mystere)
mot_masque = ['-'] * taille_mot

print(''.join(mot_masque))

while (''.join(mot_masque) != mot_mystere) and (vies > 0):
    lettre = input('Tapez une lettre: ')

    if lettre in mot_mystere:
        for i in range(len(mot_mystere)):
            if mot_mystere[i] == lettre:
                mot_masque[i] = lettre
        print(''.join(mot_masque))
    else:
        vies -= 1
        print(f"Erreur, il vous reste {vies} vies")
        print(''.join(mot_masque))

if ''.join(mot_masque) == mot_mystere:
    print('Vous avez gagné!')
else:
    print('Vous avez perdu.')
