#!/usr/bin/env python3

import random

valor = random.randint(1,100)

print("\nDebes adivinar un numero que acabo de pensar")

print("\nEs un numero entre 0 y 100")

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

print("\nEl numero era", valor, "Y te costo", intentos,"intentos.")
