#18. Programa para determinar cuánto pagara una persona por una compra de la cual se sabe la cantidad de artículos y el valor unitario. Se debe tener en cuenta que el almacén hace un 20% de descuento cuando la compra supera $100000. 

prod = int(input("Cantidad de articulos: "))
val_un = float(input("Valor unitario: "))

prod_f = prod*val_un

if prod_f >= 100000:
    print("El valor total con descuento es de")
    desc = prod_f*0.20
    print(prod_f-desc)
else:
    print("No tiene descuento")