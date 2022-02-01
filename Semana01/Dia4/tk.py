from tkinter import *
from tkinter import messagebox

app = Tk()
app.title("Mi primera interfaz")
app.geometry("310x90")

def saludar():
    messagebox.showinfo("Title","Hola "+txtNombre.get())
#*Creamos un frame
frame = LabelFrame(app, text="Mi primera interfaz")
frame.grid(row=1, column=0,columnspan=3,pady=10,padx=10,)

lbnombre = Label(frame,text='Nombre: ')
lbnombre.grid(row=1,column=0,padx=10,pady=10)

txtNombre = Entry(frame)
txtNombre.grid(row=1,column=1,padx=10,pady=10)

btnSaludo = Button(frame,text='Saludar',command=saludar)
btnSaludo.grid(row=1,column=2,padx=10,pady=10)



app.mainloop()