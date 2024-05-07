import pandas as pd

# Cargar los datos desde el archivo Excel 
df = pd.read_excel('Las_500_de_Expansion_2022.xlsx', sheet_name='Base')

# Definir las columnas de interés
columnas_interes = ['Sector', 'MargenOper2021', 'MargenNeto2021', 'Liquidez2021', 'Apalan2021', 'Solvencia2021', 'VtasXEmp2021', 'ROE2021']
df = df[columnas_interes]

# Agrupar los datos por sector
grupo_sector = df.groupby('Sector')

# Calcular estadísticas descriptivas para cada variable financiera
estadisticas_por_sector = grupo_sector.agg({
    'MargenOper2021': ['mean', 'median', 'std', 'min', 'max'],
    'MargenNeto2021': ['mean', 'median', 'std', 'min', 'max'],
    'Liquidez2021': ['mean', 'median', 'std', 'min', 'max'],
    'Apalan2021': ['mean', 'median', 'std', 'min', 'max'],
    'Solvencia2021': ['mean', 'median', 'std', 'min', 'max'],
    'VtasXEmp2021': ['mean', 'median', 'std', 'min', 'max'],
    'ROE2021': ['mean', 'median', 'std', 'min', 'max']
})

pd.set_option('display.max_columns', None)


# Tabla con las estadísticas descriptivas
print(estadisticas_por_sector)

estadisticas_por_sector.fillna(0, inplace=True)

estadisticas_por_sector_hml = estadisticas_por_sector.to_html()
with open('estadisticas_por_sector.html', 'w') as f:
    f.write(estadisticas_por_sector_hml)
    
print("Se ha generado la tabla HTML: estadisticas_por_sector.html")