import pandas as pd

# Carga los datos desde el archivo Excel (reemplaza con tu ruta y nombre de archivo)
df = pd.read_excel('Las_500_de_Expansion_2022.xlsx', sheet_name='Base')

# Columnas de interés
columnas_interes = ['Sector', 'MargenOper2021', 'MargenNeto2021', 'Liquidez2021', 'Apalan2021', 'Solvencia2021', 'VtasXEmp2021', 'ROE2021']
df = df[columnas_interes]

# Calcula la media y desviación estándar por sector
media_por_sector = df.groupby('Sector').mean()
desvEst_por_sector = df.groupby('Sector').std()

pd.set_option('display.max_columns', None)

media_por_sector.fillna(0, inplace=True)
desvEst_por_sector.fillna(0, inplace=True)

# Muestra la tabla de medias por sector
print("Tabla de medias por sector:")
print(media_por_sector)


# Muestra la tabla de desviación estándar por sector
print("Tabla de desviaciones estándar por sector:")
print(desvEst_por_sector)



# Convertir DataFrame a una tabla HTML
tablaM_html = media_por_sector.to_html()
tablaDE_html = desvEst_por_sector.to_html()

# Guardar la tabla HTML en un archivo
with open('tabla_medias_por_sector.html', 'w') as f:
    f.write(tablaM_html)
with open('tabla_medias_por_sector.html', 'w') as f:
    f.write(tablaDE_html)

# Imprimir la ruta del archivo
print("Se ha generado la tabla HTML: tabla_medias_por_sector.html")
print("Se ha generado la tabla HTML: tabla_desvEst_por_sector.html")
