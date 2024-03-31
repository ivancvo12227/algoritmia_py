#33. Programa para calcular la edad promedio de un grupo de 15 estudiantes.

lista = []

for i in range(0,15):
    edad = int(input("Cual es tu edad:"))
    lista.append(edad)
print(lista)

suma = sum(lista)

prom = suma/15

print(f"La edad promedio es de {prom}")