import tkinter
from tkinter import messagebox
from tkinter import *
import ast

ventana = tkinter.Tk()
ventana.title('Sistema de Login')
ventana.geometry('925x500+300+200')
ventana.configure(bg="white")
ventana.resizable(False, False)

# Insertar en la funcion sistema de datos
def iniciar_sesion():
  usuario=usuario_login.get()
  contraseña=contraseña_login.get()

  archivo_1=open(r"C:\Users\doyou\Desktop\Code\Code for KOED\basededatos.txt","r")
  x_1= archivo_1.read()
  s_1=ast.literal_eval(x_1)
  archivo_1.close()

  #print(s_1.keys())
  #print(s_1.values())

  if usuario in s_1.keys() and contraseña==s_1[usuario]:
    pantalla=Toplevel(ventana)
    pantalla.title("Sesión online")
    pantalla.geometry('925x500+300+200')
    pantalla.config(bg="white")

    Label(pantalla, text="¡Bienvenido a KOED!", bg= "#fff", font=("Calibri(Body)", 50, "bold")).pack(expand=True)

    pantalla.mainloop()

  else:
    messagebox.showerror("Error", "El usuario y contraseña son incorrectos")
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
def registro_2():
  ventana_2=Toplevel(ventana)
  ventana_2.title("Registro")
  ventana_2.geometry("925x500+300+200")
  ventana_2.configure(bg="#fff")
  ventana_2.resizable(False, False)
  def registrarse():
    usuario_1= usuario_registro.get()
    contraseña_1= contraseña_registro.get()
    contraseña_repetir_1 = contraseña_repetir.get()

#Experimental de Database(funcional con .txt)===========================================
    if contraseña_1==contraseña_repetir_1:
      try:
        archivo = open(r"C:\Users\doyou\Desktop\Code\Code for KOED\basededatos.txt", "r+")
        X=archivo.read()
        s = ast.literal_eval(X)

        dict2= {usuario_1:contraseña_1}
        s.update(dict2)
        archivo.truncate(0)
        archivo.close()

        archivo=open(r"C:\Users\doyou\Desktop\Code\Code for KOED\basededatos.txt", "w")
        w=archivo.write(str(s))

        messagebox.showinfo("Registro", "Registrado con exito")
        ventana_2.destroy()

      except:
        archivo=open(r"C:\Users\doyou\Desktop\Code\Code for KOED\basededatos.txt", "w")
        doc=str({"Usuario":"Contraseña"})
        archivo.write(doc)
        archivo.close()

    else:
      messagebox.showerror("Error","Ambas contraseñas deben ser iguales") 

#============================================================================

  def registro_1():
    ventana_2.destroy()



  imagen = PhotoImage(file=r"C:\Users\doyou\Desktop\Code\Code for KOED\FondoUsachino.PNG")
  Label(ventana_2, image=imagen, border= 0, bg="white").place(x=50, y=50)

  ventana_extendida_2 = Frame(ventana_2, width=500, height=390, bg="#fff")
  ventana_extendida_2.place(x=380, y=50)

  titulo_registro = Label(ventana_extendida_2, text= "Crea tu cuenta de KOED", fg ="#B76E22", bg="white", font=("Microsft Yahei UI Light", 23, "bold"))
  titulo_registro.place(x=100, y=5)

#=========================================================================    
  def al_clickear(e):
    usuario_registro.delete(0, 'end')

  def al_salir(e):
    nombre = usuario_registro.get()
    if nombre=="":
      usuario_registro.insert(0, "Usuario")


  usuario_registro = Entry(ventana_extendida_2, width = 25, fg="black", border=0, bg ="white", font=("Microsft Yahei UI Light", 11))
  usuario_registro.place(x=90, y=80)
  usuario_registro.insert(0, "Usuario")
  usuario_registro.bind("<FocusIn>", al_clickear)
  usuario_registro.bind("<FocusOut>", al_salir)

  Frame(ventana_extendida_2, width=395, height=2, bg="black").place(x=85, y=107)	

#===========================================================================
  def al_clickear(e):
    contraseña_registro.delete(0, 'end')

  def al_salir(e):
    nombre = contraseña_registro.get()
    if nombre=="":
      contraseña_registro.insert(0, "Contraseña")


  contraseña_registro = Entry(ventana_extendida_2, width = 25, fg="black", border=0, bg ="white", font=("Microsft Yahei UI Light", 11))
  contraseña_registro.place(x=90, y=150)
  contraseña_registro.insert(0, "Contraseña")
  contraseña_registro.bind("<FocusIn>", al_clickear)
  contraseña_registro.bind("<FocusOut>", al_salir)

  Frame(ventana_extendida_2, width=395, height=2, bg="black").place(x=85, y=177)	

#===========================================================================
  def al_clickear(e):
    contraseña_repetir.delete(0, 'end')

  def al_salir(e):
    nombre = contraseña_repetir.get()
    if nombre=="":
      contraseña_repetir.insert(0, "Contraseña")


  contraseña_repetir = Entry(ventana_extendida_2, width = 25, fg="black", border=0, bg ="white", font=("Microsft Yahei UI Light", 11))
  contraseña_repetir.place(x=90, y=220)
  contraseña_repetir.insert(0, "Repita la contraseña")
  contraseña_repetir.bind("<FocusIn>", al_clickear)
  contraseña_repetir.bind("<FocusOut>", al_salir)

  Frame(ventana_extendida_2, width=395, height=2, bg="black").place(x=85, y=247)	
#===========================================================================

  Button(ventana_extendida_2, width=39, pady=7, text="Registrase", bg="#B76E22", fg="white", border=0, command=registrarse).place(x=145, y=280)
  etiqueta_final_2=Label(ventana_extendida_2, text="¿Ya tengo una cuenta?", fg="black", bg="white", font=("Microsft Yahei UI Light", 9))
  etiqueta_final_2.place(x=175, y=340)

  registro_boton_2= Button(ventana_extendida_2, width=9, text="Iniciar sesión", border=0, bg="white", cursor="hand2", fg="#B76E22", command=registro_1)
  registro_boton_2.place(x=310, y=340)




  ventana_2.mainloop()


#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
ventana_extendida=Frame(ventana, width=450, height=350, bg="white")
ventana_extendida.place(x=350, y=70)

titulo_login=Label(ventana_extendida, text = "Iniciar sesión en \nKOED", fg="#B76E22", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
titulo_login.place(x=65, y=5)

#================================================================
def al_clickear(e):
  usuario_login.delete(0, 'end')

def al_salir(e):
  nombre = usuario_login.get()
  if nombre=="":
    usuario_login.insert(0, "Usuario")


usuario_login = Entry(ventana_extendida, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
usuario_login.place(x=30, y=100)
usuario_login.insert(0, "Usuario")
usuario_login.bind("<FocusIn>", al_clickear)
usuario_login.bind("<FocusOut>", al_salir)

Frame(ventana_extendida, width=325, height=2, bg="black").place(x=26, y=123)

#================================================================

def al_clickear(e):
  contraseña_login.delete(0, 'end')

def al_salir(e):
  nombre = contraseña_login.get()
  if nombre=="":
    contraseña_login.insert(0, "Contraseña")

contraseña_login = Entry(ventana_extendida, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11), show="*")
contraseña_login.place(x=30, y=170)
contraseña_login.insert(0, "Contraseña")
contraseña_login.bind("<FocusIn>", al_clickear)
contraseña_login.bind("<FocusOut>", al_salir)

Frame(ventana_extendida, width=325, height=2, bg="black").place(x=26, y=193)

#================================================================
Button(ventana_extendida, width=39, pady=7, text="Iniciar sesión", bg="#B76E22", fg="white", border=0, command=iniciar_sesion).place(x=50, y=220)
etiqueta_final=Label(ventana_extendida, text="¿No tienes cuenta de KOED?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9))
etiqueta_final.place(x=55, y=280)

registro_final = Button(ventana_extendida, width=8, text="Registrate", border=0, bg='white', cursor="hand2", fg="#B76E22", command=registro_2)
registro_final.place(x=230, y=280)


imagen = PhotoImage(file=r"C:\Users\doyou\Desktop\Code\Code for KOED\Koed.PNG")
Label(ventana, image=imagen, bg="white").place(x=10,y=150)

ventana.mainloop()
