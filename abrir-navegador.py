import webbrowser
from tkinter import *

root = Tk( )

root.title('Meu Portfólio')
root.geometry('300x200')


def tag():
    webbrowser.open('https://fernandamakihirose.github.io/portfolio/')


myTag = Button(root, text='Clique para Abrir', command=tag).pack(pady=20)
root.mainloop()