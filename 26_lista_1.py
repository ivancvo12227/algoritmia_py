#26. Programa que permita ingresar un número cualquiera y luego mostrar el siguiente menú: 1. Determinar si es positivo o negativo 2. Determinar si es par o impar. El programa debe realizar las operaciones que el usuario seleccione del menú.

num = int(input("Digite un numero: "))

print("\t.:MENU:.")
print("1. Determinar si es positivo o negativo.")
print("2. Determinar si es par o impar.")

n = int(input("Elija una opción: "))

if n == 1:
    if num > 0:
        print("El numero es positivo")
    else:
        print("El numero es negativo")
elif n == 2:
    if num % 2 == 0:
        print("El numero es par")
    else: 
        print("El numero es impar")