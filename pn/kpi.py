class Kpi:
    def __init__(self,identificador, historico):
        self.identificador = identificador
        self.valor = historico
    pass

    @property
    def historico(self):
         return self._historico

    @historico.setter
    def historico(self, historico):
         self._historico= historico    