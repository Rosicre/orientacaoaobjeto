from ContasBancos import ContaCorrente, CartaoCredito
from Agencia import AgenciaPremium, AgenciaComum, AgenciaVirtual


#programa
#conta_Rosicre = ContaCorrente('Rosicre_Ferreira', '819.550.611-15', 12345, 32861)

#Ecartao_Rosicre = CartaoCredito('Rosicre_Ferreira', conta_Rosicre)

#conta_Rosicre.nome = 'Ferreira'
#print(conta_Rosicre.nome)

#cartao_Rosicre.senha = '4455'
#print(cartao_Rosicre.senha)

#print(conta_Rosicre.__dict__)
#print(cartao_Rosicre.__dict__) 

agencia_premium_especial = AgenciaPremium(999581221, 33355511121)
print(agencia_premium_especial.caixa)