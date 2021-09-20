#!/python/python
#import pyanp
import random
#import numpy
from ps.geradadosps import Geradadosps
from pn.geradadospn import Geradadospn

if __name__== "__main__":

    print("-------------Trabalho de TCC 2 - Analisador de risco utilizando AHP/ANP---------------\n")
    print("------------------------Desenvolvido por Robson Berthelsen----------------------------\n")
    print("-------------------------------Data:19/09/2021----------------------------------------\n")

    qnt_ps = 3
    qnt_pn = 0
    ps = []

    print("Criando Provedores de Serviços:\n")
    print("Quantidade de PS's: ",qnt_ps)

    #Cria lista de PS's

    ##Criar metodo que cria uma lista de objetos de PS e alterar nome da classe geradadosPS para PS
    #for i in range(qnt_ps):
    #    ps.append(Geradadospn(i,qnt_ps))
    ps1 = Geradadospn(1,qnt_ps)
    #Fazer count para saber quantos PS's possuem a mesma habilidade. Se count <=1, então é impossível de formar uma OV. Caso contrário, executar AHP
