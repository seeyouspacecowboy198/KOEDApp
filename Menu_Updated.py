from tkinter import*
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox as mb
import os
import sys

'''
FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA
SECCIÓN DEL CURSO: 0-L-18
PROFESOR DE LABORATORIO: CÉSAR RIVERA MORALES
GRUPO: 2
INTEGRANTES:
1. Felipe Cubillos Arredondo / 21.461.391-3
2. Franco Ramos Tapia / 21.235.785-5
3. Henry White Bahamondes / 21.391.941-5
4. Hector Berguño Ordenes / 21.436.054-3
5. Catalina Santana Teiguel / 21.403.107-8
6. Nicola Venegas Osses / 21.144.306-5
DESCRIPCIÓN DEL PROGRAMA: Menu con las funciones de revisar archivos, ver enlaces externos de la app y tutorial de uso junto con info
'''

#DIMENSIONES DEL MENU, (POR CAMBIAR)
raiz=Tk()
raiz.title("Aplicacion KOED")
raiz.resizable(False, False)
raiz.geometry("1299x705")
raiz.config(bg="white")
miframe=Frame()
miframe.pack()

#(IMAGEN DE FONDO EN EL MENU O CANVAS)
miImagen=PhotoImage(file=r"fondo.png")
my_canvas = Canvas(raiz, width=1299, height=705)
my_canvas.pack(fil="both", expand=True)
my_canvas.create_image(0,0, image=miImagen, anchor="nw")

#APARTADO DE FUNCIONES Y DEFINICIONES

def onOpen():
    print(filedialog.askopenfilename(initialdir="/", title="open file", filetypes=(("Python files","*.py;*.pyw"),("All files","*.*"))))
#DA LA OPCION DE ABRIR ARCHIVOS .PY Y DE TODO TIPO

def onSave():
    print(filedialog.asksaveasfilename(initialdir="/", title="open file", filetypes=(("Python files","*.py;*.pyw"),("All files","*.*"))))
#DA LA OPCION DE ABRIR ARCHIVOS .PY Y DE TODO TIPO

def resetProgram():
    python= sys.executable
    os.execl(python, python, * sys.argv)

#FUNCION RESETEAR MENU

def OpenWord():
    os.startfile("Documento.docx")

#FUNCION ABRIR DOCUMENTO WORD

def OpenPdf():
    os.startfile("archivo.pdf")
#FUNCION ABRIR ARCHIVO PDF

#

#FUNCION ABRIR ENLACES EXTERNOS:
def OpenDiscord():
    os.startfile("https://discord.gg/GVZnPmE8vV")
#SERVIDOR DISCORD

def OpenDrive():
    os.startfile("https://drive.google.com/drive/folders/1J1ZL69j467ZDmcYZrXG0iLoU6Z1uwSpy?usp=share_link")
#MATERIAL DRIVE

def OpenRick():
    os.startfile("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")
#HIMNO KOED

def Tutorial():
    mb.showinfo("Tutorial", "1. Archivo: te da la opcion de revisar tus archivos o resetear y salir de la aplicacion\n\n 2. Documentacion: te permite acceder a archivos py docx y pdf\n\n 3. Enlaces: te permite acceder a los enlaces externos que son: Discord y Drive\n\n 4. Ayuda: es el menu en el que estas ahora xd")
#TUTORIAL DE COMO FUNCIONA EL MENU

def About():
    mb.showinfo("Información", "KOED es una aplicacion sin fines de lucro que busca solucionar el problema relacionado con la ODS:4 Educacion de calidad")
#EXPLICA EL PROPOSITO DE KOED (INFO)

#AGREGAR MENU
barraMenu=Menu(raiz)

#AGREGAR OPCIONES DE MENU
mnuArchivo=Menu(barraMenu)
mnuTipoDocum=Menu(barraMenu)
mnuEnlaces=Menu(barraMenu)
mnuAyuda=Menu(barraMenu)

#VENTANA ARCHIVOS CON 4 FUNCIONES
mnuArchivo.add_command(label="Abrir", command=onOpen)
mnuArchivo.add_command(label="Guardar", command=onSave)
mnuArchivo.add_separator()
mnuArchivo.add_command(label="Reset", command=resetProgram)
mnuArchivo.add_command(label="Salir", command=raiz.destroy)

#VENTANA DOCUMENTOS 2 FUNCIONES ABRIR ARCHIVOS
mnuTipoDocum.add_command(label="PDF", command=OpenPdf)
mnuTipoDocum.add_command(label="Word", command=OpenWord)

#VENTANA ENLACES EXTERNOS
mnuEnlaces.add_command(label="Drive", command=OpenDrive)
mnuEnlaces.add_command(label="Discord", command=OpenDiscord)
mnuEnlaces.add_command(label="RickRoll", command=OpenRick)

#VENTANA AYUDA (FALTA AGREGAR FUNCIONES)
#AYUDA=ABRIR PDF CON INFORMACION SOBRE EL MENU
#ABOUT= EXPLICAR EL PROPOSITO DE KOED
mnuAyuda.add_command(label="Ayuda", command=Tutorial)
mnuAyuda.add_separator()
mnuAyuda.add_command(label="About",command=About)

#AGREGAR MENU COMO CASCADA
barraMenu.add_cascade(label="Archivo", menu=mnuArchivo)
barraMenu.add_cascade(label="Documentacion", menu=mnuTipoDocum)
barraMenu.add_cascade(label="Enlace", menu=mnuEnlaces)
barraMenu.add_cascade(label="Ayuda", menu=mnuAyuda)

#AGREGAR MENU
raiz.config(menu=barraMenu)

#ABRIR MENU
raiz.mainloop()