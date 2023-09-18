# Importacion de Paquetes o Liberias 

"""
1) primer forma de importar : import tkinter
2) segunda formad de importar : from tkinter import * 
el asterisco significa que importamos todo lo de la libreria 

tkinter --> 

es una interfaz grafica por defecto de python para el kit de herramientas
de GUI tk. tanto tk como tkinter estan disponibles en la mayoria de plataformas
Unix, asi como en sistemas de Windows (Tk en si no es parte de Python, es mantenido por ActiveState)
"""

# Armado de una Calculadora Basica 

from tkinter import Tk, Entry, Button, StringVar   #---> importamos desde tkinter Tk 


# Funciones 

digito = "" 

def tomar_digito(n):
    global digito 
    digito += str(n)
    calculo.set(digito)


# Funcion para el boton = 

def resultado():
    try:
        global digito
        total = str(eval(digito))
        calculo.set(total)
        digito = ""
    except:
        calculo.set("Error")

# Funcion para el boton de borrar

def limpiar_completo():
    global digito 
    calculo.set("")
    digito = ""

ventana = Tk()


#---> Configuracion de Ventana

ventana.configure(background="light blue")
ventana.title("Calculadora Basica")
ventana.geometry("244x330")
ventana.resizable(False,False)

calculo = StringVar() #---> Variable de control

#---> Configuracion de Espacio para Ingresar

datos = Entry(ventana, bg="black", fg="white", textvariable=calculo )   #---> En la variable datos le vamos a pasar nuestra variable ventana.
datos.grid(columnspan="5" , ipadx=60 , ipady= 15)


###-->

###--> Botones Calculadora

###--> Fila 1 

boton_uno = Button(ventana, text="1", fg="black", bg="white", height=3 , width=7,command= lambda: tomar_digito(1))
boton_uno.grid(columnspan=1,row=2,column=1)

boton_dos = Button(ventana, text="2", fg="black", bg="white", height=3 , width=7,command= lambda: tomar_digito(2))
boton_dos.grid(columnspan=1,row=2,column=2)

boton_tres = Button(ventana, text="3", fg="black", bg="white", height=3 , width=7,command= lambda: tomar_digito(3))
boton_tres.grid(columnspan=1,row=2,column=3)

boton_sumar = Button(ventana, text="+", fg="black", bg="white", height=3 , width=7,command= lambda: tomar_digito())
boton_sumar.grid(columnspan=1,row=2,column=4)

###--> Fila 2

boton_cuatro = Button(ventana, text="4", fg="black", bg="white", height=3 , width=7,command= lambda: tomar_digito(4))
boton_cuatro.grid(columnspan=1,row=3,column=1)

boton_cinco = Button(ventana, text="5", fg="black", bg="white", height=3 , width=7,command= lambda: tomar_digito(5))
boton_cinco.grid(columnspan=1,row=3,column=2)

boton_seis = Button(ventana, text="6", fg="black", bg="white", height=3 , width=7,command= lambda: tomar_digito(6))
boton_seis.grid(columnspan=1,row=3,column=3)

boton_restar = Button(ventana, text="-", fg="black", bg="white", height=3 , width=7,command= lambda: tomar_digito("-"))
boton_restar.grid(columnspan=1,row=3,column=4)

###--> Fila 3

boton_siete = Button(ventana, text="7", fg="black", bg="white", height=3 , width=7,command= lambda: tomar_digito(7))
boton_siete.grid(columnspan=1,row=4,column=1)

boton_ocho = Button(ventana, text="8", fg="black", bg="white", height=3 , width=7,command= lambda: tomar_digito(8))
boton_ocho.grid(columnspan=1,row=4,column=2)

boton_nueve = Button(ventana, text="9", fg="black", bg="white", height=3 , width=7,command= lambda: tomar_digito(9))
boton_nueve.grid(columnspan=1,row=4,column=3)

boton_multiplicar = Button(ventana, text="*", fg="black", bg="white", height=3 , width=7,command= lambda: tomar_digito("*"))
boton_multiplicar.grid(columnspan=1,row=4,column=4)

###--> Fila 4

boton_cero = Button(ventana, text="0", fg="black", bg="white", height=3 , width=7,command= lambda: tomar_digito(0))
boton_cero.grid(columnspan=1,row=5,column=1)

boton_coma = Button(ventana, text=",", fg="black", bg="white", height=3 , width=7,command= lambda: tomar_digito(","))
boton_coma.grid(columnspan=1,row=5,column=2)

boton_borrar = Button(ventana, text="C", fg="black", bg="white", height=3 , width=7,command= lambda: tomar_digito(limpiar_completo))
boton_borrar.grid(columnspan=1,row=5,column=3)

boton_dividir = Button(ventana, text="/", fg="black", bg="white", height=3 , width=7,command= lambda: tomar_digito("/"))
boton_dividir.grid(columnspan=1,row=5,column=4)

###-->

boton_parentesis_uno = Button(ventana, text="(", fg="black", bg="white", height=3 , width=7,command= lambda: tomar_digito("("))
boton_parentesis_uno.grid(columnspan=1,row=6,column=1)

boton_igual = Button(ventana, text="=", fg="black", bg="white", height=3 , width=16,command= lambda: tomar_digito(resultado))
boton_igual.grid(columnspan=2,row=6,column=2)

boton_parentesis_dos = Button(ventana, text=")", fg="black", bg="white", height=3 , width=7,command= lambda: tomar_digito(")"))
boton_parentesis_dos.grid(columnspan=1,row=6,column=4)

###-->

ventana.mainloop()  #---> Metodo mainloop para visualizar 

#----> Escribir el codigo debajo del mainloop ()

