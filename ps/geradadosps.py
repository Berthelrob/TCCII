from ps.kpi import Kpi
import random

class Geradadosps:
    def __init__(self,identificador,qnt_ps):
 #       self.nome_arquivo = nome_arquivo
        self.identificador = identificador
        self.habilidade = random.randint(1,qnt_ps/3)
        self.qnt_kpi = 4
        self.qnt_historico = 10
        self.kpi_tratado = []
    pass

    def kpis_do_ps(self):
        kpi = Kpi(self.qnt_kpi, self.qnt_historico)
        kpi.inicia_e_trata_historico()

    ##Gerar 4 vezes dados KPI's
    #Criar metodo para pegar e atribuir valor gerado pelo gerar_dados_kpi e incluir em variável local na classe geradadosps


