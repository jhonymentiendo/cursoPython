import funciones

def run():
    bandera_salir=True
    menu="""
ingresa una frase que sea palindromo
[exit/salir] - salir

>>"""
    while(bandera_salir):
        dato = input(menu)
        bandera_salir = funciones.validasalir(dato)
        if(bandera_salir):
            print(funciones.validaPalindromo(dato))

if __name__ == '__main__':
    run()