from random import randint


class Agencia:


    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print ('Caixa abaixo do nível recomendado. Caixa Atual: R$ {:,.2f} de Reais '.format(self.caixa))
        else:
            print (' O Valor de Caixa está ok. Caixa Atual: R$ {:,.2f} de Reais '.format(self.caixa))

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Empréstimo não é possível. Dinheiro não disponível em caixa')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


class AgenciaVirtual(Agencia):

    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 3210)
        self.caixa = 1000000 
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor

    def sacar_paypal(self, valor):
        self.caixa_paypal -= valor
        self.caixa += valor


    
    
class AgenciaComum(Agencia):
    
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero = randint(1001 , 9999))
        self.caixa = 1000001

    

class AgenciaPremium(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero = randint(1001 , 9999))
        self.caixa = 2000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print('O Cliente não tem o Patrimônio mínimo necessário para entrar na Agência Premium')

       

if __name__ == '__main__':
    
    agencia1 = Agencia(999541521, 11133344425, 4568)

    agencia_virtual = AgenciaVirtual('www.agenciavirtual.com.br', 91221212115, 88811166612)
    agencia_virtual.verificar_caixa()
    agencia_comum = AgenciaComum(999541444, 11133344000)
    agencia_premium = AgenciaPremium(55500044415, 11133344000)

    agencia_virtual.depositar_paypal(20000)
    print(agencia_virtual.caixa)
    print(agencia_virtual.caixa_paypal)
        
    agencia_premium.adicionar_cliente('Rosicre', 11155544545, 50000000)
    print(agencia_premium.clientes)

    agencia_comum.adicionar_cliente('Irmão do Rosicre', 88844455652, 10)
    print(agencia_comum.clientes)

