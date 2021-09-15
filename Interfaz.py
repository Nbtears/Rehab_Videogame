# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 01:41:07 2021

@author: diana
"""

import tkinter as tk   
   

def ingresar():
    print ("Ingreso")
    ingresowindow = tk.Tk()
    ingresowindow.tk.call('wm', 'iconphoto', ingresowindow._w, tk.PhotoImage(file='sources/buble2.png'))
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
    
    y_label = tk.Label (registrowindow,text="Edad: ")
    y_label.pack()
    ytext = tk.Entry (registrowindow)
    ytext.pack()
    
    les_label = tk.Label (registrowindow,text="Lesion: ")
    les_label.pack()
    lestext = tk.Entry (registrowindow)
    lestext.pack()
    
    cl_label = tk.Label (registrowindow,text="Clínica: ")
    cl_label.pack()
    cltext = tk.Entry (registrowindow)
    cltext.pack()
    
    def get_data():
        
        name = nametext.get()
        user = usertext.get()
        age = ytext.get()
        lesion = lestext.get()
        clinic = cltext.get()
        
        print(name)
        print(user)
        print(age)
        print(lesion)
        print(clinic)
        
        return 
    
    accept = tk.Button(registrowindow, text= "Aceptar", command = get_data,
                    activebackground="#008f39")
    accept.pack()
    
def main():
    ventana = tk.Tk()
    ventana.tk.call('wm', 'iconphoto', ventana._w, tk.PhotoImage(file='sources/buble2.png'))
    ventana.geometry("900x600")
    tittle = tk.Label(ventana,text = "Save the axo")
    tittle.pack()
    
    IngBt = tk.Button(ventana,text = "Ingresar", command = ingresar,
                  activebackground="#008f39")
    RegBt = tk.Button(ventana,text = "Registro", command = registro,
                  activebackground="#008f39")
    IngBt.pack(side=tk.BOTTOM)
    RegBt.pack(side=tk.BOTTOM)

    ventana.mainloop()
    
    
main()

