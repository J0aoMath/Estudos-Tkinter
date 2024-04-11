from tkinter import *
root = Tk()
root.geometry('300x200')


meuMenu = Menu(root)
#meuMenu.add_command(label='File')

fileMenu = Menu(meuMenu, tearoff=0)
#fileMenu = Menu(meuMenu, tearoff=0)
fileMenu.add_command(label='New')
fileMenu.add_command(label='Open')
fileMenu.add_command(label='Save')
fileMenu.add_separator()
fileMenu.add_command(label='Exit')
meuMenu.add_cascade(label='File', menu=fileMenu)

fileEdit = Menu(meuMenu, tearoff=0)
fileEdit.add_command(label='Copy')
fileEdit.add_command(label='Paste')
fileEdit.add_command(label='Select All')
meuMenu.add_cascade(label='Edit', menu=fileEdit)

#meuMenu.add_command(label='Edit')

root.config(menu=meuMenu)
root.mainloop()