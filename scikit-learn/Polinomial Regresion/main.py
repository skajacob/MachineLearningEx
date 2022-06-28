#%%
#####LIBRERIAS A UTLIZAR######

#Importamos las librerias a utilizar
import numpy as np
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

######PRERARAR LA DATA######

#Importamos los datos de la misma libreria de scikilearn
boston = datasets.load_boston()



######ENTENDIMIENTO DE LA DATA###########

#verificamos la informacion contenida en el dataset
print('Informacion en el dataset: \n')
print(boston.keys())

#verifico las caracteristicas del dataset
print('Caracteristicas del dataset: \n')
print(boston.DESCR)

#Verificar la informacion de las columnas
print('Nombres de columnas: \n')
print(boston.feature_names)


###### PREPARAR LA DATA REGRESION POLINOMIAL #######

#Selecionamos solamente la columna 6 del dataset
X_p = boston.data[:, np.newaxis, 5]
print(X_p)

#Definimos los datos correspondientes a las etiquetas
y_p = boston.target

#Graficamos los datos correspondientes
# # plt.scatter(X_p, y_p,)
# # plt.show()

#######IMPLEMENTACION DE REGRESION POLINOMIAL ######

#separo los datos de "Train" en entrenamiento y prueba para probar el algoritmos
X_train_p, X_test_p, y_train_p, y_test_p = train_test_split(X_p, y_p, test_size=0.2)

#Se define el grado del polinomio

poli_reg = PolynomialFeatures(degree=2)

#Se transforma las caracteristcas existentes en caracteristicas de mayor grado
X_train_poli = poli_reg.fit_transform(X_train_p)
X_test_poli = poli_reg.fit_transform(X_test_p)

#Defina el algoritmo a utilizar
pr = linear_model.LinearRegression()

#Entreno el modelo
pr.fit(X_train_poli, y_train_p)


#realiza una prediccion
y_pred_pr = pr.predict(X_test_poli)

#Graficamos los datos juntos con el modelo
plt.scatter(X_test_p, y_test_p)
plt.plot(X_test_p, y_pred_pr, color='red', linewidth= 3)
plt.show

print('DATOS DEL MODELO REGRESION POLINOMIAL \n')

print('Valor de la pendiente o coeficiente "a": \n')
print(pr.coef_)

print('Precision del modelo: \n')
print(pr.score(X_train_poli, y_train_p))

# %%
