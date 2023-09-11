"""
1- Cree un algoritmo que nos pida ingresar una edad y nos indique por
pantalla si somos mayores de edad.

2- Cree un algoritmo que al ingresar un color nos indique si este es primario o
no con las posibles siguientes leyendas:
“El (color ingresado) es primario” o “El (color ingresado) no es primario”

3- Cree un algoritmo que determine que numero es mayor de una serie de 5
numeros ingresado por el usuario.

4- Defina un algoritmo que le permita al usuario crear una tabla de
multiplicar(del 1 al 10) de X numero.

5- Mejorando el algoritmo anterior ahora el usuario podra elegir desde que
numero empezar y hasta que numero llegar , es decir, podra seleccionar
tabla del 5 desde el 12 hasa el 23.

6 - Cree una calculadora de porcentaje simple, la cual al ingresarle un valor y
un porcentaje nos dira:
Cuanto es el X% de la cantidad ingresada
Cuanto es la cantidad ingresada mas el porcentaje
Cuanto es la cantidad ingresada menos el porcentaje

7- Defina un algoritmo que nos deje ingresar numeros enteros hasta ingresar
un 0 y al finalizar nos regrese la suma total.

8- Calcule el factorial de un numero ingresado por el usuario.

9- Dibuje un rectangulo de 4 filas y 8 columnas utilizando bucles anidados

10- Modificando el ejercio anterior ahora el usuario debe ingresar las
dimensiones.
---------------------------------------------------------------
"""


"""
1)
edad = int(input("Ingrese su edad: "))
if edad >= 18 :
    print(f"Su edad es {edad} Usted es mayor de edad")
else:
    print(f"Su edad es {edad} Usted es menor de edad")
"""



"""
2)
color_primario1 = "rojo"
color_primario2 = "amarillo"
color_primario3 = "azul"

texto = input("Ingrese su color: ")
if texto == color_primario1:
    print(f"El color {texto} es primario")
elif texto == color_primario2:
    print(f"El color {texto} es primario")
elif texto == color_primario3:
    print(f"El color {texto} es primario")
else: 
    print(f"El color {texto} no es primario")
"""



"""
3)
mayor = 0
maximo = 5 #Cantidad de numeros, puede variar

for i in range(maximo):
    num = int(input('Dame un numero:'))
    if num > mayor:
     mayor = num
print("El Numero Mayor de los 5 ingresados es:", mayor)
"""

"""
4)
numero_ingresado = int(input("Ingrese su numero: "))  # Ingreso el numero
tabla = [1,2,3,4,5,6,7,8,9,10]
for i in (tabla):
    resultado = print(f"El resultado de",numero_ingresado,"X",i,"ES: ",numero_ingresado*i)
"""

