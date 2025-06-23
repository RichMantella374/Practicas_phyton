# -*- coding: utf-8 -*-  para eliminar es drop xd
"""
Created on Mon Jun  9 10:13:29 2025

@author: LCE3-16
"""
import pandas as pd
cliente=[1,5,3,1,5]
pedido=['p105','p103','p109','p102','p101']
importe=[1000,1500,1200,1000,700]
pagado=[True,False,True,False,True]


a=pd.Series(cliente,name='cliente')
b=pd.Series(pedido,name='pedido')
c=pd.Series(importe,name='importe')
d=pd.Series(pagado,name='pagado')
data=pd.concat([a,b,c,d],axis=1)

no_deudores=data[data['pagado']==True].index
data=data.drop(index=no_deudores,axis=1)