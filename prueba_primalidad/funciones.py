def es_primo(num):
    for n in range(2,int(num)):
        if num % n == 0:
            return False
    return True


def imprimePrimos():
    limite = pidenumero("hasta que numero vamos a imprimir los primos:\n>>")
    for n in range(1,limite):
        if es_primo(n):
            print(n)


def pidenumero(mensaje):
    try:
        return int(input(mensaje))
    except:
        return pidenumero("Fallo al pedir el dato, intenta otra vez\n\n"+mensaje)