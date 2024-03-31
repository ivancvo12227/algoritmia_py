#10. Programa que permita determinar el salario a pagar a un empleado teniendo como entradas el salario diario y el número de días trabajados. Tenga en cuenta que al empleado se le debe descontar el 10% por concepto de pensión y 15% por concepto de salud.

sal_dia = 43333

dias_trab = int(input("Cuantos dias trabajo: "))

sal_sindesc = dias_trab*sal_dia

sal_pen = sal_sindesc*0.10

sal_salu = sal_sindesc*0.15

total_sal = sal_sindesc-sal_pen-sal_salu

print(f"El total del salario es de: {total_sal}")