with open('monfichier.txt', encoding='utf-8') as x:
    texte = x.read()
    text_renverse = texte[::-1]
    print(text_renverse)
    with open('nouveau_fichier_cree_automatiquement', mode='w', enconding='utf8') as fw:
        fw.write(text_renverse)