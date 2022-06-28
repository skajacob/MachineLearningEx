#importamos las libreras
from sklearn import linear_model, datasets
import numpy as np
import matplotlib.pyplot as plt

#importamos los datos de la misma libreria de scikit learn
boston = datasets.load_boston()

#######ENTENDIMIENTO DE LA DATA##############
#verificar la informacion de la dataset
# print("Informacion del dataset")
# print(boston.keys())

#verificamos  las caracteristicas del dataset
# print("Caracteristicas del dataset")
#print(boston.DESCR)

#para verificar los datos que hay en el dataset 
#print(boston.data.shape)

#para obtener el indices de las columnas
#print(boston.feature_names)


#Seleccionamos solamente la columna 5 del data set numero de cuartos RM
X = boston.data[:, np.newaxis, 5]

#Definimos los datos correspondientes a las etiqeutas
y = boston.target

#graficamos los datos correspodientes con grafica de dispersion para visualixzar mejor los datos
plt.scatter(X,y)
plt.xlabel("Numero de habitaciones")
plt.ylabel("Valor medio")
plt.show()

###IMPLEMENTAMOS LA REGRESION LINEAL SIMPLE ####
from sklearn.model_selection import train_test_split

#separamos los datos de "train" en entrenamiento y prueba para probar los algorimos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#definimos el algoritmo a utilizar
lr = linear_model.LinearRegression()

#entrenamos el modelo
lr.fit(X_train,y_train)

#realizamos la prediccion
Y_pred = lr.predict(X_test)

#Graficamos los datos junto con el modelo

plt.scatter(X_test, y_test)
plt.plot(X_test, Y_pred, color='red', linewidth=3)
plt.title("Regresion Lineal Simple")
plt.xlabel("Numero de habitaciones")
plt.ylabel("Valor medio")
plt.show()

print("DATOS DEL MODELO REGRESION LINEAL SIMPLE")
print()
# print('Valor de la pendiente o coeficiente "a":')
# print(lr.coef_)
# print('Valor de la pendiente o coeficiente "b":')
# print(lr.intercept_)

print(f'La ecuacion del modelo es igual a: y={lr.coef_}x {lr.intercept_} ')
print()
#imprimir la presicion del modelo
print(f'La presicion del modelo es igual a: {lr.score(X_train, y_train)}')