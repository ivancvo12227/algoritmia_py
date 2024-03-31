#45. Programa  que  permita  calcular  el  factorial  de  un  número.  El  factorial  corresponde  a  la multiplicación de todos los números naturales anteriores incluyendo el número ingresado. 

num = int(input("Ingresa un número: "))

factorial = 1
i = 1

if num < 0:
    print("El factorial no está definido para números negativos.")
elif num == 0:
    print("El factorial de 0 es 1")
else:
    while i <= num:
        factorial *= i
        i += 1
    print("El factorial de", num, "es", factorial)