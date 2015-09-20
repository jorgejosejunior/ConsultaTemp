__author__ = 'Jorge Jose'
#-*-encoding: utf8 -*-
"""
Primeiro desafio: conseguir instalar o modulo sud no python27
na instalacao nao eh inclusa este modulo quando tentei compilar
o codigo deu erro pedindo o sud ai encontrei na net um comando
para o cmd do windows que baixou e instalou o sud.
Problema resolvido
"""

from suds.client import Client
import xml.dom.minidom
import re
def entradaTemp(tF):
    print '%s F = %s C\n '% (tF, client2.service.FahrenheitToCelsius(tF))
    #print '%s graus em Celsius e = %s Fahrenheit' % (tC, client.service.CelsiusToFahrenheit(tC))

wsdlFile = 'http://www.webservicex.net/globalweather.asmx?WSDL'
#wsdlFile = 'http://www.w3schools.com/webservices/tempconvert.asmx?WSDL'
#serv_url = 'http://www.w3schools.com/webservices/tempconvert.asmx'
client = Client(wsdlFile)
#print client
#Um programa basico seria fazer tres consultas ao site para converter
#tres temperaturas requeridas pelo usuario. Como poderiamos fazer
#isso? Pederiamos utilizar o laco de repeticao for que realizasse
#tres lacos cada um com uma entrada de temperatura diferente.
#print 'Temperatura em Fortaleza = %s '%(client.service.GetCitiesByCountry("Brazil"))
#print client.service.GetWeather("Fortaleza Aeropor-To","Brazil")

#for i in range(0,2):
#    Temperatura = raw_input('Por favor digite a temperatura em Celsius a ser convertida: ')
#    entradaTemp(Temperatura)
#doc.toxml print (client.service.GetWeather("Fortaleza Aeropor-To","Brazil"))
#rXml = client.service.GetWeather("Fortaleza Aeropor-To","Brazil")
#print rXml
with open("este.xml", "w") as arq:
    arq.write(client.service.GetWeather("Fortaleza Aeropor-To","Brazil"))
    arq.close()

"""
    Aqui esta o fim do acesso ao primeiro webservice
    No primeiro webservice eu coletoo valor da temperatura a
    ser convertido no segundo webservice
"""
arq  = open("este.xml",'r+')
arq.seek(1)
arq.flush()
arq.write("?xml version='1.0'  encoding='utf-8'")
arq.close()

#Acesso ao segundo webservice
DOMTree = xml.dom.minidom.parse("este.xml")
collection = DOMTree.documentElement
print "***********Temperatura em Fortaleza WebService 1********"
Temperatura =collection.getElementsByTagName('Temperature')[0]
print "Temperatura: %s" % Temperatura.childNodes[0].data
#print Temperatura.childNodes[0].data
ValorFarenheit = Temperatura.childNodes[0].data
TempFarenheit = ValorFarenheit[1:3]
#print TempFarenheit

wsdlFile2 = 'http://www.w3schools.com/webservices/tempconvert.asmx?WSDL'
client2 = Client(wsdlFile2)
print '*******Temperatura Convertida no WebService 2***********'
entradaTemp(str(TempFarenheit))
