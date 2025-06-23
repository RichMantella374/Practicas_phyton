import pandas as pd

datos= pd.read_csv('ligamx.csv')

ganados= datos[datos['Pg']>6]
print(ganados)

columnas= datos[datos['Pp', 'Df']]
print(columnas)

 