#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address
me = "info@ibercivis.es"
#???? Tendria que ir abajo
you = "frasanz@bifi.es"

# Create message container - the correct MIME type is multipart/alternative.
# Create the body of the message (a plain-text and an HTML version).
# Text in plain text
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"

# Text in html Format
html = """\
<html>
<head>
¡Ahora puedes colaborar con la gripe!
</head>
<p>
Si la meteorología es capaz de predecir el comportamiento de tormentas y huracanes, con datos suficientes y un modelo adecuado la ciencia también puede llegar a anticipar la evolución de una epidemia. Eso nos ayudaría a reducir sus efectos y a mejorar las respuestas del sistema público de salud ante la enfermedad.
<p>
Por esta razón, investigadores de la Universidad de Zaragoza y la Fundación Ibercivis pusieron en marcha el proyecto de participación ciudadana en ciencia GripeNet. La iniciativa realiza un seguimiento de los niveles de incidencia del virus de la gripe en España mediante la colaboración de voluntarios que, de forma anónima y a través de internet, informan regularmente a los investigadores de su estado de salud.
<p>
Desde la Fundación Ibercivis se ha organizado el acto de presentación de GripeNet el<b>lunes 25 de noviembre, a las 11:00 horas
Salón de Actos del edificio central del CSIC en Madrid (c/ Serrano, 117).</b>
<p>Si quieres colaborar en el estudio de la gripe, ¡no lo dudes y participa!
<ul>
    <li>Visita la web <a href='https://www.gripenet.es'>GripenNet</a> y regístrate como voluntario</li>
    <li>Ven a la presentación: para asistir solo tienes que <a href='http://www.reunalia.com/6813998'>inscribirte</a>.</li>
</ul>
<p>Aquí puedes consultar el programa para el día 25 <a href='http://www.ibercivis.es/wp-content/uploads/2013/10/Flyer-Gripenet-Web.pdf '>Flyer Gripenet</a>.
<p>Te esperamos: <a href="https://twitter.com/intent/user?screen_name=Todos con la ciencia">@TodosConLaCiencia</a> <a href="https://twitter.com/intent/user?screen_name=SomosCiencia">@SomosCiencia</a>

<p>Gracias
<p>El equipo de Ibercivis <a href="https://twitter.com/intent/user?screen_name=Ibercivis">@Ibercivis</a>
</body>
</html>
"""

# Send the message via local SMTP server.
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.



fileSource= 'emails2'
fsrc = open(fileSource, "r")
for line in fsrc:
# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
    s = smtplib.SMTP('smtp.ibercivis.es')
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "¡Ahora puedes colaborar con la gripe!i 9933"
    msg['From'] = me
# Record the MIME types of both parts - text/plain and text/html.
    part2 = MIMEText(html, 'html')

    msg.attach(part2)

    line =line[:-1]
    msg['To'] = line
    print msg.as_string()
    s.sendmail(me, line, msg.as_string())
    msg = None
fsrc.close()

#s.sendmail(me, you, msg.as_string())
s.quit()
