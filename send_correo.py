#!/usr/bin/python
# -*- coding: utf-8 -*-

import send_mail

def bold(msg):
    return u'\033[1m%s\033[0m' % msg

print "Envio de correos"

subject = u'¡Ahora puedes colaborar con la gripe!'

body = u"""
\033[1m' + 'Hello'
\033[1mHolita\033[0mAdios
\nSi la meteorología es capaz de predecir el comportamiento de tormentas y huracanes, con datos suficientes y un modelo adecuado la ciencia también puede llegar a anticipar la evolución de una epidemia. Eso nos ayudaría a reducir sus efectos y a mejorar las respuestas del sistema público de salud ante la enfermedad.
\nPor esta razón, investigadores de la Universidad de Zaragoza y la Fundación Ibercivis pusieron en marcha el proyecto de participación ciudadana en ciencia GripeNet. La iniciativa realiza un seguimiento de los niveles de incidencia del virus de la gripe en España mediante la colaboración de voluntarios que, de forma anónima y a través de internet, informan regularmente a los investigadores de su estado de salud.
\nGripeNet se presentará de primera mano \033el próximo lunes 25 de noviembre, a las 11:00 horas
Salón de Actos del edificio central del CSIC en Madrid (c/ Serrano, 117)\033.
\nDesde ibercivis se ha organizado el acto, un sólido programa que para dar respuesta
\nSi quieres colaborar en el estudio de la gripe, ¡no lo dudes y participa!
\n- Visita la web GripenNet.es y regístrate como voluntario
\n- Ven a la presentación: para asistir solo tienes que inscribirte.
\nAquí puedes consultar el programa para el día 25 Flyer Gripenet Desde ibercivis se ha organizado el acto, un sólido programa que para cubrir todos los aspectos.
\nTe esperamos. #Todos con la ciencia #SomosCiencia

\n\nMil gracias
\n -- firma:
\nEl equipo de Ibercivis
\n@Ibercivis"
"""

body  =u"""
<p style="border:0px none;font-family:'helvetica neue',Helvetica,Arial,Verdana,sans-serif;font-size:11.818181991577148px;margin:0px;padding:0.5em 0px;vertical-align:baseline;color:rgb(68,68,68);line-height:16.363636016845703px">

- Visita la web&nbsp;<a href="http://www.gripenet.es/" style="border:0px none;font-family:inherit;font-size:11.818181991577148px;font-style:inherit;font-weight:inherit;margin:0px;padding:0px;vertical-align:baseline;color:rgb(10,188,229);text-decoration:none" target="_blank">GripenNet.es</a>&nbsp;y regístrate como voluntario</p>
"""



#fileSource= 'email_list'
#fsrc = open(fileSource, "r")
#for line in fsrc:
#   line =line[:-1]
#   print line
#   send_mail.send("info@ibercivis.es", line, subject, body)
#fsrc.close()

send_mail.send("info@ibercivis.es", "carlos.val@bifi.es", subject, body)

