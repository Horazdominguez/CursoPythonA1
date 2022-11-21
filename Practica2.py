#!/usr/bin/env python3

import random

valor = random.randint(1,100)

print("\nDebes adivinar un nùmero que acabo de pensar")

print("\nEs un nùmero entre 0 y 100")

print("\nTe aviso si estàs cerca")

numero = int(input("\nColoca el nùmero: "))

intentos = 1

while numero != valor:

    if numero > valor:

        print("Más bajo...")
        intentos += 1
        numero = int(input("Proba otra vez:"))
    else:

        print("Más alto...")
        intentos += 1
        numero = int(input("Coloca el numero:"))


print("\nBien, Le pegaste")

print("\nEl nùmero era", valor, "Y te costo", intentos,"intentos.")
