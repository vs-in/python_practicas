# ---> Funciones en Python 

# Una funcion tiene un nombre que la identifica y puede recibir 
# argumentos o parametros de entrada, realizar operaciones basadas 
# en esos argumentos, y devolver un valor de salida. 

#-------------
"""
---> Estructura de las Funciones <--- 

def restar (a,b):   #--> Definimos la funcion
    r = a - b 
    print(f"Restar: {r}")  #--> El proceso de la funcion


restar(4,1)   #--> Invocamos la funcion 

#---> Donde def es la PALABRA RESERVADA para llamar a la fucnion :
#---> Donde (a,b) son llamados PARAMETROS (pueden ser opcionales) :
#Los cuales son las variables que ponemos cuando se define una funcion
--> Se puede saber tambien que el PARAMETRO puede tener dos opciones: 
#Paso por valor: si hay un valor como un int,float,booleano,etc 
#Paso por referencia:
#---> Donde (4,1) son llamados ARGUMENTOS :
#Los cuales son los valores que le enviamos a la funcion cuando la ejecutamos
"""

#-------------


"""
Si usamos un parámetro pasado por VALOR, se creará una copia local de la variable,
lo que implica que cualquier modificación sobre la misma no tendrá efecto
sobre la original

--> EJEMPLO

x = 10
def funcion(entrada):
    entrada = 0
funcion(x)

print(x) # 10

->Iniciamos la x a 10 y se la pasamos a funcion(). Dentro de la función hacemos que la variable valga 0. 
Dado que Python trata a los int como pasados por valor, dentro de la función se crea una copia local de x, por lo que la variable original no es modificada.
Con una variable pasada como REFERENCIA, se actuará directamente
sobre la variable pasada, por lo que las modificaciones afectarán
a la variable original
"""

#-------------
# ---> Ejemplo de funcion : -->"Calcular Area Circulo"<---


#--> Definicion de la funcion 
"""
def calcular_area(radio):
    PI = 3.1416
    area = PI * radio ** 2 
    return area

#--> Solicitar al usuario ingresar un valor

radio = float(input("Ingrese el radio del circulo: "))

#--> Llamar a la funcion y mostrar el resultado 

area_resultante = calcular_area(radio)
print(f"El area del circulo con radio {radio} es: {area_resultante}")
"""
#-------------

# ---> Ejemplo de funcion : -->"Convertidor de pesos a dolares"<---

"""
#--> Defino la funcion
def conversor (pesos, valor_dolar):
    dolares = pesos/ valor_dolar
    return dolares

#--> Solicitar al usuario que ingrese la cantidad de pesos 

pesos = float(input("Ingrese la cantidad de PESOS que desea convertir: "))

#--> Solicitar al usuario que ingrese el valor del dolar actual 

valor_dolar = float(input("Ingrese el valor del DOLAR actual: "))

#--> Llamar a la funcion 

resultado = conversor(pesos,valor_dolar)

#--> Mostrar el resultado 

print(f"Usted tiene {resultado} USD")
"""
#-------------


