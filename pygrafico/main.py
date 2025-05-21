import pandas as pd
import matplotlib.pyplot as plt

# Datos

estudiantes = ['Karen','Santiago','Isaac','Brayan','Sofia','Camilo','esteban']
definitivas = [3.36, 3.53, 3.64, 3.00, 4.17, 3.20, 3.36]

plt.figure(figsize=(8, 8))
plt.pie(definitivas, labels=estudiantes, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)

# Añadir un titulo

plt.title('Notas definitivas de los estudiantes (Gráfico Circular)', fontsize=14)

plt.axis('equal')
plt.show()