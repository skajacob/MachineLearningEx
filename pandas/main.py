import numpy as np
import pandas as pd

#crear un dataframe con indices
data = np.array([['','Col1','Col2'],['Fila1',11,22],['Fila2',33,44]])
pd.DataFrame(data=data[1:,1:], index=data[1:,0],columns=data[0,1:])

#crear dataframe 
df = pd.DataFrame(data=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]))

#crear serias con diccionarios
series = pd.Series({
    "Argentina":"Buenos Aires",
    "Chile":"Colombia",
    "Peru":"Mexico",
    "Lima":"Bogota"
})


#forma del tada frame
df.shape
#alruta de un frame
len(df.index)
#estadisticas de dataframe
df.describe()
#media de todas las columnas
df.mean()
#correlacion del dataframe
df.corr()
#cuenta de os datos del dataframe
df.count()
# conocer el valor mas alto de cada columna
df.max()
#conocer el valor mas bajo de cada columna
df.min()
#conocer la mediana de la columna 
df.median()
#conocer la desviacion estandar de cada columna
df.std()
#obtener la primera o segunda columna del dataframe
df[0]
df[[0,1]]
#Seleccionar el valor de la primera fila y ultima columna
df.iloc[0][2]
#seleccionar los valores de la primera fila del dataframe
df.loc[0]
df.iloc[0,:] #con iloc
#Verificar si hay datos nulos en el data fram
df.isnull() 
#suma de datos nulos en el dataframe
df.isnull().sum() 
#eliminar la fila de los valores nulos
pd.dropna()
df.dropna(axis=1)
#en caso de no querer eliminar las filas y rellenarlas con otros valores
df.fillna('x')
#Reemplazar los valores perididos por la media 
df.fillna(df.mean())