nombre = input("Tapez un nombre: ")

conversion = int(nombre)

compte = 0

for i in range(2, conversion):
    if conversion % i == 0:
        compte += 1

if compte == 0 and conversion > 1:
    print("Ce nombre est premier")
else:
    print("Ce nombre n'est pas premier")
