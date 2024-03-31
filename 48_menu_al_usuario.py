#48. Programa que muestre un menú al usuario que se repita las veces que sea necesario, hasta que escoja la opción salir. Las opciones del menú deben permitir:       
#1. Ingresar 2 números 2. Realizar la suma 3. Realizar la resta 4. Realizar la multiplicación 5. Realizar la división 6. Salir del programa 

continuar = True

while continuar:
    print("\t.:MENU:.") 
    print("1. Ingresar 2 números")
    print("2. Realizar la suma")
    print("3. Realizar la resta")
    print("4. Realizar la multiplicación")
    print("5. Realizar la división")
    print("6. Salir del programa")
    op = int(input("Elige una opción: "))
    if op == 1:
        num1 = int(input("Digite un numero: "))
        num2 = int(input("Digite un numero: "))
    elif op == 2:
        suma = num1+num2
        print(f"El resultado de la suma es {suma}")
    elif op == 3:
        resta = num1-num2
        print(f"El resultado de la suma es {resta}")
    elif op == 4:
        mult = num1*num2
        print(f"El resultado de la suma es {mult}")
    elif op == 5:
        div = num1/num2
        print(f"El resultado de la suma es {div}")
    elif op == 6:
        continuar = False
        print("Saliste del programa")
    else: 
        print("Error")
