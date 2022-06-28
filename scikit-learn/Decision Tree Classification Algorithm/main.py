#%%
from sklearn import tree
from sklearn.model_selection import train_test_split, cross_val_predict
from sklearn import metrics
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('car.csv', header= None)

data.columns = ['price', 'maintenance', 'n_doors', 'capacity', 'size_lug', 'safety', 'class']
# print(data.head(5))
# print("------------------------")
# print(data.sample(5))
# print("------------------------")
# print(data[['price', 'capacity']].tail(5))
# print("------------------------")
# print(data.shape)
# print("------------------------")
# print(data['maintenance'].sample(6))
# print("------------------------")
# print(data['price'][0:6])
# print("------------------------")
# print(data['class'].value_counts().sort_index(ascending= True))#ordenar por index alfabeticamente
# print("------------------------")


#generar tabla de barras de la columna decision
desicion = data['class'].value_counts()
desicion.plot(kind='bar')



#generar tabla con colores personalidad del precio de los vehivulos
price = data['price'].value_counts()
#recomdable rempalazar datos tipo string por tipo int
data['price'].replace(('vhigh', 'high' ,'med' ,'low'),(4,3,2,1), inplace= True)
print(data['price'].unique())
print(data['price'].head())
colors = ['#DDEE01','#CC0101','#FE10D1','#BCC111']
price.plot(kind='bar',color=colors)
plt.xlabel('Precio')
plt.ylabel('Autos')
plt.title('Precio de los autos')

#grafica de pastel
data['safety'].value_counts()
labels = ['low', 'med', 'high']
size = [576, 576, 576]
colors = ['cyan', 'gray', 'orange']
explode = [0, 0, 0]
plt.pie(size, labels = labels, colors= colors, explode= explode, shadow= True, autopct='%.2f%%')
plt.title('Nivel de seguridad', fontsize= 10)
plt.axis('off')
plt.legend(loc = 'best')
plt.show()


#arbol de decision
data.price.replace(('vhigh', 'high', 'med', 'low'),(4, 3, 2, 1), inplace= True)
data.maintenance.replace(('vhigh', 'high', 'med', 'low'),(4, 3, 2, 1), inplace= True)
data.n_doors.replace(('2', '3', '4', '5more'),(1, 2, 3, 4), inplace= True)
data.capacity.replace(('2', '4', 'more'),(1, 2, 3), inplace= True)
data.size_lug.replace(('small', 'med', 'big'),(1, 2, 3), inplace= True)
data.safety.replace(('low', 'med', 'high'),(1, 2, 3), inplace= True)
data['class'].replace(('unacc','acc','good','vgood'),(1,2,3,4), inplace=True)
#Recomendacion de division de datos
#   -80% aprendizaje
#   -20% pruebas 
dataset = data.values
x = dataset[:, 0:6]
y = np.asarray(dataset[:,6],dtype='S6')

X_Train, X_Test, Y_Train, Y_Test = train_test_split(x, y, test_size = 0.2, random_state = 0)

tr = tree.DecisionTreeClassifier(max_depth=10)

tr.fit(X_Train, Y_Train)

y_pred = tr.predict(X_Test)

score=tr.score(X_Test,Y_Test)

print('Precision: %0.4f' % (score))

