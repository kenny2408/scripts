import time

import facebook

# Tokens de acceso
access_token = ''
instagram_account_id = ''
page_id = ''

# Autenticación con facebook
graph = facebook.GraphAPI(access_token)

# Crear una publicación en la herramienta de Facebook Creator Studio
post_details = {
    'caption': 'Esto es una publicación de prueba',
    'media_url': 'https://www.example.com/image.jpg',
    'access_token': access_token
}
post = graph.post(f'{instagram_account_id}/media', post_details)

# Programar la publicación
while True:
    current_time = time.localtime("%H:%M:%S")
    if current_time == '12:00:00':  # Programar la publicación para las 12:00 PM
        params = {
            'creation_id': post['id'],
            'access_token': access_token
        }
        graph.post(f'{instagram_account_id}/media_publish', params=params)
        print('Publicación programada')
    time.sleep(1)
