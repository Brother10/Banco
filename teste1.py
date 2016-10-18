#-*- coding:UTF-8 -*-
from Tkinter import *

class novo:

    def __init__(self, janela):
        # Inicia como None
        self.jan = None
        self.caixa=Frame(janela)
        self.caixa.grid()
        self.b=Button(janela, text='Cadastrar', width=10, command=self.new_jan)
        self.b.grid()
        self.b.place(x=30, y=50)
        self.b=Button(janela, text='Saldo', width=10, command=self.saldo)
        self.b.grid()
        self.b.place(x=30, y=80)
        self.b=Button(janela, text='Saque', width=10, command=self.new_jan)
        self.b.grid()
        self.b.place(x=30, y=110)
        self.b=Button(janela, text='Deposito', width=10, command=self.new_jan)
        self.b.grid()
        self.b.place(x=30, y=140)
        self.b=Button(janela, text='Extrato', width=10, command=self.new_jan)
        self.b.grid()
        self.b.place(x=30, y=170)
        self.b=Button(janela, text='Sair', width=10, command=self.new_jan)
        self.b.grid()
        self.b.place(x=30, y=200)
        self.l1=Label(janela, text='raiz!')
        self.l1.grid()

    def new_jan(self):
        # Verifica se já foi criada
        if self.jan is None:
            self.jan=Tk()
            self.jan.protocol("WM_DELETE_WINDOW", self.fecha_jan)
            self.l=Label(self.jan, text='apenas fechando essa janela poderá voltar ou clicar na raiz!')
            self.l.grid()
            self.jan.geometry('300x200')
    def saldo(self):
        if self.jan is None:
            self.jan=Tk()
            self.jan.protocol("WM_DELETE_WINDOW", self.fecha_jan)
            self.l=Label(self.jan, text='Saldo R$ 0,00')
            self.l.grid()
            self.jan.geometry('300x200')
        else:
            # Se já foi, basta colocá-la na frente
            self.jan.lift()

    def fecha_jan(self):
        # Seta de novo em None para recriar quando abrir
        self.jan.destroy()
        self.jan = None

root=Tk()

novo(root)
root.geometry('400x300')

root.mainloop()
novo()
