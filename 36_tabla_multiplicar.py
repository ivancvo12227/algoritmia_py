#36. Programa que imprima la tabla de multiplicar hasta 10 de un número cualquiera ingresado por el usuario. 

mult = int(input("De que numero quiere ver la tabla de multiplicar: "))

for i in range(0,10):
    i += 1
    tabla = mult*i
    print(f"{mult} * {i} : {tabla}")