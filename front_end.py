# -*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox as messagebox # Importa la caja de texto
import ttk
from back_end import *

master = Tk()

def registraDatos(raza,edad,genero,nombre, ecosistema, comida):
    if ( (raza == "") or (edad == "") or (genero == "") or (nombre == "")
        or (ecosistema == "") or (comida == "") ):
            #Mensaje de respuesta
            messagebox.showwarning("¡Alerta!",
                                           "Debes ingresar todos los datos")
    else:
        insertar(raza, edad, genero, nombre, ecosistema, comida)
        #print(raza, edad, genero, nombre, ecosistema, comida)
        #Mensaje de respuesta
        messagebox.showwarning("¡Aviso!",
                                        "Datos registrados con exito")

def consultaDatos(raza,edad,genero,nombre, ecosistema, comida):
    consultar([raza, edad, genero, nombre, ecosistema, comida],[raza, edad, genero, nombre, ecosistema, comida] )
    #print(raza, edad, genero, nombre, ecosistema, comida)

def gui():

    window = ttk.Notebook(master)
    window.pack(fill='both', expand='yes')

    ##Creacion de frames de ambos modulos
    frame1 = ttk.Frame(window)
    frame2 = ttk.Frame(window)

#############################################################################

    ##Labels de la interfaz de mantenimiento
    intro=Label(frame1, text="Por favor ingrese los datos a registrar"
                ).place(x=5,y=10)
    raza=Label(frame1, text="Raza:").place(x=30,y=40)
    edad=Label(frame1, text="Edad:").place(x=30,y=70)
    genero=Label(frame1, text="Genero:").place(x=30,y=100)
    nombre=Label(frame1, text="Nombre:").place(x=30,y=130)
    ecosistema=Label(frame1, text="Ecosistema:").place(x=30,y=160)
    comida=Label(frame1, text="Comida favorita:").place(x=30,y=190)

    ##Creacion de los entrys de la interfaz de mantenimiento
    s_raza = StringVar()
    s_edad = StringVar()
    s_nombre = StringVar()
    s_ecosistema = StringVar()
    s_comida = StringVar()

    e_raza = Entry(frame1,textvariable=s_raza).place(x=150,y=40)
    e_edad = Entry(frame1,textvariable=s_edad).place(x=150,y=70)
    e_nombre = Entry(frame1,textvariable=s_nombre).place(x=150,y=130)
    e_ecosistema = Entry(frame1,textvariable=s_ecosistema).place(x=150,y=160)
    e_comida = Entry(frame1,textvariable=s_comida).place(x=150,y=190)
    
    ##Combobox de la seleccion de genero
    s_genero=StringVar()
    box=ttk.Combobox(frame1, textvariable=s_genero, state = 'readonly')
    box['values'] = ('macho', 'hembra')
    box.current(0)
    box.place(x=150,y=100)

    ##Boton de la interfaz de mantenimiento
    aceptar=Button(frame1,text="Registrar datos",
                   command=lambda:registraDatos(s_raza.get(),s_edad.get(),
                                        s_genero.get(),s_nombre.get(),
                                        s_ecosistema.get(),
                                        s_comida.get())).place(x=130,y=230)

    
###########################################################################


    ##Labels de la interfaz de consulta
    intro=Label(frame2, text="Ingrese los datos a consultar").place(x=5,y=10)
    raza=Label(frame2, text="Raza:").place(x=30,y=40)
    edad=Label(frame2, text="Edad:").place(x=30,y=70)
    genero=Label(frame2, text="Genero:").place(x=30,y=100)
    nombre=Label(frame2, text="Nombre:").place(x=30,y=130)
    ecosistema=Label(frame2, text="Ecosistema:").place(x=30,y=160)
    comida=Label(frame2, text="Comida favorita:").place(x=30,y=190)

    ##Creacion de los entrys de la interfaz de consulta
    s_raza2 = StringVar()
    s_edad2 = StringVar()
    s_genero2 = StringVar()
    s_nombre2 = StringVar()
    s_ecosistema2 = StringVar()
    s_comida2 = StringVar()

    e_raza = Entry(frame2,textvariable=s_raza2).place(x=150,y=40)
    e_edad = Entry(frame2,textvariable=s_edad2).place(x=150,y=70)
    e_genero = Entry(frame2,textvariable=s_genero2).place(x=150,y=100)
    e_nombre = Entry(frame2,textvariable=s_nombre2).place(x=150,y=130)
    e_ecosistema = Entry(frame2,textvariable=s_ecosistema2).place(x=150,y=160)
    e_comida = Entry(frame2,textvariable=s_comida2).place(x=150,y=190)

    ##Boton de la interfaz de consulta
    aceptar=Button(frame2,text="Consultar datos",
                   command=lambda:consultaDatos(s_raza2.get(),s_edad2.get(),
                                        s_genero2.get(),s_nombre2.get(),
                                        s_ecosistema2.get(),
                                        s_comida2.get())).place(x=130,y=230)    


############################################################################
    
    ##agrega los dos paneles
    window.add(frame1, text='Mantenimiento')
    window.add(frame2, text='Consulta')


##llamada al programa
gui()
master.title("Zoo")
master.geometry('370x300')
master.mainloop()
