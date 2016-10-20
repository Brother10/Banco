#!/usr/bin/python
#coding: utf-8

from Tkinter import *
from conta import Cliente

usuario = Cliente()

class Banco:

	def __init__(self):
		janela = Tk()
		janela.title('\t\t\t\t\tBanco')

		descricao=Label(janela, text = 'Escolha uma das operações')
		descricao.place(x=100, y=8)

		# botões
		btCadastro      = Button(janela, text = 'Cadastrar',width=20, command = self.cadastrar)
		btSaldo         = Button(janela, text = 'Saldo',    width=20, command = self.emitirSaldo)
		btSaque         = Button(janela, text = 'Saque',    width=20, command = self.sacar)
		btDeposito      = Button(janela, text = 'Deposito', width=20, command = self.depositar)
		btExtrato       = Button(janela, text = 'Extrato',  width=20, command = self.emitirExtrato)

		# posição dos botões5
		btCadastro.place(x=100, y=50)
		btSaldo.place   (x=100, y=80)
		btSaque.place   (x=100, y=110)
		btDeposito.place(x=100, y=140)
		btExtrato.place (x=100, y=170)

		janela.geometry("400x250")
		janela.mainloop()

	def cadastrar(self):
		current = Tk()
		current.title('\tCadastrar')

		descricao   = Label(current, text = 'Insira o número da conta:')
		entrada     = Entry(current, width=20)
		ok		    = Button(current, text='OK',width=10, command=lambda:usuario.cadastrar(entrada.get(), retorno))
		retorno     = Label(current, text='')

		descricao.place	(x=60, y=10)
		entrada.place	(x=60, y=40)
		ok.place		(x=90, y=80)
		retorno.place	(x=80, y=120)

		current.geometry("300x200")
		current.mainloop()

	def depositar(self):
		current = Tk()
		current.title('\tDepositar')

		descricao   = Label(current, text = 'Insira o número da conta:')
		entrada     = Entry(current, width=20)

		valor_desc	= Label(current, text = 'Insira o valor de depósito:')
		valor_ent	= Entry(current, width=20)

		ok		    = Button(current, text='OK',width=10, command=lambda:usuario.depositar(entrada.get(), valor_ent.get(), retorno))
		retorno     = Label(current, text='')

		descricao.place	(x=60, y=10)
		entrada.place	(x=60, y=40)

		valor_desc.place(x=60, y=60)
		valor_ent.place	(x=60, y=80)

		ok.place		(x=90, y=100)
		retorno.place	(x=80, y=120)

		current.geometry("300x200")
		current.mainloop()

	def emitirExtrato(self):
		current = Tk()
		current.title('\t\t\tExtrato')

		descricao	= Label(current, text = 'Insira o número da conta:')
		entrada		= Entry(current, width=20)
		ok			= Button(current, text='Emitir',width=10, command=lambda:usuario.emitirExtrato(entrada.get(), retorno))
		retorno     = Label(current, text='')

		descricao.place	(x=60, y=10)
		entrada.place	(x=60, y=40)
		ok.place		(x=90, y=80)
		retorno.place	(x=80, y=120)

		current.geometry("300x200")
		current.mainloop()

	def emitirSaldo(self):
		current = Tk()
		current.title('\t\t\tSaldo')

		descricao	= Label(current, text = 'Insira o número da conta:')
		entrada		= Entry(current, width=20)
		ok			= Button(current, text='Emitir',width=10, command=lambda:usuario.emitirSaldo(entrada.get(), retorno))
		retorno     = Label(current, text='')

		descricao.place	(x=60, y=10)
		entrada.place	(x=60, y=40)
		ok.place		(x=90, y=80)
		retorno.place	(x=80, y=120)

		current.geometry("300x200")
		current.mainloop()

	def sacar(self):
		current = Tk()
		current.title('\t\t\tSaque')

		descricao   = Label(current, text = 'Insira o número da conta:')
		entrada     = Entry(current, width=20)

		valor_desc	= Label(current, text = 'Insira o valor do saque:')
		valor_ent	= Entry(current, width=20)

		ok		    = Button(current, text='OK',width=10, command=lambda:usuario.sacar(entrada.get(), valor_ent.get(), retorno))
		retorno     = Label(current, text='')	

		descricao.place	(x=60, y=10)
		entrada.place	(x=60, y=40)

		valor_desc.place(x=60, y=60)
		valor_ent.place	(x=60, y=80)

		ok.place		(x=90, y=100)
		retorno.place	(x=80, y=120)

		current.geometry("300x200")
		current.mainloop()

Banco()