import pandas as pd

datos = pd.read_csv("ligamx.csv")

filtar_datos=datos[datos["Pts."]==30] #filtrar datos xd
print(filtar_datos)

seleccionar_columnas=datos[["Equipo","Pg","Df"]] 
#filra cuantas columnas se ingresen
print(seleccionar_columnas)

print("hola x1dd")
filtro_con_columna = datos.loc[datos["Gf"] <= 15, ["Equipo"]]
#se filtra los datos y solo se muestra el dato solicitado "equipo"
print(filtro_con_columna)

print(datos["Gf"].describe())
print("hola x2d")

print(datos.min())
#acceder a un dato de describe uwu
print("hola x3d")

si = pd.DataFrame({
    "nombre": ["Ana", "Luis", "Carlos"],
    "primer": [8, 9, 6],
    "segundo": [7, 10, 5],
    "tercer": [9, 8, 7]
})
#crear una tabla con dataframe
print(si)

print("hola x4d")

ordenado=datos.loc[datos['Df']<0,['Equipo','Pg','Df']]

print(ordenado.sort_values(by='Pg',ascending=False))
#ascending es para acomodar de mas a menos en true