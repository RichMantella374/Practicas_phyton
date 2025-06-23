import pandas as pd
datos = pd.read_csv("ligamx.csv")
goles=datos[datos["Gf"]==20]
#datos[datos["segundo"]==7] hace el corte por renglon
#Series es como una lista  en pandas
equipos=datos[["Equipo","Pg"]]
L=['uno','dos','tres']
s=pd.Series(L,index=[901,902,903])
#s=pd.Series(L) convierte a serie tipo columna, si le pongo index cambia el numero de identificacion

print(s[901])
#print(goles)
#print(equipos)
