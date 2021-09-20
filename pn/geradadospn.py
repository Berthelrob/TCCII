from ps.kpi import Kpi
import random

class Geradadospn:
    def __init__(self,nome_arquivo,identificador):
        self.nome_arquivo = nome_arquivo
        self.identificador = identificador
    #    self.habilidade = habilidade
        self.qnt_historicos = 10
        self.qnt_kpi = 4
        self.kpi_ewa = 0
    pass

    def gerar_historicokpi(self,kpi_identificador):
        kpi_historico = []
        for i in range(self.qnt_historicos):
            kpi_historico.append(round(random.random(),2))
        kpi = Kpi(kpi_identificador,kpi_historico)
        return kpi

    def trata_historico(self,historico_kpi):
        #vetor_somatorios_kpi_ewa = [] # lista vazia   
        w = 0.25
        divisor = 0.0
        dividendo = 0.0
        for i in range(self.qnt_historicos):
            #print(historico_kpi.valor[i])
            divisor = historico_kpi.valor[i]*(w*i+1) + divisor
            dividendo = (w*i+1) + dividendo
        self.kpi_ewa = divisor/dividendo
        return self.kpi_ewa