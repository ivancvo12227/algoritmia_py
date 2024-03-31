#34.  Programa que permita calcular la estatura promedio de un grupo de 18 estudiantes y luego tomar las siguientes decisiones: a) Si la estatura promedio es menor a 140 cm imprimir un mensaje que diga “Estudiantes muy bajos”. b) Si la estatura promedio se encuentra entre 140 y 170 cm imprimir “Estudiantes de estatura normal”. c) Si la estatura promedio es mayor de 170 cm imprimir “Estudiantes muy altos”. 

lista = []

for i in range(0,18):
    estat = int(input("Cual es su estatura en cm: "))
    lista.append(estat)
print(lista)

suma = sum(lista)
prom = suma/18

if prom < 140:
    print("Estudiantes muy bajos")
elif prom >= 140 and prom <= 170:
    print("Estudiantes de estatura normal")
elif prom > 170:
    print("Estudiantes muy altos")