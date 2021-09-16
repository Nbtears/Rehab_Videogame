import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image
import os
from pathlib import Path
from datetime import datetime
import csv
import shutil
import pandas as pd

global check, carpeta_sesiones
user='Diana'
def graldatacsv(data):
    global date, carpeta_usuario
    file=open("Patient's Information.csv","a",newline="")
    writer=csv.writer(file)
    writer.writerow(['Full Name','Username','Age', 'Type of lesion','Clinic', 'Date of registration'])     
    info=(data[0],data[1],data[2],data[3],data[4],date)
    writer.writerow(info)
    file.close()
    shutil.move("Patient's Information.csv", carpeta_usuario)

def usercontrol(username):
    global values
    if os.path.exists('Users.csv')==True:
        try:
            values=pd.read_csv('Users.csv')
            exists = values['User'].str.contains(username)
            exist=exists.tolist()
            if (True in exist)==True:
                check=False
            else:
                check=True
        except:
            check=True
    else: 
        check=True      
    return check

def carpetas(data):
    #Crear carpetas
    global carpeta_sesiones, date, carpeta_usuario
    date = datetime.now().strftime("%d-%m-%Y")
    s='\\'
    a_string = os.getcwd()
    new_string = a_string.replace(os.path.basename(os.getcwd()), "")
    carpeta=new_string + 'Expedientes'
    Path(carpeta).mkdir(exist_ok=True)
    carpeta_usuario = carpeta + s + data[0]
    Path(carpeta_usuario).mkdir(exist_ok=True)
    carpeta_sesiones=carpeta_usuario + s +'Sesiones'
    Path(carpeta_sesiones).mkdir(exist_ok=True)
    
    #Almacenar en csv el nickname, nombre y path
    file=open("Users.csv","a",newline="")
    writer=csv.writer(file)
    try:
        pd.read_csv('Users.csv')
    except:
        writer.writerow(['Name','User','Path'])
    info=(data[0], data[1], carpeta_sesiones)
    writer.writerow(info)
    file.close()

def ingresar(root):
    global carpeta_sesiones
    root.destroy()
    ingresowindow = tk.Tk()
    fontStyle = tkFont.Font(family="Georgia", size=15)
    ingresowindow.title("Ingresar")
    ingresowindow.iconbitmap("sources/icon.ico")
    ingresowindow.geometry("900x600")
    
    """
    imagen=ImageTk.PhotoImage(Image.open("sources/axo5.png"))
    lbl = tk.Label(ingresowindow,image=imagen)
    lbl.pack()
    """
    
    us_label = tk.Label (ingresowindow,text="Usuario: ",font=fontStyle)
    us_label.pack(expand = True)
    usertext = tk.Entry (ingresowindow,font=fontStyle)
    usertext.pack(expand = True)
    
    def users():
        global user 
        global user,f 
        global carpeta_sesiones
        user = usertext.get()
        print(user)
        check=usercontrol(user)
        if check==False:
            Paths=values.Path.tolist()
            Users=values.User.tolist()
            i=Users.index(user)
            carpeta_sesiones=Paths[i]
            print(carpeta_sesiones)
        else:
            print('El username no existe, regístrese primero')
            #Aqui va que el nickname no existe y que se vaya a registrar
        
        ingresowindow.destroy()
        
    def new():
        ingresowindow.destroy()
        main()
    
    accept = tk.Button(ingresowindow, text= "Aceptar", command = users,font=fontStyle,
                    activebackground="#ff7ea8")
    accept.pack(expand = True)  
    back = tk.Button(ingresowindow, text= "Volver al menu", command = new,font=fontStyle,
                    activebackground="#ff7ea8")
    back.pack(expand = True)
       
def registro(root):
    root.destroy()
    registrowindow = tk.Tk()
    fontStyle = tkFont.Font(family="Georgia", size=15)
    registrowindow.title("Registro")
    registrowindow.iconbitmap("sources/icon.ico")
    registrowindow.geometry("900x600")
    
    name_label = tk.Label (registrowindow,text="Nombre: ",font=fontStyle)
    name_label.pack(expand = True)
    nametext = tk.Entry (registrowindow,font=fontStyle)
    nametext.pack(expand = True)
    
    us_label = tk.Label (registrowindow,text="Usuario: ",font=fontStyle)
    us_label.pack(expand = True)
    usertext = tk.Entry (registrowindow,font=fontStyle)
    usertext.pack(expand = True)
    
    y_label = tk.Label (registrowindow,text="Edad: ",font=fontStyle)
    y_label.pack(expand = True)
    ytext = tk.Entry (registrowindow,font=fontStyle)
    ytext.pack(expand = True)
    
    les_label = tk.Label (registrowindow,text="Lesion: ",font=fontStyle)
    les_label.pack(expand = True)
    lestext = tk.Entry (registrowindow,font=fontStyle)
    lestext.pack(expand = True)
    
    cl_label = tk.Label (registrowindow,text="Clínica: ",font=fontStyle)
    cl_label.pack(expand = True)
    cltext = tk.Entry (registrowindow,font=fontStyle)
    cltext.pack(expand = True)
    
    def get_data():
        global data, carpeta_sesiones
        name = nametext.get()
        user = usertext.get()
        age = ytext.get()
        lesion = lestext.get()
        clinic = cltext.get()
        data=[name,user,age,lesion,clinic]
        print(data)
        check=usercontrol(data[1])
        if check==True:
            carpetas(data)
            graldatacsv(data)
            print(carpeta_sesiones)
        else:
            print('Username ya utilizado')
        #Aqui va la pantalla de registro de nuevo
        registrowindow.destroy()
        
    def new():
        registrowindow.destroy()
        main()
    
    accept = tk.Button(registrowindow, text= "Guardar", command = get_data, 
                    activebackground="#ff7ea8",font=fontStyle)
    accept.pack(expand = True)
    back = tk.Button(registrowindow, text= "Volver al menu", command = new,font=fontStyle,
                    activebackground="#ff7ea8")
    back.pack(expand = True)
    
def main():
    root = tk.Tk()
    fontStyle = tkFont.Font(family="Georgia", size=50)
    buttonStyle = tkFont.Font(family="Georgia", size=20)
    root.iconbitmap("sources/icon.ico")
    root.title("Save the axo")
    root.geometry("900x600")
    
    """
    fondo
    C = tk.Canvas(root, bg="blue", height=900, width=600) 
    filename = ImageTk.PhotoImage(Image.open("sources/sea5.jpg"))
    background_label = tk.Label(root, image=filename) 
    background_label.place(x=0, y=0, relwidth=1, relheight=1) 
    C.pack() 
    """
    
    tittle = tk.Label(root,text = "Save\n The Axo",font=fontStyle,fg="#ff7ea8")
    tittle.pack()
    
    imag=ImageTk.PhotoImage(Image.open("sources/axo5.png"))
    lbl = tk.Label(root,image=imag)
    lbl.pack(expand=True)
    
    IngBt = tk.Button(root,text = "Iniciar sesión", command = lambda: ingresar(root), 
                  activebackground="#ff7ea8",font=buttonStyle)
    RegBt = tk.Button(root,text = "Registrarse", command = lambda: registro(root),
                  activebackground="#ff7ea8",font=buttonStyle)
    IngBt.pack(side=tk.BOTTOM, expand = True)
    RegBt.pack(side=tk.BOTTOM, expand = True)
    root.mainloop()
    
    return carpeta_sesiones  

if __name__ == "__main__": 
    main()