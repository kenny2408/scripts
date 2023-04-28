import os
import shutil

# Obtener la lista de todos los archivos de texto en la carpeta de origen
path = 'ruta_de_la_carpeta_de_origen'
files = [f for f in os.listdir(path) if f.endswith('.txt')]
# Crear la carpeta de destino si no existe
os.makedirs('ruta_de_la_carpeta_de_destino', exist_ok=True)
# Iterar sobre todos los archivos de texto en la carpeta de origen y realizar los cambios necesarios
for file_name in files:
    with open(os.path.join(path, file_name), 'r') as f:
        data = f.read().replace('original', 'modificado')
    new_file_name = file_name.replace('.txt', '_mod.txt')
    with open(os.path.join('ruta_de_la_carpeta_de_destino', new_file_name), 'w') as f:
        f.write(data)
# Copiar un archivo específico en la carpeta de destino
shutil.copy2('ruta_del_archivo_original', 'ruta_de_la_carpeta_de_destino/ruta_del_archivo_copiado')
