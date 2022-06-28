#importr libreria
import matplotlib.pyplot as plt

#definir los datos
dormir = [7,8,6,11,7]
comer = [2,3,4,3,2]
trabajar = [7,8,7,2,2]
recreacion = [8,5,7,8,13]
divisiones = [7,2,2,13]
actividades = ['Dormir', 'Comer', 'Trabajar','Recreacion']
colores = ['red', 'purple','blue', 'orange']

#configurar las caracteristicas del grafico
plt.pie(divisiones, labels=actividades, colors=colores, startangle=90, shadow=True, explode=(0.1,0,0,0), autopct='%1.1f%%')

#definir titulo
plt.title('grafico circular')
#mostrar figura
plt.show  
#%%