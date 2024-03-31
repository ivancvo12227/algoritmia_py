#22. Programa que permita calcular el valor final a pagar en una súper tienda en donde se aplican los siguientes descuentos: a) Por compras entre 10000 y 20000 el 10% b) Por compras entre 20001 y 50000 el 30% c) Por compras superiores a 50000 el 50%.

prod = int(input("Cantidad de articulos: "))
val_un = float(input("Valor unitario: "))

prod_f = prod*val_un

if prod_f >= 10000 and prod_f <= 20000:
    desc = prod_f*0.10
    total_f = prod_f-desc
    print(f"El valor final con el descuento del 10% {total_f}")
elif prod_f >= 20001 and prod_f <= 50000:
    desc = prod_f*0.30
    total_f = prod_f-desc
    print(f"El valor final con el descuento del 30% {total_f}")
elif prod_f > 50000:
    desc = prod_f*0.50
    total_f = prod_f-desc
    print(f"El valor final con el descuento del 50% {total_f}")
else:
    print("No tiene descuento")