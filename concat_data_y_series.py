import pandas as pd
p=[7,8,5]
s=[9,6,10]
i=['a1','a2','a3']

primer=pd.Series(p,name='uno',index=i)
segundo=pd.Series(s,name='dos',index=i)
datos=pd.concat([primer,segundo],axis=1)

dato1=pd.DataFrame([{'uno':10,'dos':7}],index=['a'+str(datos['uno'].count()+1)])

datos=pd.concat([datos,dato1],axis=0)
print(datos)
