#importamos la libreria
import matplotlib.pyplot as plt

#definir los datos
a=[22,55,62,45,21,34,42,42,40,10,23,65,56,5,4,70,70,50,30,50,6]
bins=[0,10,20,30,40,50,60,70,80,90,100]

#configuramos las caracteriticas del grafico
plt.hist(a, bins, histtype='bar', rwidth=0.8, color='lightgreen')
#definir titulo y nombres de ejes
plt.title('Histograma')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
#mostrar figura
plt.show()
