# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 01:41:07 2021

@author: diana
"""

import tkinter as tk   
 
def ingresar():
    ingresowindow = tk.Tk()
    ingresowindow.title("Ingresar")
    ingresowindow.geometry("900x600")
    
    us_label = tk.Label (ingresowindow,text="Usuario: ")
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
    registrowindow.title("Registro")
    registrowindow.geometry("900x600")
    
    name_label = tk.Label (registrowindow,text="Nombre: ")
    name_label.pack(expand = True)
    nametext = tk.Entry (registrowindow)
    nametext.pack(expand = True)
    
    us_label = tk.Label (registrowindow,text="Usuario: ")
    us_label.pack(expand = True)
    usertext = tk.Entry (registrowindow)
    usertext.pack(expand = True)
    
    y_label = tk.Label (registrowindow,text="Edad: ")
    y_label.pack(expand = True)
    ytext = tk.Entry (registrowindow)
    ytext.pack(expand = True)
    
    les_label = tk.Label (registrowindow,text="Lesion: ")
    les_label.pack(expand = True)
    lestext = tk.Entry (registrowindow)
    lestext.pack(expand = True)
    
    cl_label = tk.Label (registrowindow,text="Clínica: ")
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
    
    accept = tk.Button(registrowindow, text= "Aceptar", command = get_data, 
                    activebackground="#ff7ea8")
    accept.pack(expand = True)
    
def main():
    ventana = tk.Tk()
    #ventana.tk.call('wm', 'iconphoto', ventana._w, tk.PhotoImage(file='sources/buble2.png'))
    ventana.title("Save the axo")
    ventana.geometry("900x600")
    tittle = tk.Label(ventana,text = "Save the axo")
    tittle.pack()
    
    
    IngBt = tk.Button(ventana,text = "Ingresar", command = ingresar, 
                  activebackground="#ff7ea8")
    RegBt = tk.Button(ventana,text = "Registro", command = registro, 
                  activebackground="#ff7ea8")
    IngBt.pack(side=tk.BOTTOM, expand = True)
    RegBt.pack(side=tk.BOTTOM, expand = True)

    ventana.mainloop()
    
    return data,user

    
    
main()

