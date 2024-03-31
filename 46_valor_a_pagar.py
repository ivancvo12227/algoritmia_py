#46. Programa que permita calcular el valor a pagar en una caja registradora donde se reciben N productos y se ingresan los precios de uno en uno.

cant = int(input("Cuantos productos va a pagar: "))
i = 0
lista = []
while i < cant:
    prod = float(input("Digite el valor del producto: "))
    i +=1
    lista.append(prod)

total = sum(lista)

print(f"El total es de {total:.3f}")