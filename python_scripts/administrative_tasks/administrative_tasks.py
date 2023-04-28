import zipfile
from pathlib import Path

import pywinauto
from PIL import Image


def delete_temp_files(route):
    for file_name in os.listdir(route):
        if file_name.startswith('temp_'):
            os.remove(os.path.join(route, file_name))
    print('Archivos temporales eliminados.')


def compress_files(route, extension):
    with zipfile.ZipFile('archivo_comprimido.zip', 'w', zipfile.ZIP_DEFLATED) as archivo_zip:
        for file_name in os.listdir(route):
            if file_name.endswith(extension):
                archivo_zip.write(os.path.join(route, file_name), file_name)
    print(f'Archivos con extension {extension} comprimidos.')


def convert_file(s, s1):
    path_to_convert = './files/example.docx'
    path_to_result = f'./files/{Path(path_to_convert).stem}.pdf'
    # Abre Microsoft Word
    app = pywinauto.application.Application()
    app.start('WINWORD.EXE')
    main_win = app.window(title='Documento1 - Word')
    main_win.wait('visible', timeout=20)
    # Abre el archivo a convertir
    main_win.menu_select('Archivo -> Abrir')
    dialog_win = app.window(title='Abrir')
    dialog_win.wait('visible', timeout=20)
    dialog_win.FileNameEdit.type_keys(path_to_convert)
    dialog_win.Abrir.click()
    # Convierte el archivo a PDF
    main_win.menu_select('Archivo -> Guardar como')
    dialog_win = app.window(title='Guardar como')
    dialog_win.wait('visible', timeout=20)
    dialog_win.FileTypeComboBox.select('PDF (*.pdf)')
    dialog_win.FileNameEdit.type_keys(path_to_result)
    dialog_win.Guardar.click()
    # Espera unos segundos para que se complete la conversión
    app.top_window().set_focus()
    app.top_window().type_keys('%{F4}')
    app.top_window().type_keys('{ENTER}')


def convert_images(route, format):
    for file_name in os.listdir(route):
        if file_name.endswith('.jpg'):
            with Image.open(os.path.join(route, file_name)) as image:
                image.save(os.path.join(route, file_name.replace('.jpg', format)))
    print(f'Imágenes convertidas a formato {format}.')


delete_temp_files('./files')
compress_files('./files', '.docx')
convert_file('./files', '.pdf')
convert_images('./files', '.png')
