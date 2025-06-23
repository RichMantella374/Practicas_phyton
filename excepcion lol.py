P=['paleta','refresco','galleta']
C=[10,5,12]
try:
    nombre=input("Dame el producto: ")
    i=P.index(nombre.lower())
    print("el precio es de ",C[i])
except:
    print("no valido lol")
    