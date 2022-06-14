class Funcionario:

    def __init__(self, numFuncional, nome, salario, email):
        self.__numFuncional = numFuncional
        self.nome = nome
        self.salario = salario
        self.email = email
    
    @property
    def numFuncional(self):
        return self.__numFuncional

    @numFuncional.setter
    def numFuncional(self, numFuncional):
        self.__numFuncional = numFuncional