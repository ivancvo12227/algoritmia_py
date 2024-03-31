#57.  Programa que permita calcular la cantidad total de clientes que atienden en un mes un hotel utilizando un vector. Como entrada se debe solicitar el número de clientes que atiende el hotel cada día del mes.

mes = []

i = 0 

while i < 30:
    clientes = int(input(f"Cuantos clientes ingresaron el día {i+1}: "))
    i+=1
    mes.append(clientes)

print(mes)

total_cli = sum(mes)

print(f"El total de clientes en el mes fue de {total_cli}")