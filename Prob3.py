import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Cargar los datos desde el archivo Excel
datos = pd.read_excel("Las_500_de_Expansion_2022.xlsx", sheet_name='Base')

# Seleccionar las variables explicativas (X) y la variable objetivo (y)
variables_explicativas = ['Liquidez2021', 'Apalan2021', 'Solvencia2021', 'VtasXEmp2021', 'ROE2021']
variable_objetivo = 'MargenNeto2021'

X = datos[variables_explicativas]
y = datos[variable_objetivo]

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar el modelo de regresión lineal
modelo = LinearRegression()

# Entrenar el modelo con los datos de entrenamiento
modelo.fit(X_train, y_train)

# Evaluar el modelo con los datos de prueba
y_pred = modelo.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Error cuadrático medio (MSE):", mse)

# Calcular las medias de las variables financieras
medias_variables_financieras = datos[['Liquidez2021', 'Apalan2021', 'Solvencia2021', 'VtasXEmp2021', 'ROE2021']].mean()

# Crear DataFrame con las medias como valores
nuevos_datos = pd.DataFrame({
    'Liquidez2021': [medias_variables_financieras['Liquidez2021']],
    'Apalan2021': [medias_variables_financieras['Apalan2021']],
    'Solvencia2021': [medias_variables_financieras['Solvencia2021']],
    'VtasXEmp2021': [medias_variables_financieras['VtasXEmp2021']],
    'ROE2021': [medias_variables_financieras['ROE2021']]
})

prediccion = modelo.predict(nuevos_datos)
print("Predicción de Margen Neto:", prediccion)
