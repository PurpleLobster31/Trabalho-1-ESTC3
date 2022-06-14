class Projeto:

    def __init__(self, nome, dataInicio, dataTermino, tempoEstimado, valorEstimado, funcionarioResponsavel):
        self.__nome = nome
        self.dataInicio = dataInicio
        self.dataTermino = dataTermino
        self.tempoEstimado = tempoEstimado
        self.valorEstimado = valorEstimado
        self.funcionarioResponsavel = funcionarioResponsavel

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome