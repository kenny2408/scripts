import smtplib

# Configurar la información del servidor SMTP y el remitente
smtp_server = "smtp.gmail.com"
smtp_port = 587  # Este es el puerto para gmail. Otros proveedores de correo pueden usar otros puertos
smtp_user = "tu_correo@gmail.com"
smtp_password = "tu_contraseña"
from_addr = smtp_user

# Configurar la lista de destinatarios
to_addr = ["destinatario1@ejemplo.com", "destinatario2@ejemplo.com", "destinatario3@ejemplo.com"]

# Configurar el correo electrónico
subject = "Correo Electrónico Masivo de Prueba"
body = "Hola! \n\n Esta es una prueba de envío de correo electrónico masivo."

# Combinar el correo electrónico en un mensaje
message = f"Subject: {subject}\n\n{body}"

# Configurar la conexión con el servidor SMTP

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_user, smtp_password)

    # Enviar correos electrónicos a la lista de destinatarios
    server.sendmail(from_addr, to_addr, message)

print("Correos electrónicos enviados correctamente.")
