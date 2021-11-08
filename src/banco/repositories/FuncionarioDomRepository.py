import os
projectPath = os.path.abspath('main.py').replace('\main.py', '')
import sys
sys.path.append(projectPath)

from src.enums.FuncionarioDomEnum import FUNCIONARIO_ENUM
from src.model.FuncionarioDomModel import FuncionarioDomModel
from src.banco.db import Banco

class FuncionarioRepository:

    def __init__(self, ):
        self._banco = Banco()
        self._cursor = self._banco.getCursor()
        
    # -> Os nomes do campos são guardados no Enum: FUNCIONARIO_ENUM para boas práticas
    campo_id = FUNCIONARIO_ENUM.ID.value # ->Não utilizado no insert pois é AUTO_INCREMENT
    campo_cpf = FUNCIONARIO_ENUM.CPF.value
    campo_nome = FUNCIONARIO_ENUM.NOME.value
    campo_numero = FUNCIONARIO_ENUM.NUMERO.value
    campo_email = FUNCIONARIO_ENUM.EMAIL.value
    campo_cargo = FUNCIONARIO_ENUM.CARGO.value
    campo_nivel = FUNCIONARIO_ENUM.NIVEL.value
    campo_ident = FUNCIONARIO_ENUM.IDENTIFC.value

    def validateNoneValue(self, campo):
        try:
            return campo
        except NameError:
            return '' 

    def mapper(self, row):
        funcRow = FuncionarioDomModel()
                
        funcRow.setId(str(row[0]))
        funcRow.setCpf(str(row[1]))
        funcRow.setNome(str(row[2]))
        funcRow.setNumero(str(row[3]))
        funcRow.setEmail(str(row[4]))
        funcRow.setCargo(str(row[5]))
        funcRow.setIdNivel(int(row[6]))

        return funcRow

    def findByCampo(self, campo, value):
        query = 'SELECT * FROM TAPS_DOM_FUNC WHERE {} = "{}"'.format(str(campo), str(value))
        self._cursor.execute(query)
        
        records = self._cursor.fetchall()
        rowCount = len(records)
        
        if(rowCount == 0):
            return FuncionarioDomModel()
        
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
        query = 'SELECT * FROM TAPS_DOM_FUNC'
        self._cursor.execute(query)
        
        records = self._cursor.fetchall()
        funcList = []

        for row in records:
            funcRow = self.mapper(row)
            funcList.append(funcRow)

        return funcList

    def save(self, func:FuncionarioDomModel):
        
        queryInsert = 'INSERT INTO TAPS_DOM_FUNC( {}, {}, {}, {}, {}, {}) '.format(
            self.campo_cpf, self.campo_nome, self.campo_numero, self.campo_email, self.campo_cargo, self.campo_nivel
        )

        #value_id = func.getId() if func.getId() != None else None   # ->Não utilizado no insert pois é AUTO_INCREMENT
        value_cpf = self.validateNoneValue(func.getCpf())
        value_nome = self.validateNoneValue(func.getNome())
        value_numero = self.validateNoneValue(func.getNumero())
        value_email = self.validateNoneValue(func.getEmail())
        value_cargo = self.validateNoneValue(func.getCargo())
        value_nivel = self.validateNoneValue(func.getIdNivel())
       
        queryValue = 'VALUES ("{}", "{}", "{}", "{}", "{}", "{}")'.format(
            value_cpf, value_nome, value_numero, value_email, value_cargo, value_nivel
        )

        query = queryInsert + queryValue
        
        self._cursor.execute(query)
        self._banco.commit()


