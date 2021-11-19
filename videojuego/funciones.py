import random


def iniciaJuego():
    bandera_salida=True
    limite = pideNumero("hasta que numero quieres el limite de adivinar:")
    numero_ganador = random.randint(1,limite)
    while(bandera_salida):
        if bandera_salida:
            numero = pideNumero("adivina:")
            if numero == numero_ganador:
                bandera_salida=False
            elif numero < numero_ganador:
                print("mas")
            elif numero > numero_ganador:
                print("menos")

def determinaSalir(dato):
    return dato!="exit" and dato !="salir"


def pideNumero(mensaje):
    try:
        return int(input(mensaje + "\n>>"))
    except:
        pideNumero("fallo al obtener el dato, ingresa numero valido\n\n"+mensaje)