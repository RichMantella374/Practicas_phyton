import pandas as pd
datos = pd.read_csv('ligamx.csv')
goles=datos[datos["Gf"]==20]
print(goles)

eq=datos[["Equipo","Pg"]]
print(eq)

print("akjsndhjkadhjkas")
print(datos.loc[datos['Pj']>10,['Equipo','Pj']])
print("akjsndhjkadhjkas")
ordenado=datos.loc[datos['Pj']>10,['Equipo','Pj']]
print(ordenado.sort_values(by='Pg',ascending=False))
print(ordenado.head(2))