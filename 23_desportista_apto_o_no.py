# 23. Programa para determinar si un deportista es aceptado en el equipo de baloncesto de Bogotá. Las condiciones para ser aceptado son: a) La edad debe ser menor o igual a 18 años b) La estatura debe ser mayor a 180 cm c) El peso debe ser menor o igual a 80 kg.

edad = int(input("Cual es su edad: "))
estatura = int(input("Cual es su estatura: "))
peso = int(input("Cuanto pesas: "))  

if edad <= 18 and estatura >= 180 and peso <= 80:
    print("¡Aceptado en el equipo de baloncesto!")
else:
    print("No fuiste aceptado")