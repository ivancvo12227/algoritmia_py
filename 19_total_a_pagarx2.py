#19. Programa que permita determinar el total a pagar por una compra de la cual se sabe el valor unitario y la cantidad. Se debe tener en cuenta que se realiza un descuento del 15% por compra inferiores a $20000 y del 35% por compras mayores o iguales a $20000.  

cant_prod = int(input("Cuantos productos adquirio: "))
val_un = int(input("Cuanto es el valor unitario: "))    

total = cant_prod*val_un

if total >= 20000:
    desc = total*0.35
    total_f = total-desc
    print(f"El valor con descuento: {total_f}")
elif total < 20000: 
    desc = total*0.15
    total_f = total-desc
    print(f"El valor con descuento: {total_f}")
    