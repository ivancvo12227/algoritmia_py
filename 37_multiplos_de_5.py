#37. Realizar un Programa que permita visualizar en pantalla los múltiplos de 5 hasta el número 100.

mult = []

for i in range(1,101):
    if i%5==0:
        mult.append(i)
print(mult)