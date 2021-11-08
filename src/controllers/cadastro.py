import os
projectPath = os.path.abspath('main.py').replace('\main.py', '')
import sys
sys.path.append(projectPath)

from src.model.FuncionarioDomModel import FuncionarioDomModel
from src.banco.repositories.FuncionarioDomRepository import FuncionarioRepository 
from src.recognizer.captura import Captura
from src.recognizer.treinamento import Treinamento
from src.enums.FuncionarioDomEnum import FUNCIONARIO_ENUM
from src.controllers.reports import ReportController

class Cadastro():
    
    def __init__(self, ):
        self._repository = FuncionarioRepository()
        self._captura = Captura()
        self._treinamento = Treinamento()
        self._reportController = ReportController()

    # -> Realiza a ação de cadastro
    def cadastroAction(self, ):
        print('============================================')   
        print('==== CADASTRO DE FUNCIONARIO:    ===========')
        print('============================================')
        print('...')
        cpf = str(input('[INPUT]...CPF: '))
        nome = str(input('[INPUT]...Nome: '))
        numero = str(input('[INPUT]...Numero: '))
        email = str(input('[INPUT]...E-mail: '))
        cargo = str(input('[INPUT]...Cargo: '))
        nivel = int(input('[INPUT]...Nivel: '))

        model = FuncionarioDomModel()

        model.setCpf(cpf)
        model.setNome(nome)
        model.setNumero(numero)
        model.setEmail(email)
        model.setCargo(cargo)
        model.setIdNivel(nivel)

        self._repository.save(model)

        # -> Inicio de Captura e Treinamento Facial
        print('[INFO] --- Iniciando captura de faces.')
        print('[INFO] ---  Favor apertar "Q" para captura. Total de fotos a ser tiradas: 25')

        # -> Necessário realizar consulta pois o ID é gerado pelo banco
        savedModel:FuncionarioDomModel = self._repository.findByCampo(FUNCIONARIO_ENUM.CPF.value, cpf)

        print(savedModel.getId())
        # self._captura.capturaCadastro(savedModel.getId)
        # print('[INFO] --- Captura de faces concluida!')

        # print('[INFO] --- Iniciando treinamento de faces.')
        # self._treinamento.treinarFisherFace(savedModel.getId())
        # print('[INFO] --- Treinamento de faces concluida!')
        
        print("[SISTEMA] --- Abrindo tela de Reports... ")
        self._reportController.getReportAction(savedModel)

