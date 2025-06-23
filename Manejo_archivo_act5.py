lineas = [linea.strip() for linea in open("a.txt")]
s = open("a.txt").read().lower()
palabras= s.split()
vocales="aeiou"
contador=0
for palabra in palabras:
    if palabra and palabra[0] in vocales:   
        contador += 1  
total=len(palabras)
if total > 0:
    porcentaje = (contador / total) * 100
else:
    porcentaje = 0
print(s)
print(total)
print(porcentaje,"%")

