"""Enunciado: escriba un programa que simule la conexión de un usuario a un sitio web para el que ya
se ha registrado, solo con su dirección de correo electrónico (la gestión de una contraseña está fuera
del alcance de esta sección). Este programa debe ofrecer la posibilidad al usuario de introducir una 
dirección de correo electrónico, y mostrará diferentes mensajes de error en función de la cadena
introducida. El programa debe continuar si el correo electrónico indicado tiene un formato
incorrecto y finalizar si no se reconoce el correo electrónico, ya que se podría tratar de
un ciberataque. Importante: el método que analiza la cadena de caracteres no debe devolver
ningún valor.

Comportamiento esperado: la ejecución del programa en una consola se debe desarrollar de la
siguiente manera:
vicente: $ python exceptions.py 
--> 
'' es una entrada incorrecta. Introduzca una dirección de correo 
electrónico 
--> t 
Una dirección de correo electrónico debe tener el formato xxx@xxx.xx 
--> t@t.t 
Cuenta bloqueada a causa de un ataque 
vicente: $ python exceptions.py 
--> vicente@eni.es 
¡Bienvenido Vicente! 
Requisitos previos:

Puede usar el módulo de expresiones regulares ofrecido por Python, para determinar si la cadena
de caracteres tiene el formato correcto. Para hacerlo, importe el módulo "re" (import re) y utilice
el método search() de la siguiente manera: re.search(". * @. * \ .. *", s). Esta línea devolverá None
si la cadena s no tiene el formato de una dirección de correo electrónico.

El método input(’->’) le permite recopilar una cadena de caracteres escrita en la entrada estándar
(la consola, en este caso)."""

import re

class Correo(): #clase correo con un solo atributo  correo
    def __init__(self,correo):
        self.correo = correo
    def validar(self):   #metodo que valida si el correo introducido es correcto o incorrecto
        validacion = re.search(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", self.correo) #metodo re que busca en el self.correo la arroba
        correoIntroducido = input("-> ")#pedimos que introduzca un correo
        if validacion: # si el correo contiene una arroba, continuamos
            if correoIntroducido == self.correo: #si el correo coincide pues terminamos
                nombre = ""
                for i in self.correo:
                    if i != "@":
                        nombre += i 
                    else:
                        break
                nombre = nombre.capitalize()
                return "Bienvenido {}!!".format(nombre)
            else: #si no coincide enviamos una excepcion de que la cuenta ha sido bloqueda
                raise Exception("Cuenta bloqueada a causa de un ataque")
        else: #si el correo no contiene una arroba, enciamos "correo incorrecto"
            return ("Correo Incorrecto")

correo1=Correo("joseantonio@gmail.com")#creamos los objetod de la clase correo
correo2 = Correo("alejandro@gmail.com")
correo3 = Correo("jacobo@gmail.com")
correos = [correo1, correo2, correo3]#creamos una lista con los correos
for i in correos:
    print(i.validar())#los validamos

