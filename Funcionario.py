class Funcionario(object):

    def __init__(self, numFuncional, nome, salario, email):
        self.__numFuncional = numFuncional
        self.nome = nome
        self.salario = salario
        self.email = email
    
    @property
    def numFuncional(self):
        return self.__numFuncional

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
    
    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, salario):
        self._salario = salario
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email