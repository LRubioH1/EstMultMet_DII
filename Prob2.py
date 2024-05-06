import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo Excel
datos = pd.read_excel("Las_500_de_Expansion_2022.xlsx", sheet_name='Base')

# Seleccionar variables financieras
datos_financieros = datos[['MargenOper2021', 'MargenNeto2021', 'Liquidez2021', 'Apalan2021', 'Solvencia2021', 'VtasXEmp2021', 'ROE2021']]

# Escalar los datos financieros
scaler = StandardScaler()
datos_financieros_escalados = scaler.fit_transform(datos_financieros)

# Seleccionar variables cualitativas y realizar codificación one-hot
variables_cualitativas = datos[['Oficinas', 'Pais_de_origen', 'Sector']]
onehot = OneHotEncoder()
variables_cualitativas_codificadas = onehot.fit_transform(variables_cualitativas).toarray()

# Combinar datos financieros escalados con variables cualitativas codificadas
datos_combinados = np.hstack((datos_financieros_escalados, variables_cualitativas_codificadas))

# Entrenar el modelo de clustering con datos combinados
kmeans = KMeans(n_clusters=5)
kmeans.fit(datos_combinados)

# Agregar las etiquetas de clusters al DataFrame original
datos['cluster'] = kmeans.labels_

# Seleccionar solo columnas numéricas para calcular la media
datos_numericos = datos.select_dtypes(include=[np.number])

# Interpretación de resultados
resultados = datos_numericos.groupby('cluster').mean()
print(resultados)


# Seleccionar las variables numéricas relevantes para visualización
variables_visualizacion = ['MargenOper2021', 'MargenNeto2021', 'Liquidez2021', 'Apalan2021', 'Solvencia2021', 'VtasXEmp2021', 'ROE2021', 'cluster']

# Filtrar el DataFrame para incluir solo las variables relevantes
datos_visualizacion = datos[variables_visualizacion]

# Calcular la matriz de correlación
matriz_correlacion = datos_visualizacion.corr()

# Visualizar la matriz de correlación como un mapa de calor
plt.figure(figsize=(10, 8))
sns.heatmap(matriz_correlacion, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Matriz de Correlación de Variables con Clústeres')
plt.show()
