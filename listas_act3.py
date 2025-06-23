re=True
A=["Luis","Juan","Pepe","Joel"]
B=[10,6,2,9]
while(re):
    producto=input("desea buscar a un alumno?:  ")
    if producto=="si":
        nom=input("ingrese su nombre: ")
        encontrado=False
        
        for i in range(len(A)):
            if nom == A[i]:
                print("La calificación de ",nom," es de:",B[i])
                encontrado=True
                cam=input("La calificacion es correcta? si/no: ")
                if(cam=="no"):
                    ca_n=input("ingrese su nueva calificación: ")
                    B[i] = ca_n
                    print("La calificación de ",nom," es de:",B[i])
                break
            if encontrado==False:
                print("Alumno no encontrado.")                
    else:
        re=False