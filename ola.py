from string import punctuation
f=open("datos.txt",mode='r')
#datos=f.read()
#d1=datos.split('\n')
#datos=f.readline()
#datos=[linea for linea in open("datos.txt")]
datos=f.read()
words=datos.split(' ')

for w in words:
    for p in punctuation:
        w=w.replace(p,'')  
        print(w)
