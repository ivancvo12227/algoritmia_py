#27. Programa que muestre un menú que tenga las siguientes opciones: 1. Pasa o no la materia? 2. Es mayor o menor de edad? Caso 1: Solicitar 3 notas y determinar si el promedio es mayor a 3.0, en ese caso el estudiante pasa. Caso 2: Se debe solicitar el año de nacimiento y el año actual y determinar si es o no mayor de edad.

print("\t.:MENU:.")
print("1. Pasa o no la materia")
print("2. Es mayor o menor de edad")

n = int(input("Eliga una opción: "))

if n == 1:
    nota1 = float(input("Digite la primera nota: "))
    nota2 = float(input("Digite la segunda nota: "))
    nota3 = float(input("Digite la tercera nota: "))
    prom = (nota1+nota2+nota3)/3
    if prom >= 3.0:
        print("¡Paso la materia!")
    else:
        print("No pasas la materia")
elif n == 2:
    año_ac = int(input("Año actual: "))
    año_na = int(input("Año de nacimiento: "))
    edad = año_ac-año_na
    if edad >= 18:
        print("Eres mayor de edad")
    else: 
        print("Eres menor de edad")
else:
    print("Error")