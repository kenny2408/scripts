import pandas as pd

# lee un archivo CSV y carga los datos en un DataFrame
data = pd.read_csv("ruta_del_archivo.csv", usecols=['columna1', 'columna2'], dtype={'columna1': int, 'columna2': str})
# filtra los datos por una columna específica
data_filtrada = data[data['nombre_columna'] == 'valor']
# ordena los datos por una columna específica
data_ordenada = data.sort_values(by='nombre_columna')
# agrupa los datos por una columna específica y calcula la suma
data_agrupada = data.groupby('nombre_columna').sum()
# crea un nuevo archivo CSV con los datos filtrados
data_filtrada.to_csv("ruta_del_archivo_filtrado.csv", index=False)
# crea un nuevo archivo de Excel con los datos ordenados y agrupados
with pd.ExcelWriter("ruta_del_archivo_procesado.xlsx") as writer:
    data_ordenada.to_excel(writer, sheet_name='Ordenado')
    data_agrupada.to_excel(writer, sheet_name='Agrupado')
