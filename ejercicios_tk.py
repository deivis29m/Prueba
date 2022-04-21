
import csv

import tkinter as tk

import pymysql

def Guarda_registro(D_nombre,D_apellido,D_cedula,D_genero):
    miconexion = pymysql.connect(
        host="localhost",
        user="root",
        passwd="", #colocar contraseña
        database="registros"
        )
    cur = miconexion.cursor()

    consultas = "INSERT INTO registros.registros_de_empleados(nombre,Apellido,Cedula,Genero) VALUES (%s , %s , %s, %s)"
    valor = (D_nombre, D_apellido,D_cedula,D_genero)

    cur.execute(consultas,valor)

    miconexion.commit()

    miconexion.close()
    print(valor)

def Botones_principales(gui):
    boton_registro = tk.Button(gui,text="nuevo registro de empleado" , command=registro_ventana)
    boton_registro.grid(row=2 , column= 0)

def registro_ventana():
    ventana_de_registro = tk.Tk() #ventana regritor empleaddo
    ventana_de_registro.configure(background="sky blue") 
    ventana_de_registro.title("registro_ventana")
    ventana_de_registro.geometry("400x300")
    # almacen de datos
    D_nombre = tk.StringVar()
    D_apellido = tk.StringVar()
    D_cedula = tk.IntVar()
    D_genero = tk.StringVar()

    #campos de texto

    campo_nombre = tk.Entry(ventana_de_registro, textvariable=D_nombre)
    campo_nombre.grid(row=1, column=1, columnspan=2)

    campo_apellidos = tk.Entry(ventana_de_registro, textvariable=D_apellido)
    campo_apellidos.grid(row=2, column=1, columnspan=2)

    campo_cedula = tk.Entry(ventana_de_registro, textvariable=D_cedula)
    campo_cedula.grid(row=3, column=1, columnspan=2)

    campo_genero = tk.Entry(ventana_de_registro, textvariable=D_genero)
    campo_genero.grid(row=4, column=1, columnspan=2)

    #etiquetas

    etiqueta_nombre = tk.Label(ventana_de_registro, text="Nombre")
    etiqueta_nombre.grid(row=1,column=0)

    etiqueta_apellido = tk.Label(ventana_de_registro, text="Apellido")
    etiqueta_apellido.grid(row=2,column=0)

    etiqueta_cedula = tk.Label(ventana_de_registro, text="Cedula")
    etiqueta_cedula.grid(row=3,column=0)

    etiqueta_genero = tk.Label(ventana_de_registro, text="sexo")
    etiqueta_genero.grid(row=4,column=0)

    #botones
    boton_guardar = tk.Button(ventana_de_registro, text="Guarda", command=lambda:[Guarda_registro(D_nombre=campo_nombre.get(), D_apellido=campo_apellidos.get(), D_cedula=campo_cedula.get(), D_genero=campo_genero.get())])
    boton_guardar.grid(row=5, column=0)

    #boton_Consultar = tk.Button(ventana_de_registro, text="Consultar", command=lambda :Guarda_registro(D_nombre=campo_nombre.get(),D_apellido=campo_apellidos.get(),D_cedula=campo_cedula.get(),D_sexo=campo_sexo.get()))
    #boton_Consultar.grid(row=6, column=0)

    #cuadro de consulta 

    text = tk.Text(ventana_de_registro)
    text['state'] = 'disabled'
    text.place(x=180, y=0,width=150,
               height=100)


    ventana_de_registro.mainloop()

if __name__ == "__main__":
    gui = tk.Tk() #ventana principal 
    gui.configure(background="sky blue") #color de fondo
    gui.title("administracion") #titulo de la ventana  
    gui.geometry("500x500") #tamaño de la ventana

    Botones_principales(gui)

    gui.mainloop()