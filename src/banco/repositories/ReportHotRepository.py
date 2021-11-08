import os
projectPath = os.path.abspath('main.py').replace('\main.py', '')
import sys
sys.path.append(projectPath)

from src.model.ReportHotModel import ReportHotModel
from src.banco.db import Banco
from src.enums.ReportHotEnum import REPORT_ENUM

class ReportRepository():

    def __init__(self, ):
        self._banco = Banco()
        self._cursor = self._banco.getCursor()

    campo_id = REPORT_ENUM.ID.value
    campo_nome_empre = REPORT_ENUM.NOME_EMPRE.value
    campo_numero_empre = REPORT_ENUM.NUMERO_EMPRE.value
    campo_endereco = REPORT_ENUM.EDENRECO.value
    campo_dono = REPORT_ENUM.DONO.value
    campo_gravidade = REPORT_ENUM.GRAVIDADE.value
    campo_tipo_dano = REPORT_ENUM.TIPO_DANO.value
    campo_tipo_agro = REPORT_ENUM.TIPO_AGRO.value
    campo_qt_agro = REPORT_ENUM.QT_AGRO.value

    def validateNoneValue(self, campo):
        try:
            return campo
        except NameError:
            return '' 

    def mapper(self, row):
        funcRow = ReportHotModel()
                
        funcRow.setId(int(row[0]))
        funcRow.setNomeEmpresa(str(row[1]))
        funcRow.setNumEmpresa(str(row[2]))
        funcRow.setEndereco(str(row[3]))
        funcRow.setGravidade(str(row[4]))
        funcRow.setTipoDano(str(row[5]))
        funcRow.setTipoAgro(str(row[6]))
        funcRow.setQtdAgro(str(row[7]))

        return funcRow

    def findByCampo(self, campo, value):
        query = 'SELECT * FROM TAPS_HOT_REPORT WHERE {} = "{}"'.format(str(campo), str(value))
        self._cursor.execute(query)
        
        records = self._cursor.fetchall()
        rowCount = len(records)
        
        if(rowCount == 0):
            return ReportHotModel()
        
        elif(rowCount == 1):
            func = self.mapper(records[0])                
            return func
        
        else:    
            funcList = []
            for row in records:
                funcRow = self.mapper(row)
                funcList.insert(funcRow)

            return funcList


    def findAll(self, ):
        query = 'SELECT * FROM TAPS_HOT_REPORT'
        self._cursor.execute(query)

        records = self._cursor.fetchAll()
        funcList = []

        for row in records:
            funcRow = self.mapper(row)
            funcList.insert(funcRow)

        return funcList

    def save(self, report:ReportHotModel):
        
        queryInsert = 'INSERT INTO TAPS_HOT_REPORT( {}, {}, {}, {}, {}, {}, {}) '.format(
            self.campo_nome_empre, self.campo_numero_empre, self.campo_endereco, self.campo_dono, self.campo_gravidade, self.campo_tipo_dano,
            self.campo_tipo_agro, self.campo_qt_agro
        )

        value_nome = self.validateNoneValue(report.getNomeEmpresa)
        value_numero_empre = self.validateNoneValue(report.getNumEmpresa())
        value_endereco = self.validateNoneValue(report.getEndereco)
        value_dono = self.validateNoneValue(report.getDonoEmpresa)
        value_gravidade = self.validateNoneValue(report.getGravidade())
        value_tipo_dano = self.validateNoneValue(report.getTipoDano())
        value_tipo_agro = self.validateNoneValue(report.getTipoAgro())
        value_qt_agro = self.validateNoneValue(report.getQtdAgro())

        queryValue = 'VALUES ("{}, "{}", "{}", "{}", "{}", "{}", "{}")'.format(
            value_nome, value_numero_empre, value_endereco, value_dono, value_gravidade, value_tipo_dano, value_tipo_agro, value_qt_agro
        )

        query = queryInsert + queryValue
        
        self._cursor.execute(query)
        self._banco.commit()