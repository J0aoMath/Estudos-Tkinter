from tkinter import *
root = Tk()
valor_a = IntVar()
ra_1 = Radiobutton(root, text='Opção A 1', variable=valor_a, value = 1)
ra_2 = Radiobutton(root, text='Opção A 2', variable=valor_a, value = 2)
ra_3 = Radiobutton(root, text='Opção A 3', variable=valor_a, value = 3)
#indicatoron=0, etc

ra_1.pack()
ra_2.pack()
ra_3.pack()
ra_1.select()
def ver_radio():
    print(valor_a.get())
cmd = Button(root, text='Executar', command=ver_radio)
cmd.pack()

root.mainloop()