import os
projectPath = os.path.abspath('main.py').replace('\main.py', '')
import sys
sys.path.append(projectPath)

from src.model.AgroToxicoHotModel import AgroToxicoModel
from src.banco.db import Banco
from src.enums.AgroToxicoHotEnum import AGROTOX_ENUM

class AgroToxRepository:
    
    def __init__(self, ):
        self._banco = Banco()
        self._cursor = self._banco.getCursor()

    campo_id = AGROTOX_ENUM.ID_AGRO.value
    campo_categoria = AGROTOX_ENUM.CATEGORIA.value
    campo_descricao = AGROTOX_ENUM.DESC_AGRO.value
    campo_efeito_oral = AGROTOX_ENUM.EFEITO_ORAL.value
    campo_efeito_dermico = AGROTOX_ENUM.EFEITO_DERM.value
    campo_efeito_inalar = AGROTOX_ENUM.EFEITO_INALAR.value

    def validateNoneValue(self, campo):
        try:
            return campo
        except NameError:
            return '' 

    def mapper(self, row):
        agroRow = AgroToxicoModel()

        agroRow.setId(row[0])
        agroRow.setCategoria(row[1])
        agroRow.setDescricao(row[2])
        agroRow.setEfeitoOral(row[3])
        agroRow.setEfeitoDermico(row[4])
        agroRow.setEfeitoInalar(row[5])
               
        return agroRow

    def findByCampo(self, campo, value):
        query = 'SELECT * FROM TAPS_DOM_AGRO WHERE {} = "{}"'.format(str(campo), str(value))
        self._cursor.execute(query)
        
        records = self._cursor.fetchall()
        rowCount = len(records)
        
        if(rowCount == 0):
            return AgroToxicoModel()
        
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
        query = 'SELECT * FROM TAPS_DOM_AGRO'
        self._cursor.execute(query)
        
        records = self._cursor.fetchAll()
        agroList = []

        for row in records:
            agroRow = self.mapper(row)
            agroList.insert(agroRow)

        return agroRow

    