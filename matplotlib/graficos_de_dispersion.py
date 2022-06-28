#importamos la libreia
import matplotlib.pyplot as plt

#Definimos los datos
x1=[0.25, 1.25, 2.25, 3.25, 4.25]
y1=[10, 55, 80, 32, 40]
x2=[0.75, 1.75, 2.75, 3.75, 4.75]
y2=[42, 26, 10, 29, 66]

#configurar las caracteristicas del grafico
plt.scatter(x1, y1, label='Datos 1', color = 'red')
plt.scatter(x2, y2, label='Datos 2',  color = 'purple')

#definir titulo y nombre de los ejes
plt.title('Diagrama de dispersion')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')

#mostrar leyenda y figura
plt.legend()
plt.show()