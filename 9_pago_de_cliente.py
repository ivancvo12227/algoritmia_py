#9. Programa que permita a una tienda saber el valor que pagara un cliente por la compra de varios elementos de la misma referencia. Debe tener como entradas el valor unitario, la cantidad de productos comprados y al valor final se debe adicionar el 16% correspondiente al IVA.   

cantidad = int(input("Cuantos productos compro: "))
valorunit = float(input("De cuanto es el valor unitario: "))

iva = valorunit*0.16

total = valorunit+iva

print(f"El total es {total}")