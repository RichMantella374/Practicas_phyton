import pandas as pd
datos = pd.read_csv('ligamx.csv')
x=datos["Gf"].std()
print(x)
