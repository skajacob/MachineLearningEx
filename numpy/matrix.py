#%%
import numpy as np

#generar matriz unidimencional
matrix_1d = np.array([1,2,3])
#generar una matris bidimencional
matrix_2d = np.array([(1,2,3),(4,5,6)])
#crear una matriz de unos de 2 dimensiones de nxm 
matriz_de_uno=np.ones((5,3))
#crear matriz de numero aleatorios
matriz_num_aleatorios= np.random.random((3,3))
#crear matriz vacia
matrix_vacia=np.empty((3,3))
#crar matriz de un solo valor
matrix_un_solo_valor=np.full((2,2),8)
#crear matrices con valores espaciados uniformemente
matrix_val_esp1=np.arange(0,30,5) #genera[0 5 10 15 20 25 30]
matrix_val_esp2=np.linspace(0,2,5) #genera[0. 0.5 1. 1.5 2.]
#crear matrix identidad
matrix_identidad1=np.eye(4,4)
matrix_identidad2=np.identity(4)

#conocer las dimenciones de una matriz
matrix_1d.ndim
matrix_2d.ndim
#conocer el typo de datos de una matriz
matrix_1d.dtype
matrix_2d.dtype
#conocer el tamaño de una matriz
matrix_1d.size
#conocer la forma de una matriz
matrix_1d.shape
#matriz traspuesta
matriz_traspuesta= matrix_2d.reshape(3,2)
#extraer valores de una matriz
a = np.array([(1,2,3,4),(3,4,5,6)])
a[0,2] # esto imprime 3
a[0:,2] # imprie [3 5] genera la fila

#minimo, maximo, suma, raiz cuadrada, desviacion estandar
b = np.array([2,4,8])
b.min()
b.max()
b.sum()
np.sqrt(b)
np.std(b)


# %%
