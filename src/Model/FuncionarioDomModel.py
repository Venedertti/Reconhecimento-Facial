#Objeto do Funcionario
# -> TAPS_DOM_FUNC

class FuncionarioDomModel():    

    def __init__(self, ):
        self._id:str = None
        self._cpf:str = None
        self._nome:str = None
        self._numero:str = None
        self._email:str = None
        self._cargo:str = None
        self._id_nivel:int = None

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
    