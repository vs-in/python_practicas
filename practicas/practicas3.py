# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

"""
nombre = input("Ingrese una palabra: ")  #----> Ingreso de la palabra.
variable = 10 #---> Variable de Control
for i in range (variable):
    print("La palabra ingresada es:",nombre)
"""

# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)

"""
edad = int(input("Ingrese su edad: "))

for i in range (edad):
    edad = i + 1 
    print("Su edad es:",edad)
"""

#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

n = int(input("Por favor ingrese un numero entero: "))

for i in range (n,-1,-1):
    print(i,end=", ")

