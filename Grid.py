from tkinter import *
#Lógica
def mostrarNome():
    nome = textbox1.get()
    lab_f=Label(root,text='Seu nome é ' + nome)
    lab_f.grid()
#GUI
root = Tk()
root.title('Título da app')
root.geometry('200x100')
#criar os widgets
lab1 = Label(root,text='Escreva seu nome:')
textbox1 = Entry(root)
btn_1 = Button(root,text='Executar', command=mostrarNome)
#Organizar os widgets
lab1.grid()
textbox1.grid()
btn_1.grid()


root.mainloop()