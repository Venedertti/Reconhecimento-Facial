#Objeto Report
# -> TAPS_HOT_REPORT

class  ReportHotModel():
    _id         : int
    _empre_nome : str
    _empre_num  : str
    _endereco   : str
    _empre_dono : str
    _gravidade  : int
    _tipo_dano  : str
    _tipo_agro  : str
    _qtd_agro   : int

    def __init__(self, id):
        self._id = id

    def getId(self, ):
        return self._id
    
    def setId(self, id):
        self._id = id
    
    def getNomeEmpresa(self, ):
        return self._empre_nome

    def setNomeEmpresa(self, nomeEmpresa):
        self._empre_nome = nomeEmpresa

    def getNumEmpresa(self, ):
        return self._empre_num
    
    def setNumEmpresa(self, numEmpresa):
        self._empre_num = numEmpresa

    def getEndereco(self, ):
        return self._endereco

    def setEndereco(self, endereco):
        self._endereco = endereco

    def getDonoEmpresa(self, ):
        return self._empre_dono

    def setDonoEmpresa(self, donoEmpresa):
        self._empre_dono = donoEmpresa

    def getGravidade(self, ):
        return self._gravidade

    def setGravidade(self, gravidade):
        self._gravidade = gravidade

    def getTipoDano(self, ):
        return self._tipo_agro
    
    def setTipoDano(self, tipoDano):
        self._tipo_dano = tipoDano
    
    def getTipoAgro(self, ):
        return self._tipo_agro

    def setTipoAgro(self, tipoAgro):
        self._tipo_agro = tipoAgro

    def getQtdAgro(self, ):
        return self._qtd_agro

    def setQtdAgro(self, qtdAgro):
        self._qtd_agro = qtdAgro
    
