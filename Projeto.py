class Projeto:

    def __init__(self, nome, dataInicio, dataTermino, tempoEstimado, valorEstimado, funcionarioResponsavel, finalizado):
        self.__nome = nome
        self.dataInicio = dataInicio
        self.dataTermino = dataTermino
        self.tempoEstimado = tempoEstimado
        self.valorEstimado = valorEstimado
        self.funcionarioResponsavel = funcionarioResponsavel
        self.finalizado = finalizado

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def dataInicio(self):
        return self._dataInicio
    
    @dataInicio.setter
    def dataInicio(self, dataInicio):
        self._dataInicio = dataInicio
    
    @property
    def finalizado(self):
        return self._finalizado

    @finalizado.setter
    def finalizado(self, finalizado):
        self._finalizado = finalizado

    @property
    def dataTermino(self):
        return self._dataTermino

    @dataTermino.setter
    def dataTermino(self, dataTermino):
        self._dataTermino = dataTermino
    
    @property
    def tempoEstimado(self):
        return self._tempoEstimado

    @tempoEstimado.setter
    def tempoEstimado(self, tempoEstimado):
        self._tempoEstimado = tempoEstimado
    
    @property
    def valorEstimado(self):
        return self._valorEstimado

    @valorEstimado.setter
    def valorEstimado(self, valorEstimado):
        self._valorEstimado = valorEstimado

    @property
    def funcionarioResponsavel(self):
        return self._funcionarioResponsavel

    @funcionarioResponsavel.setter
    def funcionarioResponsavel(self, funcionarioResponsavel):
        self._funcionarioResponsavel = funcionarioResponsavel

    