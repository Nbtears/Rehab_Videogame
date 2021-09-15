# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 01:41:07 2021

@author: diana
"""

import tkinter as tk      

ventana = tk.Tk()
ventana.geometry("900x600")
tittle = tk.Label(ventana,text = "Save the axo")
tittle.pack()

def ingresar():
    print ("Ingreso")
    ingresowindow = tk.Tk()
    ingresowindow.geometry("900x600")
    
    us_label = tk.Label (ingresowindow,text="Usuario: ")
    us_label.pack()
    usertext = tk.Entry (ingresowindow)
    usertext.pack()
    
    accept = tk.Button(ingresowindow, text= "Aceptar", 
                    activebackground="#008f39")
    accept.pack()
    
       
def registro():
    print ("Registro")
    registrowindow = tk.Tk()
    registrowindow.geometry("900x600")
    
    name_label = tk.Label (registrowindow,text="Nombre: ")
    name_label.pack()
    nametext = tk.Entry (registrowindow)
    nametext.pack()
    
    us_label = tk.Label (registrowindow,text="Usuario: ")
    us_label.pack()
    usertext = tk.Entry (registrowindow)
    usertext.pack()
    
    us_label = tk.Label (registrowindow,text="Usuario: ")
    us_label.pack()
    usertext = tk.Entry (registrowindow)
    usertext.pack()
    
    les_label = tk.Label (registrowindow,text="Lesion: ")
    les_label.pack()
    lestext = tk.Entry (registrowindow)
    lestext.pack()
    
    cl_label = tk.Label (registrowindow,text="Clínica: ")
    cl_label.pack()
    cltext = tk.Entry (registrowindow)
    cltext.pack()
    
    
IngBt = tk.Button(ventana,text = "Ingresar", command = ingresar,
                  activebackground="#008f39")
RegBt = tk.Button(ventana,text = "Registro", command = registro,
                  activebackground="#008f39")
IngBt.pack(side=tk.BOTTOM)
RegBt.pack(side=tk.BOTTOM)

ventana.mainloop()

