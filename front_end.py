from Tkinter import *
import ttk
from back_end import insertar

def datos(raza,edad,genero,nombre, ecosistema, comida):
    insertar(raza, edad, genero, nombre, ecosistema, comida)

def gui():
    master = Tk()

    notebook = ttk.Notebook(master)
    notebook.pack(fill='both', expand='yes')

    ##Creacion de frames de ambos modulos
    frame1 = ttk.Frame(notebook)
    frame2 = ttk.Frame(notebook)

    ##Labels de la interfaz de mantenimiento
    intro=Label(frame1, text="Por favor ingrese los datos").place(x=5,y=10)
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
    box['values'] = ('','macho', 'hembra')
    box.current(0)
    box.place(x=150,y=100)

    ##Boton de la interfaz de mantenimiento
    aceptar=Button(frame1,text="Registrar datos",
                   command=lambda:datos(s_raza.get(),s_edad.get(),
                                        s_genero.get(),s_nombre.get(),
                                        s_ecosistema.get(),
                                        s_comida.get())).place(x=130,y=230)

    ##agrega los dos paneles
    notebook.add(frame1, text='Mantenimiento')
    notebook.add(frame2, text='Consulta')


    master.geometry('370x300')
    master.mainloop()

##llamada al programa
gui()
