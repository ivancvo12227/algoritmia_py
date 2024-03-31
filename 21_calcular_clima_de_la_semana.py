#21. Programa el cual permita ingresar los valores de temperatura de cada día durante una semana. Le programa debe calcular la temperatura promedio y luego mostrar los siguientes mensajes: a) Si el promedio es mayor a 35° mostrar el mensaje “Que semana tan calurosa” b) Si el promedio esta entre 15° y 35° mostrar el mensaje “Que clima tan delicioso” c) Si el promedio es menor de 15° mostrar el mensaje “Que semana tan fría”.

dia1 = int(input("Temperatura del dia 1: "))
dia2 = int(input("Temperatura del dia 2: "))
dia3 = int(input("Temperatura del dia 3: "))
dia4 = int(input("Temperatura del dia 4: "))
dia5 = int(input("Temperatura del dia 5: "))
dia6 = int(input("Temperatura del dia 6: "))
dia7 = int(input("Temperatura del dia 7: "))

dia_prom = (dia1+dia2+dia3+dia4+dia5+dia6+dia7)/7

if dia_prom > 35:
    print("Que semana tan calurosa")
    print(f"El clima promedio fue de {dia_prom:.2f}°")
elif dia_prom >= 15 and dia_prom <= 35:
    print("Que clima tan delicioso")
    print(f"El clima promedio fue de {dia_prom:.2f}°")
elif dia_prom < 15: 
    print("Que semana tan fria")
    print(f"El clima promedio fue de {dia_prom:.2f}°")