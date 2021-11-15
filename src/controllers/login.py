import os
projectPath = os.path.abspath('main.py').replace('\main.py', '')
import sys
sys.path.append(projectPath)

from src.controllers.cadastro import Cadastro
from src.banco.repositories.FuncionarioDomRepository import FuncionarioRepository as repository
from src.model.FuncionarioDomModel import FuncionarioDomModel
from src.enums.FuncionarioDomEnum import FUNCIONARIO_ENUM
from src.recognizer.regonizer import Recognizer
from src.controllers.reports import ReportController

class Login:
    
    def __init__(self, ):
        self._repository = repository()
        self._cpfList = []
        self._cadastro = Cadastro()
        self._recognizer = Recognizer()
        self._reportController = ReportController()
        listFunc = self._repository.findAll()        
        
        for func in listFunc:
            self._cpfList.append(func.getCpf())

    # -> Realiza a ção do login
    def loginAction(self, ):
        print('============================================')   
        print('==== LOGIN DE FUNCIONARIO: .................')
        print('============================================')
        print('...')
        cpf = str(input('[INPUT] --- CPF: '))
        
        if(cpf in self._cpfList):
            
            func:FuncionarioDomModel = self._repository.findByCampo(FUNCIONARIO_ENUM.CPF.value, cpf)
            print('[SISTEMA] --- Iniciado reconhecimento no funcionário: ' + func.getNome())
            isAutenticado, confianca = self._recognizer.getAutenticacao(func = func)
             
            if(isAutenticado == True):
                print('[SISTEMA] --- Bem vindo {}!'.format(func.getNome()))
                print('[SISTEMA] --- Usuário autenticado com uma confianca de:  {}'.format(str(confianca)))
                
                # -> Action de reports
                self._reportController.getReportAction(func)

            else:
            
                while(True):    
                    print('[SISTEMA] --- A autenticação facial falhou. Deseja tentar novamente ?')
                    selectValue = input('[SISTEMA] --- Informe [1] para tentar novamente e [2] para sair do sistema')

                    if(int(selectValue) == 1):
                        print('[SISTEMA] --- Iniciado reconhecimento no funcionário: ' + func.getNome())
                        isAutenticado, confianca = self._recognizer.getAutenticacao(func = func)
                        
                        if(isAutenticado == True):
                            print('[SISTEMA] --- Bem vindo {}!'.format(func.getNome))
                            print('[SISTEMA] --- Usuário autenticado com uma confianca de:  {}'.format(str(confianca)))
                    
                            # -> Action de Reports
                            self._reportController.getReportAction(func)
                        
                    elif(int(selectValue) == 2):
                        print('[INFO] --- Fechando sistema...')
                        exit
                    else:
                        print('[ERRO] --- Comando invalido. Fechando sistema...')
                        exit
        else:
            print('[ERRO] --- CPF não cadastrado ')
            value = int(input('[SISTEMA] --- Aperte [1] para cadastrar e [2] para sair do sistema:  '))

            if(value == 1):
                self._cadastro.cadastroAction()
            else:
                exit