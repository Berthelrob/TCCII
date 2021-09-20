import random

class Kpi:

    def __init__(self,qnt_kpi,qnt_historicos,identificador):
        self.identificador = identificador
        self.qnt_historicos = qnt_historicos
        self.qnt_kpi = qnt_kpi
        self.kpi_nao_tratado = []
        self.kpi_tratado = []
    pass

    def trata_historico(self):  
        print("Entrou no trata_historico")
        w = 0.25
        divisor = 0.0
        dividendo = 0.0
        for i in range(self.qnt_kpi):
            for j in range(self.qnt_historicos):
                divisor = self.kpi_nao_tratado[j]*(w*j+1) + divisor
                dividendo = (w*j+1) + dividendo
            self.kpi_tratado = self.kpi_tratado + divisor/dividendo
        
    def gerar_dados_kpi(self):
        print("Entrou no gerar_dados_kpi")
        for identificador in range(self.qnt_kpi):
            kpi_historico = []
            for historico in range(self.qnt_historicos):
                kpi_historico.append(round(random.random(),2))
            self.kpi_nao_tratado = self.kpi_nao_tratado + kpi_historico
        self.trata_historico()
  
