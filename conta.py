#coding: utf-8

import pickle, os, commands
from Tkinter import *
from errors import ValorInvalidoError
from errors import SaldoInsuficienteError

class Cliente:

	def cadastrar(self, user, retorno):

		try:
			path = open('contas/' + user, 'rb')
			retorno['text'] = 'Conta já cadastrada!'

		except:
			os.system('mkdir contas') # cria a pasta
			os.system('clear')

			path = open('contas/' + user, 'wb')
			pickle.dump('Extrato - Conta: ' + user, path)
			pickle.dump('==============', path)
			retorno['text'] = 'Cadastrada com sucesso!'
			path.close()

			paths = open('contas/' + user + '_saldo', 'wb')
			pickle.dump('0.00', paths)
			paths.close()


	def depositar(self, user, valor, retorno):

		if float(valor) <= 0:
			retorno['text'] = ValorInvalidoError()
			return

		try:
			path = open('contas/' + user, 'ab')
			pickle.dump('R$ ' + str(valor) + ' (Depósito)', path)

			path = open('contas/' + user + '_saldo', 'rb')
			atual = pickle.load(path)
			
			value = float(valor) + float(atual)

			path = open('contas/' + user + '_saldo', 'wb')
			pickle.dump(str(value), path)

			retorno['text'] = 'Depósito efetuado!'
			path.close()
		except IOError:
			retorno['text'] = 'Conta inexistente!'

		return


	def emitirSaldo(self, user, retorno):

		try:
			path = open('contas/' + user + '_saldo', 'rb')
		except:
			retorno['text'] = 'Conta inexistente!'
			return

		retorno['text'] = 'Saldo: R$ ' + str(pickle.load(path))
		path.close()

	def emitirExtrato(self, user, retorno):

		try:
			path = open('contas/' + user, 'rb')
		except:
			retorno['text'] = 'Conta inexistente!'
			return

		current = Tk()
		current.title('\tExtrato')

		ty = 20

		while True:
			try:
				line = Label(current, text=pickle.load(path))
				line.place(x=80, y=ty)
				ty += 20
			except EOFError:
				break

		line = Label(current, text='==============')
		line.place(x=80, y=ty)
		self.emitirSaldo(user, retorno)

		line = Label(current, text=retorno['text'])
		line.place(x=80, y=ty+20)

		retorno['text'] = ''
		current.geometry("300x300")
		current.mainloop()

	def sacar(self, user, valor, retorno):

		try:
			path = open('contas/' + user + '_saldo', 'rb')
		except:
			retorno['text'] = 'Conta inexistente!'
			return

		saldo = float(pickle.load(path))

		if valor <= 0:
			retorno['text'] = ValorInvalidoError()
		elif float(valor) > float(saldo):
			retorno['text'] = SaldoInsuficienteError()
		else:
			retorno['text'] = 'Saque efetuado com sucesso!'
			path = open('contas/' + user + '_saldo', 'wb')
			pickle.dump(str( float(saldo) - float(valor) ), path)
			path.close()

			path = open('contas/' + user, 'ab')
			pickle.dump('R$ ' + valor + ' (Saque)', path)
		
