import matplotlib.pyplot as plt
import numpy as np

# Datos para los histogramas
data1 = np.random.randn(1000)
data2 = np.random.randn(1000)
data3 = np.random.randn(1000)
data4 = np.random.randn(1000)

# Crear una figura y ejes
fig, axs = plt.subplots(2, 2)

# Graficar los histogramas en cada eje
axs[0, 0].hist(data1, bins=30, color='blue', alpha=0.7)
axs[0, 0].set_title('Histograma 1')
axs[0, 0].set_xlabel('Notas 1')
axs[0, 0].set_ylabel('Frecuencia')

axs[0, 1].hist(data2, bins=30, color='green', alpha=0.7)
axs[0, 1].set_title('Histograma 2')
axs[0, 0].set_xlabel('Notas 2')
axs[0, 0].set_ylabel('Frecuencia')

axs[1, 0].hist(data3, bins=30, color='red', alpha=0.7)
axs[1, 0].set_title('Histograma 3')
axs[0, 0].set_xlabel('Notas 3')
axs[0, 0].set_ylabel('Frecuencia')

axs[1, 1].hist(data4, bins=30, color='purple', alpha=0.7)
axs[1, 1].set_title('Histograma 4')
axs[0, 0].set_xlabel('Notas 4')
axs[0, 0].set_ylabel('Frecuencia')

# Ajustar el espaciado entre subfiguras
plt.tight_layout()

# Mostrar la figura
plt.show()
