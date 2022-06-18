import random
from pyfiglet import Figlet


def funcion_figlet():
    figlet=Figlet()
    fuente=input("Ingrese la fuente a utilizar: ")
    texto=input("Ingrese texto: ")
    if (fuente in figlet.getFonts()):
        figlet.setFont(font=fuente)
    else:
        fuente= random.choice(figlet.getFonts())
        figlet.setFont(font=fuente)
    print(figlet.renderText(texto))
funcion_figlet()