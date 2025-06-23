d = {'luis':(18,'6im5'),'juan':(17,'6im6'),'pedro':(19,'6im6'),'monica':(17,'6im4')}
l = []
l2 = []

for nombre,(edad,grupo) in d.items():
    if grupo == '6im6':
        l.append((nombre,edad))
    if edad >= 18:
        l2.append(nombre)
        
l = tuple(l)
print(l)
print(l2)