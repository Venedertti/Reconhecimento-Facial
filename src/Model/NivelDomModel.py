#Objeto de Nível
# -> TAPS_DOM_NIVEL

class NivelDom():
    _id         : int
    _descricao  : str

    def __init__(self, id):
        self._id = id

    def getId(self, ):
        return self._id
    
    def setId(self, id):
        self._id = id

    def getDescricao(self, ):
        return self._id
    
    def setDescricao(self, descricao):
        self._descricao = descricao