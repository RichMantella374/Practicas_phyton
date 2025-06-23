import pandas as pd
liga = pd.read_csv('ligamx.csv')

ordenado=liga.loc[liga['Df']<0,['Equipo','Pg','Df']]

print(ordenado.sort_values(by='Pg',ascending=False))

print('\n datos filtrados \n')
print(ordenado.head(3))