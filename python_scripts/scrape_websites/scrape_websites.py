import requests
from bs4 import BeautifulSoup

# Pedimos la url del sitio web
url = input("Introduce la url del sitio web: ")

# Hacemos una petición a la url y parseamos el contenido HTML con Beautiful Soup
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

# Extraemos los datos de interés
enlaces = [enlace.get("href") for enlace in soup.find_all("a")]

# Mostramos los enlaces encontrados
for enlace in enlaces:
    print(enlace)
