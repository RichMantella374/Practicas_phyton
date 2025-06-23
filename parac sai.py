# -*- coding: utf-8 -*-
"""
Created on Mon May 26 10:01:15 2025

@author: LCE3-16
"""
import pandas as pd
#los data frames se pueden hacer de varias series, las setries nnon de una dimencion, y oara 
n=['luis','juan','pedro','monica','itzel']
p=[7,9,6,8,5]
s=[8,10,7,6,10]
t=[8,8,9,9,8]

nombre=pd.Series(n,name='nombre')
primer=pd.Series(p,name='primer')
segundo=pd.Series(s,name='segundo')
tercero=pd.Series(t,name='tercero')

calif=pd.concat([nombre,primer,segundo,tercero],axis=1)
#calif['promedio']=(calif["primer"]+calif["segundo"]+calif["tercero"])/3
#calif['proimedio']=calif[['primer','segundo','tercero']].mean(axis=1)   
nuevo= pd.DataFrame([{"nombre":"oscar","primer":7,"segundo":9,"tercero":6}],index=[calif["nombre"].count()])
calif= pd.concat([calif,nuevo])