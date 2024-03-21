from tkinter import *

def mostrarNome():
    vartexto.set(textbox.get())

root = Tk()
root.title('app')

vartexto = StringVar()
label1 = Label(root,text='Seu nome é: ')
textbox = Entry(root)
button1 = Button(root, text='Executar',command=mostrarNome)
label2 = Label(root, textvariable=vartexto)
#layout
label1.grid()
textbox.grid()
button1.grid()
label2.grid()
root.mainloop()