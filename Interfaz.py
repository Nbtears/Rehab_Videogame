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
    carpeta=new_string + 'Medical records'
    Path(carpeta).mkdir(exist_ok=True)
    carpeta_usuario = carpeta + s + data[0]
    Path(carpeta_usuario).mkdir(exist_ok=True)
    carpeta_sesiones=carpeta_usuario + s +'Sesions'
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

def ingresar(root,control=False):
    global carpeta_sesiones
    root.destroy()
    ingresowindow = tk.Tk()
    fontStyle = tkFont.Font(family="Georgia", size=15)
    ingresowindow.title("Log in")
    ingresowindow.iconbitmap("sources/icon.ico")
    ingresowindow.geometry("900x600")
    
    if control:
        error_label = tk.Label (ingresowindow,text="Username not found",font=fontStyle,fg="#ff0080")
        error_label.pack(expand = True)

    us_label = tk.Label (ingresowindow,text="Username: ",font=fontStyle)
    us_label.pack(expand = True)
    usertext = tk.Entry (ingresowindow,font=fontStyle)
    usertext.pack(expand = True)
    
    def users():
        global vaules 
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
            ingresowindow.destroy()

        else:
            control=True
            ingresar(ingresowindow,control)
            #Aqui va que el nickname no existe y que se vaya a registrar
        
       
        
    def new():
        ingresowindow.destroy()
        main()
    
    accept = tk.Button(ingresowindow, text= "Log in", command = users,font=fontStyle,
                    activebackground="#ff7ea8")
    accept.pack(expand = True)
    re = tk.Button(ingresowindow, text= "Sign up", command = lambda: registro(ingresowindow),font=fontStyle,
                    activebackground="#ff7ea8")
    re.pack(expand = True)
    back = tk.Button(ingresowindow, text= "Menu", command = new,font=fontStyle,
                    activebackground="#ff7ea8")
    back.pack(expand = True)
       
def registro(root,control=False):
    root.destroy()
    registrowindow = tk.Tk()
    fontStyle = tkFont.Font(family="Georgia", size=15)
    registrowindow.title("Sign up")
    registrowindow.iconbitmap("sources/icon.ico")
    registrowindow.geometry("900x600")
    
    name_label = tk.Label (registrowindow,text="Full name: ",font=fontStyle)
    name_label.pack(expand = True)
    nametext = tk.Entry (registrowindow,font=fontStyle)
    nametext.pack(expand = True)

    if control:
        error_label = tk.Label (registrowindow,text="Username not available",font=fontStyle,fg="#ff0080")
        error_label.pack(expand = True)

    us_label = tk.Label (registrowindow,text="Username: ",font=fontStyle)
    us_label.pack(expand = True)
    usertext = tk.Entry (registrowindow,font=fontStyle)
    usertext.pack(expand = True)
    
    y_label = tk.Label (registrowindow,text="Age: ",font=fontStyle)
    y_label.pack(expand = True)
    ytext = tk.Entry (registrowindow,font=fontStyle)
    ytext.pack(expand = True)
    
    les_label = tk.Label (registrowindow,text="Lesion: ",font=fontStyle)
    les_label.pack(expand = True)
    lestext = tk.Entry (registrowindow,font=fontStyle)
    lestext.pack(expand = True)
    
    cl_label = tk.Label (registrowindow,text="Clinic: ",font=fontStyle)
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
        check=usercontrol(data[1])
        if check==True:
            registrowindow.destroy()
            carpetas(data)
            graldatacsv(data)
            
        else:
            control = True
            registro(registrowindow,control)
        #Aqui va la pantalla de registro de nuevo
        
    def new():
        registrowindow.destroy()
        main()
    
    accept = tk.Button(registrowindow, text= "Save", command = get_data, 
                    activebackground="#ff7ea8",font=fontStyle)
    accept.pack(expand = True)
    back = tk.Button(registrowindow, text= "Menu", command = new,font=fontStyle,
                    activebackground="#ff7ea8")
    back.pack(expand = True)
    
def main():
    global caperta_sesiones,control
    root = tk.Tk()
    control = False
    fontStyle = tkFont.Font(family="Georgia", size=50)
    buttonStyle = tkFont.Font(family="Georgia", size=20)
    root.iconbitmap("sources/icon.ico")
    root.title("Save the axo")
    root.geometry("900x600")
    
    tittle = tk.Label(root,text = "Save\n The Axo",font=fontStyle,fg="#ff7ea8")
    tittle.pack()
    
    imag=ImageTk.PhotoImage(Image.open("sources/axo5.png"))
    lbl = tk.Label(root,image=imag)
    lbl.pack(expand=True)
    
    IngBt = tk.Button(root,text = "Log in", command = lambda: ingresar(root), 
                  activebackground="#ff7ea8",font=buttonStyle)
    RegBt = tk.Button(root,text = "Sign up", command = lambda: registro(root),
                  activebackground="#ff7ea8",font=buttonStyle)
    IngBt.pack(side=tk.BOTTOM, expand = True)
    RegBt.pack(side=tk.BOTTOM, expand = True)
    root.mainloop()
    print(carpeta_sesiones)
    return carpeta_sesiones  

if __name__ == "__main__": 
    main()