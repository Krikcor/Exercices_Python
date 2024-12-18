class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
    
    def perimetre(self):
        return (self.longueur * 2) + (self.largeur * 2)
    
    def aire(self):
        return self.longueur * self.largeur
    
    def est_carre(self):
        return self.longueur == self.largeur

premier_rect = Rectangle(4, 8)
second_rect = Rectangle(4, 4)

print(premier_rect.perimetre())
print(second_rect.est_carre())
