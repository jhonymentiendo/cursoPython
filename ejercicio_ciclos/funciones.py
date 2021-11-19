
def ejercicioWile():
    numerobase=pidenumero("dame un numero base:\n>>")
    contador=0
    limite = pidenumero("dame un numero limite:\n>>")
    while(numerobase**contador<limite):
        print( str(numerobase) + " elevado a la " + str(contador) + " es : " + str(numerobase**contador))
        contador+=1

def ejercicioFor():
    for n in range(0,10):
        print(str(n+1))


def pidenumero(mensaje):
    try:
        return int(input(mensaje))
    except:
        return pidenumero("Fallo al pedir el dato, intenta otra vez\n\n"+mensaje)