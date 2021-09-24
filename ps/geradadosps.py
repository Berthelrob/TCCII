from ps.kpi import Kpi
import random

class Geradadosps:
    def __init__(self,identificador,qnt_ps):
 #       self.nome_arquivo = nome_arquivo
        self.identificador = identificador
        self.habilidade = random.randint(1,qnt_ps/3)
        self.qnt_kpi = 4
        self.qnt_historico = 10
        pass

    def gerar_dados_kpi(self):
        kpi = Kpi()
        w = 0.25
        divisor = 0.0
        dividendo = 0.0

        print("Entrou no gerar_dados_kpi")
        for identificador in range(self.qnt_kpi):
            kpi_historico = []
            for historico in range(self.qnt_historicos):
                kpi_historico.append(round(random.random(),2))
            kpi.kpi_nao_tratado = kpi.kpi_nao_tratado + kpi_historico

        for i in range(self.qnt_kpi):
            for j in range(self.qnt_historicos):
                divisor = kpi.kpi_nao_tratado[j]*(w*j+1) + divisor
                dividendo = (w*j+1) + dividendo
            kpi.kpi_tratado = kpi.kpi_tratado + divisor/dividendo
        


