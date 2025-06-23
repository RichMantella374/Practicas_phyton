import matplotlib.pyplot as plt
import pandas as pd
datos = pd.read_csv('ligamx.csv')

valores= datos['Pg'].value_counts() #Muestra cantidad de veces que se repite el parametro

plt.bar(valores.index,valores.values)
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid(False) #malla
plt.title('Partidos ganados') 

#plt.xticks(fontsize=6)
plt.show()
                                        
print(valores.index)
print(valores.values)
