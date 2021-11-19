valor_dolar_a_peso = 20.67
valor_peso_a_dolar = 0.048
def defineSalida(accion):
    try:
        return (str(accion) != 'exit' and str(accion) != 'salir')
    except:
        print("fallo")
        return False

def presentaresp(cantidad,moneda_origen,cantidad_convert,moneda_destino):
    print("\n\n-> " + str(cantidad) + " de "+ str(moneda_origen) +" equivale a " + str(cantidad_convert) + " " + str(moneda_destino) +" \n\n")

def defineconversion(accion,cantidad):
    if(int(accion) == 1):
        cantidad_convert = convierte(cantidad,valor_peso_a_dolar)
        presentaresp(cantidad,"peso mexicano",cantidad_convert,"dolares")
    elif(int(accion) == 2):
        cantidad_convert = convierte(cantidad,valor_dolar_a_peso)
        presentaresp(cantidad,"dolares",cantidad_convert,"peso mexicano")
    else:
        print("no hay accion para " + accion)

def convierte(cantidad,valor_conversion):
    return int(cantidad) * valor_conversion

def pidenumero(mensaje):
    try:
        return int(input(mensaje))
    except:
        return pidenumero("Fallo al pedir el dato, intenta otra vez\n\n"+mensaje)