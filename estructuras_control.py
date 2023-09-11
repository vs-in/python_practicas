"""
Las ESTRUCTURAS DE CONTROL permiten modificar el flujo de la 
ejecucion de las instrucciones de un programa:

1) Ejecutar un grupo u otro de sentencias, segun se cumpla o no
una condicion.
2) Ejecutar un grupo de sentencias mientras se cumpla una condicion.
3) Repetir un grupo de sentencias un numero determinado de veces.

"""



"""
#TIPOS DE ESTRUCTURAS DE CONTROL:

#SECUENCIALES : Las instrucciones se ejecutan una despues de la otra 
en el orden en que estan escritas, es decir, en secuencia.
SE EJECUTAN UNA ABAJO DE LA OTRA.

#CONDICIONALES: (Selecciones o de decision) ejecutan un bloque de instrucciones
u otro, o saltan a un subprograma o subrutina segun se cumpla o no
una condicion. 
VERDADERO O FALSO (CONDICION).

#ITERATIVAS: (Repetitivas) inician o repiten un bloque de instrucciones
si se cumple una condicion o mientras se cumple una condicion.
(BUCLES O CICLOS)
"""


"""
#OPERADORES 

#OPERADORES RELACIONALES

Los operadores de relacion o de comparacion se utilizan para comparar
dos o mas valores. El resultado de estos operadores siempre es TRUE o FALSE.
Donde los operandos podran ser variables - constantes o expresiones aritmeticas

> mayor que
>= mayor o igual que 
< menor que
<= menor o igual que 
== igual 
!= distinto 

#OPERADORES LOGICOS 

Se utiliza un operador logico para una decision basada en multiples condiciones
los operadores logicos utilizados en python son:

AND : Conector "Y" ( Ambas tienen que ser VERDADERO )
OR : Conector "o" ( Siempre va a hacer VERDADERO cuando alguna de las dos de VERDADERO)
NOT : Negacion ( Siempre va a dar el valor opuesto )

"""

"""
#ESTRUCTURAS CONDICIONALES

Las estructuras condiciones tienen como objetivo ejecutar un bloque de 
instrucciones u otro en base a una condicion que puede ser VERDADERA o FALSA
la palabra clave asociada a esta estructura es IF.

Si la condiciones es TRUE se ejecuta el bloque dentro del IF 
luego independientemente del valor de verdad de la condicion
el programa continua con la ejecucion del resto del programa.
--------------------------
"""



"""
--------------------------
CONDICIONAL SIMPLE

temperatura = float(input("ingrese la temperatura : "))

if temperatura > 37.8:
    print("usted tiene fiebre")  

El bloque 76 se encuentra INDENTADO sino no tendria valor el IF.

CONDICIONAL COMPUESTO

temperatura = float(input("ingrese la temperatura : "))

if temperatura > 37.8:
    print("usted tiene fiebre")  
else:
    print("usted no tiene fiebre)

"""


"""
--------------------------
# Elif

nota = int(input("ingrese su nota:  "))

if nota <= 4: 
     print("Desaprobado)
elif nota >4 and nota <=8:
     print("Aprobado)
else:
     print("Promocionado)

--------------------------
"""






"""
--------------------------
#--> BUCLES (CICLOS)

Repiten un codigo dependiendo de una condicion o de un contador.
si se cumple la condicion se ejecuta un bloque de codigo y se comprueba
nuevamente la condicion. Pueden ser dos clases:


-CICLOS EXACTOS: conocemos la cantidad exacta de repeticiones.
ese valor es aportado al iniciar el programa o por el usuario
antes de que se inicie el ciclo. 

WHILE & FOR PERTENECEN A ESTE GRUPO

-CICLOS CONDICIONALES: No se conocen de antemano la cantidad de 
repeticiones. Dependen de una condicion que puede variar.
Finaliza cuando la condicion es falsa. Se puede repetir una vez,
varias veces o ninguna vez.

WHILE PERTENECE A ESTE GRUPO

--------------------------
#--> Ejemplos 


#-While version 1 - Exacto

contador = 1 
suma = 0 

while contador <= 3:
     nota = int(input("Ingrese su nota:  "))
     contador += 1
     suma += nota

print(f"Su promedio es: {suma/(contador-1)}  /n")
#print(f"Valor final del contador: {contador}")



#-While version 2 - Condicional

password = "holiwis"
incorrecta = True
intentos = 0 
nombre = input("Ingrese su nombre:  ")

while incorrecta:
    password2 = input("Ingrese su contraseña:  ")
    if password == password2:
      incorrecta = False
    intentos += 1 

print(f"Hola {nombre}, ingresaste al sistema luego de {intentos} intentos fallidos")


--------------------------
"""




"""
--------------------------
#---> Bucle : FOR 

Como se forman los bucles FOR?


--> Version LARGA
for i in range (inicio,fin,paso):

Donde "i" es la variable que incrementa su valor en paso unidades en cada iteracion.
Donde "inicio" valor inicial que tomara "i".
Donde "fin" valor final del bucle, el bucle continuara para "i" menor a este valor.
Donde "paso" valor por el cual se incrementa cada vuelta.


--> Version MEDIA
for i in range(inicio,fin):

En este caso, al no estar el "paso" por defecto se incrementa en 1 en cada vuelta.


--> Version CORTA
for i in range(fin):

Al igual que el anterior se incrementa en 1 y al no tener valor inicial comienza en 0.

"""











