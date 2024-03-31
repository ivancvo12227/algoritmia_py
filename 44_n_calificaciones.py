#44. Programa que reciba N calificaciones de una materia, y luego calcule: a) La nota promedio b) La nota mayor c) Si El estudiante pasa o no la materia (Promedio>=40) 

cal = int(input("Cuantas notas quiere ingresar: "))
i = 0
lista_not = []

while i<cal:
    notas = float(input("Digite la nota: "))
    lista_not.append(notas)
    i += 1
print(lista_not)

suma = sum(lista_not)

prom = suma/cal

max_nota = max(lista_not)

print(f"El promedio fue de {prom}")
print(f"La nota maxima fue de {max_nota}")

if prom >= 4.0:
    print(f"Pasas la materia con {prom}")
else: 
    print(f"No pasas la materia con {prom}")
