from tkinter import*
import tkinter as tk
from tkinter import filedialog
import os
import sys

raiz=Tk()
raiz.title("Aplicacion KOED")
raiz.resizable(False, False)
raiz.geometry("1299x705")
raiz.config(bg="white")

miframe=Frame()
miframe.pack()

#
#DEBES TENER UNA IMAGEN GIF LLAMADA FONDO.GIF 1299X705
#

miImagen=PhotoImage(file=r"D:\Universidad\Segundo Semestre\Fundamentos de Programación\Laboratorio\Scripts\fondo.gif")
my_canvas = Canvas(raiz, width=1299, height=705)
my_canvas.pack(fil="both", expand=True)
my_canvas.create_image(0,0, image=miImagen, anchor="nw")

def onOpen():
    print(filedialog.askopenfilename(initialdir="/", title="open file", filetypes=(("Python files","*.py;*.pyw"),("All files","*.*"))))

def onSave():
    print(filedialog.asksaveasfilename(initialdir="/", title="open file", filetypes=(("Python files","*.py;*.pyw"),("All files","*.*"))))

def resetProgram():
    python= sys.executable
    os.execl(python, python, * sys.argv)

#
#ABRIR ARCHIVOS WORD DE TU COMPUTADORA
#

def OpenWord():
    os.startfile("Documento.docx")

#
#ABRIR ARCHIVOS PDF DE TU COMPUTADORA
#

def OpenPdf():
    os.startfile("archivo.pdf")

def OpenPag():
    os.startfile("https://discord.gg/GVZnPmE8vV")

def OpenPag1():
    os.startfile("https://drive.google.com/drive/folders/1J1ZL69j467ZDmcYZrXG0iLoU6Z1uwSpy?usp=share_link")

def OpenPag2():
    os.startfile("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")

barraMenu=Menu(raiz)

mnuArchivo=Menu(barraMenu)
mnuTipoDocum=Menu(barraMenu)
mnuEnlaces=Menu(barraMenu)
#mnuEdicion=Menu(barraMenu)
mnuAyuda=Menu(barraMenu)

mnuArchivo.add_command(label="Abrir", command=onOpen)
mnuArchivo.add_command(label="Nuevo", command=resetProgram)
mnuArchivo.add_command(label="Guardar", command=onSave)
mnuArchivo.add_separator()
mnuArchivo.add_command(label="Salir", command=raiz.destroy)

mnuTipoDocum.add_command(label="PDF", command=OpenPdf)
mnuTipoDocum.add_command(label="Word", command=OpenWord)

mnuEnlaces.add_command(label="Drive", command=OpenPag)
mnuEnlaces.add_command(label="Discord", command=OpenPag1)
mnuEnlaces.add_command(label="RickRoll", command=OpenPag2)

#
#MENU EDICION, DUDO DE SU UTILIDAD
#

#mnuEdicion.add_command(label="Copiar  Ctrl+C")
#mnuEdicion.add_command(label="Cortar  Ctrl+X")
#mnuEdicion.add_command(label="Pegar  Ctrl+V")

mnuAyuda.add_command(label="Ayuda")
mnuAyuda.add_separator()
mnuAyuda.add_command(label="About")

barraMenu.add_cascade(label="Archivo", menu=mnuArchivo)
barraMenu.add_cascade(label="Documentacion", menu=mnuTipoDocum)
barraMenu.add_cascade(label="Enlace", menu=mnuEnlaces)
#barraMenu.add_cascade(label="Edicion", menu=mnuEdicion)
barraMenu.add_cascade(label="Ayuda", menu=mnuAyuda)

raiz.config(menu=barraMenu)

raiz.mainloop()