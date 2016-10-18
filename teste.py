#-- coding: utf-8 --
from Tkinter import *

#def cliquei():
    #print('Botão pressionado')
    #print(ent.get())


janela = Tk()
janela.geometry('400x300')
bt = Button(janela, width=10, text='Cadastrar', command= Application()) #command=cliquei
bt.place(x=30, y=50)
bt = Button(janela, width=10, text='Saldo')
bt.place(x=30, y=80)
bt = Button(janela, width=10, text='Saque')
bt.place(x=30, y=110)
bt = Button(janela, width=10, text='Deposito')
bt.place(x=30, y=140)
bt = Button(janela, width=10, text='Extrato')
bt.place(x=30, y=170)
bt = Button(janela, width=10, text='Sair')
bt.place(x=30, y=200)
janela.mainloop()


root = Tk()
Application(root)
root.mainloop()
