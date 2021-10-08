# Objeto AgroToxico
# -> TAPS_DOM_AGRO

class AgroToxicoModel():
    _id             : int
    _categoria      : str
    _descricao      : str
    _efeito_oral    : str
    _efeito_dermic  : str
    _efeito_inalar  : str

    def __init__(self, id):
        self.id = id

    def getId(self, ):
        return self._id
    
    def setId(self, id):
        self._id = id
    
    def getCategoria(self, ):
        return self._categoria
    
    def setCategoria(self, categoria):
        self._categoria = categoria
    
    def getDescricao(self, ):
        return self._descricao
    
    def setDescricao(self, descricao):
        self._descricao = descricao
    
    def getEfeitoOral(self, ):
        return self._efeito_oral
    
    def setEfeitoOral(self, efeito_oral):
        self._efeito_oral = efeito_oral
    
    def getEfeitoDermico(self, ):
        return self._efeito_dermic
    
    def setEfeitoDermico(self, efeito_dermic):
        self._efeito_dermic = efeito_dermic
    
    def getEfeitoInalar(self, ):
        return self._efeito_inalar
    
    def setEfeitoInalar(self, efeito_inalar):
        self._efeito_inalar = efeito_inalar
    