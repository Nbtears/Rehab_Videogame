import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image

def ingresar(root):
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
        user = usertext.get()
        print(user)
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
        global data 
        name = nametext.get()
        user = usertext.get()
        age = ytext.get()
        lesion = lestext.get()
        clinic = cltext.get()
        data=[name,user,age,lesion,clinic]
        print(data)
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
       