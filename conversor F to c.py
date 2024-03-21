from tkinter import *
#Funçoes
def calcular():
    F = float(textbox1.get())
    C = (F-32) * 5/9
    final.set(str(round(C,1)) + 'graus Celsius')
#GUI
root = Tk()
root.title('App')
final=StringVar()

#widgets
label1 = Label(root, text='Graus Fahrenheit')
textbox1 = Entry(root)
btn1 = Button(root, text='Calcular', command=calcular)
label_resultado = Label(root,textvariable=final)

#Layout
label1.grid()
textbox1.grid()
btn1.grid()
label_resultado.grid()


root.mainloop()