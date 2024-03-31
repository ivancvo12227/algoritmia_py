#56. Programa que permita llenar un vector de 18 posiciones y después mostrarlo al revés.

lista = []

for i in range(18):
    num = int(input("Digite un numero: "))
    lista.append(num)

invertida = list(reversed(lista))

print(invertida)