prod=float(input("introduce el valor del producto: "))
desc=prod*0.2
prod_desc=prod-desc
iva=prod_desc*.15
precio_final=prod_desc+iva
print("El producto con descuento es de: ",prod_desc)
print("Iva: ",iva)
print("El precio final es de: ",precio_final)
