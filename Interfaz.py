# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 01:41:07 2021

@author: diana
"""
import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image

 
def ingresar():
    ingresowindow = tk.Tk()
    fontStyle = tkFont.Font(family="Lucida Grande", size=20)
    ingresowindow.title("Ingresar")
    ingresowindow.iconbitmap("sources/icon.ico")
    ingresowindow.geometry("900x600")
    
    us_label = tk.Label (ingresowindow,text="Usuario: ",font=fontStyle)
    us_label.pack(expand = True)
    usertext = tk.Entry (ingresowindow)
    usertext.pack(expand = True)
    
    def users():
        global user 
        user = usertext.get()
        print(user)
    
    accept = tk.Button(ingresowindow, text= "Aceptar", command = users,
                    activebackground="#ff7ea8")
    accept.pack(expand = True)  
       
def registro():
    registrowindow = tk.Tk()
    fontStyle = tkFont.Font(family="Lucida Grande", size=15)
    registrowindow.title("Registro")
    registrowindow.iconbitmap("sources/icon.ico")
    registrowindow.geometry("900x600")
    
    name_label = tk.Label (registrowindow,text="Nombre: ",font=fontStyle)
    name_label.pack(expand = True)
    nametext = tk.Entry (registrowindow)
    nametext.pack(expand = True)
    
    us_label = tk.Label (registrowindow,text="Usuario: ",font=fontStyle)
    us_label.pack(expand = True)
    usertext = tk.Entry (registrowindow)
    usertext.pack(expand = True)
    
    y_label = tk.Label (registrowindow,text="Edad: ",font=fontStyle)
    y_label.pack(expand = True)
    ytext = tk.Entry (registrowindow)
    ytext.pack(expand = True)
    
    les_label = tk.Label (registrowindow,text="Lesion: ",font=fontStyle)
    les_label.pack(expand = True)
    lestext = tk.Entry (registrowindow)
    lestext.pack(expand = True)
    
    cl_label = tk.Label (registrowindow,text="Clínica: ",font=fontStyle)
    cl_label.pack(expand = True)
    cltext = tk.Entry (registrowindow)
    cltext.pack(expand = True)
    
    def get_data():
        global data 
        name = nametext.get()
        user = usertext.get()
        age = ytext.get()
        lesion = lestext.get()
        clinic = cltext.get()
        data=[name,user,age,lesion,clinic]
        print(data)
        
        return 
    
    accept = tk.Button(registrowindow, text= "Guardar", command = get_data, 
                    activebackground="#ff7ea8")
    accept.pack(expand = True)
    
def main():
    root = tk.Tk()
    fontStyle = tkFont.Font(family="Lucida Grande", size=20)
    root.iconbitmap("sources/icon.ico")
    root.title("Save the axo")
    root.geometry("900x600")

    
    tittle = tk.Label(root,text = "Save\n the\n axo",font=fontStyle)
    tittle.pack()
    
    imag=ImageTk.PhotoImage(Image.open("sources/ajoloextra.png"))
    lbl = tk.Label(root,image=imag)
    lbl.pack(expand=True)
    
    IngBt = tk.Button(root,text = "Iniciar sesión", command = ingresar, 
                  activebackground="#ff7ea8")
    RegBt = tk.Button(root,text = "Registrarse", command = registro, 
                  activebackground="#ff7ea8")
    IngBt.pack(side=tk.BOTTOM, expand = True)
    RegBt.pack(side=tk.BOTTOM, expand = True)

    root.mainloop()
       
main()