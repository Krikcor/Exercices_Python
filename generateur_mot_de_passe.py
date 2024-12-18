import string
import random

taille = 8

lettres = string.ascii_letters + string.digits + string.punctuation
mot_de_passe = ''.join(random.choice(lettres) for l in range(taille))

print(mot_de_passe)