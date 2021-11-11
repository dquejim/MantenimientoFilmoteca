from tkinter import messagebox as MessageBox
import tkinter.ttk
from tkinter import *
from tkinter import ttk

from Modelo.Pelicula import Pelicula


def vaciarTreeView():

    for i in tree.get_children():
        tree.delete(i)
    ventana.update()

def refrescarTabla ():

    vaciarTreeView()

    f = open("AlmacenCine","r")
    for linea in f:
        Objeto= linea.split(" ")
        id = Objeto[0]
        nombre = Objeto[1]
        genero = Objeto[2]
        anioEstreno = Objeto[3]
        tree.insert("",0,text=id,values=(nombre,genero,anioEstreno))
    f.close()

def addFilm():

    if textId.get() == "" or textNombre.get() == "" or textGenero.get() == "" or textAnioEstreno.get() == "":
        MessageBox.showwarning("Alerta","Rellene todos los campos")
    else:

        id = int(textId.get())
        nombre = textNombre.get()
        genero = textGenero.get()
        anioEstreno = int(textAnioEstreno.get())
        nuevoRegistro = Pelicula(id,nombre,genero,anioEstreno)

        with open("AlmacenCine","a") as file:
            file.write(str(nuevoRegistro.getId()) + " " + nuevoRegistro.getNombre() + " " + nuevoRegistro.getGenero() + " " + str(nuevoRegistro.getAnioEstreno())+"\n")
        file.close()

        refrescarTabla()

def removeFilm():

    if textId.get() == "" or textNombre.get() == "" or textGenero.get() == "" or textAnioEstreno.get() == "":
        MessageBox.showwarning("Alerta","Rellene todos los campos")
    else:
        id = int(textId.get())
        nombre = textNombre.get()
        genero = textGenero.get()
        anioEstreno = int(textAnioEstreno.get())
        removeRegistro = Pelicula(id, nombre, genero, anioEstreno)

        with open("AlmacenCine", "r+") as f:
            d = f.readlines()
            f.seek(0)
            for i in d:
                if i != str(removeRegistro.getId()) + " " + removeRegistro.getNombre() + " " + removeRegistro.getGenero() + " " + str(removeRegistro.getAnioEstreno()) + "\n":
                    f.write(i)
            f.truncate()
        f.close()

        refrescarTabla()


def modifyFilm():

    if textId.get() == "" or textNombre.get() == "" or textGenero.get() == "" or textAnioEstreno.get() == "":
        MessageBox.showwarning("Alerta", "Rellene todos los campos")
    else:
        id = int(textId.get())
        nombre = textNombre.get()
        genero = textGenero.get()
        anioEstreno = int(textAnioEstreno.get())
        modifyRegistro = Pelicula(id, nombre, genero, anioEstreno)

        with open("AlmacenCine", "r+") as f:
            d = f.readlines()
            f.seek(0)
            for i in d:
                Objeto = i.split(" ")
                ModId = Objeto[0]

                if ModId == str(modifyRegistro.getId()):
                    f.write(str(modifyRegistro.getId()) + " " + modifyRegistro.getNombre() + " " + modifyRegistro.getGenero() + " " + str(modifyRegistro.getAnioEstreno()) + "\n")
                else:
                    f.write(i)

            f.truncate()

            refrescarTabla()


if __name__ == '__main__':
    # --Ventana--
    ventana = Tk()
    ventana.title("Gestión de películas")
    ventana.geometry("900x480")
    ventana.config(bg="light gray")
    ventana.resizable(0, 0)

    # --Etiquetas y entradas de texto--
    textId = StringVar()
    textNombre = StringVar()
    textGenero = StringVar()
    textAnioEstreno = StringVar()

    etiquetaId = tkinter.Label(ventana, text="Identificador:", font=("Helvetica", 10, "bold")).place(x=50, y=25)
    Entry(ventana, width=50,textvariable = textId).place(x=200, y=25)

    etiquetaNombre = tkinter.Label(ventana, text="Nombre:", font=("Helvetica", 10, "bold")).place(x=50, y=75)
    Entry(ventana, width=50, textvariable = textNombre).place(x=200, y=75)

    etiquetaGenero = tkinter.Label(ventana, text="Género:", font=("Helvetica", 10, "bold")).place(x=50, y=125)
    Entry(ventana, width=50,textvariable = textGenero).place(x=200, y=125)

    etiquetaAnioEstreno = tkinter.Label(ventana, text="Año de Estreno:", font=("Helvetica", 10, "bold")).place(x=50, y=175)
    Entry(ventana, width=50, textvariable = textAnioEstreno).place(x=200, y=175)

    # --Tabla (TreeView)--
    tree = ttk.Treeview

    tree = ttk.Treeview(ventana, heigh=10, columns=("uno", "dos", "tres"))
    tree.place(x=50, y=225)
    tree.column("#0", width=200)
    tree.column("uno", width=200)
    tree.column("dos", width=200)
    tree.column("tres", width=200)

    tree.heading("#0", text='ID', anchor=CENTER)
    tree.heading("uno", text='NOMBRE', anchor=CENTER)
    tree.heading("dos", text='GÉNERO', anchor=CENTER)
    tree.heading("tres", text='Año de Estreno', anchor=CENTER)

    refrescarTabla()

    # --Botones--

    btAdd = Button(ventana, command=lambda: addFilm(), text='Añadir', width=19)
    btAdd.configure(bg="dark gray", font=("Helvetica", 10, "bold"))
    btAdd.place(x=600, y=45, width=200, height=30)

    btMod = Button(ventana, text='Modificar',command=lambda: modifyFilm(), width=19)
    btMod.configure(bg="dark gray", font=("Helvetica", 10, "bold"))
    btMod.place(x=600, y=95, width=200, height=30)

    btRemove = Button(ventana, text='Eliminar',command=lambda: removeFilm(), width=19)
    btRemove.configure(bg="dark gray", font=("Helvetica", 10, "bold"))
    btRemove.place(x=600, y=145, width=200, height=30)

    ventana.mainloop()



