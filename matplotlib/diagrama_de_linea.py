import matplotlib.pyplot as plt
#Definimos los datos
x1=[3, 4, 5, 6]
y1=[5, 6, 3, 4]
x2=[2, 5, 8]
y2=[3, 4, 3]
#configurar la caracteristica del grafico
plt.plot(x1,y1, color='blue', linewidth=4, label='linea 1')
plt.plot(x2,y2, color='green', linewidth=4, label='linea 2')
#definir titulo y nombre de los ejes
plt.title('Diagrama de Lineas')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
#mostrar leyenda, cuadricula y figura
plt.legend()
plt.grid()
plt.show()