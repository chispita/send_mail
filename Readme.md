# Envío de correos masivos mediante programa en python

**Carlos Val Gascón * carlos.val@bifi.es**

**System Administrator**

## Introducción
El nucleo del programa es el programa send_mail.py que básicamente
realiza el envio de correos a partir de diferentes bibliotecas de 
python: SMTP, MIMEText, parseraddr, formataddr.

# Archivos de configuración
Para realizar una envío de correo podremos utilizar uno de estos dos 
ejemplos:

- send_correo.py (envía correos sin formato).
- send_correo_html.py (envía los correos con formato).

El último ejemplo contiene una parte en la que podemos pasarle un fichero
conteniendo las direcciones de correo electrónico en cada línea y un correo  
a todos ellos.
