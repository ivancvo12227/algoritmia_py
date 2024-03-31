#20. Programa para determinar si un número cualquiera ingresado por el usuario es par o impar.(Usar operación Modulo).

num = int(input("Digite un numero: "))

if num % 2 == 0: 
    print ("El numero es par")
elif num % 2 != 0:
    print ("El numero es impar")