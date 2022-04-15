# ¿que son?
# conjutno de linea de codigo agruoadas (Bloque de codigo) que funcionan como una unidad realizando una tarea 
# las funciones en python pueden devolver valores.
# las funciones en python pueden tener parametros/argumentos

# Utilidad
# Reutiluzacion de codigo #

#sintaxis "def nombre_funcion():
#   instruciones de la funcion
#   return(opcional)

#sintaxis "def nombre_funcion(parametros):
#   instruciones de la funcion
#   return(opcional)


# ejecucion :

#nombre_funcion()
#nombre_funcion(parametro)

#ejemplo:

def mensaje(): #declaracion de la funcion

    print("hola mundo") #cuerpo

# llamar a la funcion

mensaje() #llamada de la funcion

#ejercicio

def suma_v1():
    num1=5
    num2=4
    print(num1+num2)

suma_v1()


def suma_v2(num1,num2):
    print(num1+num2)

suma_v2(5,7)
suma_v2(5,9)
suma_v2(5,-9)

def suma_v3(num1, num2):
    resultado = num1 + num2
    return resultado

print(suma_v3(4 , 5))

no_aprobador = 10
aspirante = 24
resultado = no_aprobador * 100 / aspirante  

print(round(resultado)  , "%")
