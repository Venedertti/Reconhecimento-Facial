#Objeto associativo de Nivel e Funcionário
# -> TAPS_ASS_FUNC_NIVEL
# Apenas get

class NivelFuncAssModel:
    _id_func    : int
    _id_nivel   : int

    def __init__(self, idFunc, idNivel):
        self._id_func   = idFunc
        self._id_nivel  = idNivel

    def getIdFunc(self, ):
        return self._id_func

    def getIdNivel(self, ):
        return self._id_nivel