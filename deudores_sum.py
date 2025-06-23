import pandas as pd

cli=[1,5,3,1,5]
ped=['p105','p103','p109','p102','p101']
imp=[1000,1500,1200,1000,700]
pag=[True,False,True,False,True]

a=pd.Series(cli,name='cliente')
b=pd.Series(ped,name='pedido')
c=pd.Series(imp,name='importe')
d=pd.Series(pag,name='pagado')

data=pd.concat([a,b,c,d],axis=1)

pagado=data[data['pagado']==False]
print(pagado)
deuda=pagado['importe'].sum()
print('la deuda es de: ',deuda)
