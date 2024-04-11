from tkinter import *

root = Tk()
root.title('Login')

def nomeS():
    texto = textBox1.get()
    Lab = Label(root, text= texto)
    Lab.grid(row=2, sticky=S)


Label(root,text='Usuário').grid(row=0, sticky=W)
Label(root, text='Senha:').grid(row=1, sticky=W)


textBox1 = Entry(root)
textBox2 = Entry(root)

cmd_login = Button(root, text='Login', command=nomeS)

textBox1.grid(row=0, column=1)
textBox2.grid(row=1, column=1)
cmd_login.grid(row=2,column=1, sticky=E)

root.mainloop()