from datetime import datetime
import re
from tkinter.messagebox import NO
import pytz
from random import randint # Para criar números aleatórios mais simples, com a biblioteca numpy também podemos criar. 


class ContaCorrente:
    """
    Cria um objeto ContaCorrente para gerenciar as contas dos clientes:

    Atributos:
        nome: Nome do Cliente
        cpf: CPF do Cliente
        agencia: Agencia Responsavel pela conta do Cliente
        numero_conta: Numero da Conta Corrente do Cliente
        saldo: Saldo disponível na conta do Cliente
        limite: Limite do Cheque especial daquele Cliente
        transacoes: Histórico de Transacoes do Cliente
    """


    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime( '%d/%m/%Y   %H:%M:%S' )


    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self._saldo = 0
        self._limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self._transacoes = []
        self.cartoes = []

    def consultar_saldo(self):   
        print('Seu saldo atual é de R$ {:,.2f}'.format(self._saldo))

    def depositar(self, valor):
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):
        self._limite = -1000
        return self._limite    

    def sacar_dinheiro(self, valor):
        if self._saldo - valor < self._limite_conta():
            print('Você não tem saldo suficiente para sacar este valor')            
        else:
            self._saldo -= valor
            self._transacoes.append((-valor,self._saldo, ContaCorrente._data_hora()))

    def consultar_limite_chequeespecial(self):
        print('Seu limite de Cheque Especial é de R$ {:,.2f}'.format(self._limite_conta()))

    def consultar_historico_transacoes(self):
        print('Histórico de Transações:')
        print('Valor, Saldo, Data e Hora')
        for  transacao in self._transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))


class CartaoCredito:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = ' {} / {}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4) 
        self.cod_seguranca = ' {}{}{} '.format(randint(0,9), randint(0,9), randint(0,9))
        self.limite = 1000
        self._senha = '1234'
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

    
    @property #Para restringir que a senha so pode ser mudada através de uma classe método getter
    def senha(self):
        return self._senha

    @senha.setter #Para restringir que a senha so pode ser mudada através de uma classe método setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print('Nova Senha Inválida')



           