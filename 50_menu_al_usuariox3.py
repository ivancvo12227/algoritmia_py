#50. Programa que muestre un menú al usuario que se repita las veces que sea necesario, hasta que escoja la opción Salir. Las opciones del menú deben permitir:    
#1. Números pares hasta 100 (usando for) 2. Múltiplos de 4 (usando while) 3. Tabla de Multiplicar de un número hasta 10  

seguir = True
            
while seguir:
    print("\t.:MENU:.") 
    print("1. Números pares hasta 100")
    print("2. Múltiplos de 4")
    print("3. Tabla de Multiplicar de un número hasta 10")
    print("4. Salir")
    op = int(input("Elige una opción: "))
    if op == 1:
        for i in range(1, 101):
            if i%2 == 0:
                print (i)
    elif op == 2:
        i = 0
        while i < 100:
            i+=1
            if i%4 == 0:
                print(i)
    elif op == 3: 
        num = int(input("Digite un numero: "))
        for i in range(1, 11):
            tabla = num * i
            print(f"{num} * {i} : {tabla}")
    elif op == 4:
        print("Saliste del programa")
        seguir = False
    else:
        print("Error")