import time

import facebook

# Tokens de acceso
access_token = ''
page_id = ''

# Inicialización de la API
graph = facebook.GraphAPI(access_token)

# Detales de la publicación
post_details = {
    'message': 'Este es un mensaje de prueba',
    'link': 'https://www.facebook.com/groups/prueba-de-facebook-group/',
    'picture': 'https://www.facebook.com/groups/prueba-de-facebook-group/'
}

# Programar la  publicación
while True:
    if time.strftime('%H:%M:%S') == '00:00:00':
        graph.put_object(parent_object=page_id, connection_name='feed', **post_details)
        print('Publicación programada')
    time.sleep(1)
