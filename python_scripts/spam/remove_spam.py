from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Lista de comentarios de ejemplo
comments = [
    "This is a comment",
    "This is another comment",
    "This is yet another comment"
]

# Carga las stopwords en una lista
stop_words = set(stopwords.words('spanish'))

# Crea una instancia de lematizador
lemmatizer = WordNetLemmatizer()


# Define los algoritmos de detección de spam y ofensas
def is_spam(words):
    # Tokeniza el comentario
    tokens = word_tokenize(words)
    # Elimina las stopwords
    filtered_tokens = [w for w in tokens if not w in stop_words]
    # Aplica el lematizador
    lemmatized_tokens = [lemmatizer.lemmatize(w) for w in filtered_tokens]
    # Comprueba si el comentario es spam
    return "spam" in lemmatized_tokens


def is_offensive(words):
    # Tokeniza el comentario
    tokens = word_tokenize(words)
    # Elimina las stopwords
    filtered_tokens = [w for w in tokens if not w in stop_words]
    # Aplica el lematizador
    lemmatized_tokens = [lemmatizer.lemmatize(w) for w in filtered_tokens]
    # Comprueba si el comentario es ofensivo
    return "offensive" in lemmatized_tokens


# Clasifica los comentarios
for comment in comments:
    words = [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(comment) if word.lower() not in stop_words]
    is_spam_comment = is_spam(words)
    is_offensive_comment = is_offensive(words)
    if not is_spam_comment and not is_offensive_comment:
        classifield_comments.append(comment)

# Elimina los comentarios clasificados como spam y ofensivos utilizando la API de la red social
for classified_comment in classifield_comments:
    social_network.remove_comment(classified_comment)
