#17. Programa en el cual reciba como entradas la siguiente información: Código del Estudiante, Nombre del Estudiante, Nombre de la Materia y Tres Notas de 1.0 a 5.0. Con esta información el programa debe calcular la nota definitiva (promedio) y determinar si el estudiante aprueba o no la materia.   

cod = int(input("Digite su codigo de estudiante: "))
nom = input("Digite su numbre: ")
mat = input("Digite la materia: ")

not1 = float(input("Digite la primera nota: "))
not2 = float(input("Digite la segunda nota: "))
not3 = float(input("Digite la tercera nota: "))

prom = (not1+not2+not3)/3

if prom >= 4.0:
    print(nom)
    print(cod)
    print(mat)
    print("¡Aprobo!")
else:
    print(nom)
    print(cod)
    print(mat)
    print("No aprobo")