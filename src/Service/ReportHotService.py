#Templates de Report
# -> Retornar uma lista de json's de REPORT, cada campo vai exportar os dados de acordo com seus respectiveis niveis 
import src.server.db as db 

class ReportHotService():

    def __init__(self, ):
        self._cursor = db.getCursor()

    #Nivel 1
    # -> Campos a retornar: 
    #       NOME_EMPRESA, NUMERO_EMPRESA, ENDERECO_EMPRESA
    def getReportNivel_1(self):
        pass


    #Nivel 2
    # -> Campos a retornar: 
    #       NOME_EMPRESA, NUMERO_EMPRESA, ENDERECO_EMPRESA, CNPJ, DONO_EMPRESA, GRAVIDADE
    def getReportNivel_2(self, ):
        pass


    #Nivel 3
    # -> Campos a retornar: 
    #       NOME_EMPRESA, NUMERO_EMPRESA, ENDERECO_EMPRESA, CNPJ, DONO_EMPRESA, GRAVIDADE, TIPO_DANO, TIPO_AGROTOX, QT_AGROTOX
    def getReportNivel_3(self, ):
        pass