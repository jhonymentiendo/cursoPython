import funciones

def run():
    mi_diccionario = {
       'key_1' : 1,
       'key_2' : 2,
       'key_3' : 3,
       'key_4' : 4, 
    }
    for key,value in mi_diccionario.items():
        print(key + " - " + str(value))




if __name__ == '__main__':
    run()