re=True
Lista = {'toby':False,'coco':True,'leo':False}
while re:
    ver=input("desea buscar a una mascota?:  ").lower()
    if ver=="si":
        nom=input("ingrese su nombre: ").lower()  
        
        if nom in Lista:
            print("Mascota:", nom)
            print("Vacunado:", Lista.get(nom))
            
            if Lista[nom] == False:
                cam = input("¿Desea actualizar el estado de vacunación? (si/no): ").lower()
                
                if cam == "si":
                    Lista[nom] = True
                    print("se ha actualizado el estatus")
                else:
                    break
        else:
            print("La mascota no ha sido encontrada")
    else:
        re=False
        print("adios")
        
