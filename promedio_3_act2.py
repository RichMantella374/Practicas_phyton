print("ingresa 10 calificaciones")
si=0
j=0
for i in range(10):
    cal=int(input("Dame tu calificacion de 0 a 10: "))
    if cal%3==0:            
        si=cal+si
        j=j+1
    else:
        cal=0
    print(si)
re=si/j
print("el promedio de las cal multiplo de 3 es: ",re)
    
