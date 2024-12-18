from collections import Counter

def compte_mots(phrase):
    mots = phrase.lower().split()
    compteur = Counter(mots)
    return dict(compteur)