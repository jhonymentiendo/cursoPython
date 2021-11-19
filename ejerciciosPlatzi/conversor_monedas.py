import funciones
bandera_continua = True
menu = """
Ingresa la conversión que deseas hacer:\n
[1] pesos a dolares:
[2] dolares a pesos:

[exit/salir] salir: 
>>
"""

while(bandera_continua):
    try:
        accion = input(menu)
        bandera_continua = funciones.defineSalida(accion)
        if bandera_continua == True:
            cantidad = funciones.pidenumero("Ingresa la cantidad:\n>>")
            funciones.defineconversion(accion,cantidad)
    except:
        print("**********E R R O R************")