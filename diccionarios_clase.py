cadena = "2 3 15 2 9 15 100 4 2"
elementos=cadena.split(' ')

f={}
g={}
for i in range(len(elementos)):
    f[elementos[i]]=elementos.count(elementos[i])
    
for item in elementos:
    if item in g:
        g[item]+=1
    else:
        g[item]=1
        
print(f)
print(g)