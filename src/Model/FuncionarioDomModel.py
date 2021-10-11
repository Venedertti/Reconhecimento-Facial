#Objeto do Funcionario
# -> TAPS_DOM_FUNC

class FuncionarioDomModel():
    _id         : str
    _cpf        : str
    _nome       : str
    _numero     : str
    _email      : str
    _cargo      : str
    _id_nivel   : int
    _identific  : str

    def __init__(self, id):
        self._id = id

    def getId(self, ):
        return self._id

    def setId(self, id):
        self._id = id

    def getCpf(self, ):
        return self._cpf
    
    def setCpf(self, cpf):
        self._cpf = cpf

    def getNome(self, ):
        return self._nome
    
    def setNome(self, nome):
        self._nome = nome

    def getNumero(self, ):
        return self._numero

    def setNumero(self, numero):
        self._numero = numero

    def getEmail(self, ):
        return self._email

    def setEmail(self, email):
        self._email = email

    def getCargo(self, ):
        return self._cargo

    def setCargo(self, cargo):
        self._cargo = cargo

    def getIdNivel(self, ):
        return self._id_nivel
    
    def setIdNivel(self, idNivel):
        self._id_nivel = idNivel
    
    def getIdentific(self, ):
        return self._identific
    
    def setIdentific(self, identific):
        self._identific = identific