import pandas as pd
n=['luis','juan','pedro','carlos']
p=[5,6,5,5]
s=[6,7,8,9]
t=[8,7,9,6]

nombre=pd.Series(n,name='nombre')
primer=pd.Series(p,name='primer')
segundo=pd.Series(s,name='segundo')
tercero=pd.Series(t,name='tercero')


data=pd.concat([nombre,primer,segundo,tercero],axis=1)

print(data)