import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('VentasCiudad.csv')
print(df)

# Definir una variable para guardar la cantidad  ventas por ciudad
ventasXciudad = df.groupby('Ciudad')['ValorVenta'].count()
print(ventasXciudad)

#Crear un grafico de columnas

plt.figure(figsize=(5, 4))
plt.bar(ventasXciudad.index, ventasXciudad.values)
plt.title('Ventas por ciudad')
plt.xlabel('Ciudades')
plt.ylabel('Ventas en Millones')

# Crear un total de ventas x producto


ventasXproducto = df.groupby('Producto')['ValorVenta'].sum()
print("\nTotal de ventas por producto:")
print(ventasXproducto)

plt.figure(figsize=(6, 4))
plt.bar(ventasXproducto.index, ventasXproducto.values, color='orange')
plt.title('Total de Ventas por Producto')
plt.xlabel('Producto')
plt.ylabel('Ventas en Millones')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()