#49. Programa que muestre un menú al usuario que se repita las veces que sea necesario, hasta que escoja la opción Salir. Las opciones del menú deben permitir:    
#1. Calcular el factorial de un número (usando un ciclo repetitivo for) 2. Calcular la potencia (usando un ciclo repetitivo while) 3. Salir 

continuar = True

while continuar:
    print("\t.:MENU:.") 
    print("1. Calcular el factorial de un número")
    print("2. Calcular la potencia")
    print("3. Salir")
    op = int(input("Elige una opción: "))
    if op == 1:
        n = int(input("Digite un numero positivo: "))
        if n < 0:
            print("Error")
            n = int(input("Digite un numero positivo: "))
        else:
            resultado = 1
            for i in range(n):
                resultado *= n
                n -= 1
        print(f"El factorial es {resultado}")
    elif op == 2:

        resultado = 1
        contador = 0

        base = float(input("Ingresa la base: "))
        exponente = int(input("Ingrese el exponente en numero positivo: "))

        while contador < exponente:
            resultado*= base
            contador+=1

        if exponente < 0: 
            print("Digite un numero positivo")
        else: 
            resultado = base**exponente
            print(f"{base} elevado a la {exponente} es: {resultado}")
    elif op == 3:
        print("Saliste del programa")
        break
    else: 
        print("Error")