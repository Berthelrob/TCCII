from ps import Geradadosps

class Ps:
    def __init__(self):
        self.identificador
        self.habilidade 
        self.kpi1hist = {}
        self.kpi2hist = {}
        self.kpi3hist = {}
        self.kpi4hist = {}
        self.mediaexpkpi1
        self.mediaexpkpi2
        self.mediaexpkpi3
        self.mediaexpkpi4
    pass

    def calcular_ewa (self):
        #vetor_somatorios_kpi_ewa = [] # lista vazia   
        w = 0.25
        for i in range(self.qnt_kpi):
            temp_divisor = 0.0
            temp_dividendo = 0.0 
            for j in range(self.qnt_historicos):
                divisor = (self.matriz_historico[i][j]*(w*(j+1)))
                temp_divisor = divisor+temp_divisor
                dividendo = (w*(j+1))
                temp_dividendo = dividendo+temp_dividendo
            #return self.vetor_somatorios_kpi_ewa
            self.vetor_somatorios_kpi_ewa.append(temp_divisor/temp_dividendo)
        return self.vetor_somatorios_kpi_ewa

