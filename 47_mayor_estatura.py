#47. Crear un Programa que permita conocer la mayor estatura dentro un grupo de N estudiantes.  

n = int(input("Cuantos estudiantes son: "))
lista = []
i = 0 
while i < n:
    estat = float(input("Digite su estatura: "))
    lista.append(estat)
    i+= 1
max_alt = max(lista)

print(f"La mayor estatura es de {max_alt:.2f} mts")