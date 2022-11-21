#!/usr/bin/env python3

nombre = input("¿Cual es tu nombre?\n")

edad = input("¿Cuantos años tenes? ")

masa = input("Ok. Ùltima pregunta. ¿Cuanto pesas? ")

print("Si no te funcionara el Shift, tu nombre seria",nombre.lower())

print("Ahora, si tuvieses el Caps Lock trabado, sería",nombre.upper())

print("Si un nene chiquito te quisiera llamar la atención, tu nombre se volvería:")

print(nombre*5)

print("Tu edad es de",int(edad)*31536000,"segundos")

print("¿Sabías que en la Luna pesarías sólo",int(masa)*0.16,"kilos?")

print("Ahora bien, en el Sol, tu peso sería de",int(masa)*27.1,"aunque no por mucho...")

print("Presionar enter para continuar...")

input()
