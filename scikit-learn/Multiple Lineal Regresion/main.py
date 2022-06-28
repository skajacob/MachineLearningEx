#%%
#Se importa la libreria a utilizar
from time import process_time_ns
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split

#####PREPARAR LA DATA#####

#importamos los datos de la misma libreria de scikit-learn
boston = datasets.load_boston()

#verificamos la informacion contenida en el dataset

print('Informacion en el dataset: \n')
print(boston.keys())

#verifico las caracteristicas del dataset
print('Caracteristicas del dataset: \n')
print(boston.DESCR)

#Verificar la informacion de las columnas
print('Nombres de columnas: \n')
print(boston.feature_names)


###### PREPARAR LA DATA REGRESION LINEAL MULTIPLE #######

#Selecionamos las comlumnas 5, 6 y 7 del dataset
X_multiple = boston.data[:, 5:8]
print(X_multiple)

#Definimos los datos correspondientes a las etiquetas
y_multiple = boston.target

#separo los datos de "Train" en entrenamiento y prueba para probar el algoritmos
X_train, X_test, y_train, y_test = train_test_split(X_multiple, y_multiple, test_size=0.2)

#definimos el algoritmo a utilizar
lr_multiple = linear_model.LinearRegression()

#entreno el modelo
lr_multiple.fit(X_train, y_train)

#Realizo una prediccion
y_pred_multiple = lr_multiple.predict(X_test)

print('DATOS DEL MODELO REGRESION LINEAL MULTIPLE \n')

print('Valor de las pendientes o coeficientes "a" :\n')
print(lr_multiple.coef_)

print('Valor de la intersseccion o coeficientes "b" :\n')
print(lr_multiple.intercept_)

print('Precision del modelo: \n')
print(lr_multiple.score(X_train, y_train))
# %%
