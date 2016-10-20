#coding: utf-8

class SaldoInsuficienteError(Exception):

    def __str__(self):
        return "Saldo insuficiente!"

class ValorInvalidoError(Exception):

    def __str__(self):
        return "Valor informado é inválido!"
