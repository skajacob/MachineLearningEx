from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
fig = plt.figure()
# Tipo de figura
ax = fig.gca(projection='3d')
# Datos
X = np.arange(-4, 4, 0.3)
Y = np.arange(-4, 4, 0.3)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
# Graficamos o trazamos la superficie
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='jet')
# Personalizamos el ejex z
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
# Agregamos una barra de colores para que asigne valores a los colores.
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()