def validasalir(accion):
    try:
        return (str(accion) != 'exit' and str(accion) != 'salir')
    except:
        print("fallo")
        return False

def validaPalindromo(palabra):
    valida = ("" if palabra.lower().replace(" ","")[::1] == palabra.lower().replace(" ","")[::-1] else "no")
    return "la frase o palabra " + palabra + " " + valida + "es palindromo"