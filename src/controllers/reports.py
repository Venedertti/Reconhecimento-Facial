import os
projectPath = os.path.abspath('main.py').replace('\main.py', '')
import sys
sys.path.append(projectPath)

from enums.AgroToxicoHotEnum import AGROTOX_ENUM
from src.model.FuncionarioDomModel import FuncionarioDomModel
from src.model.ReportHotModel import ReportHotModel
from src.banco.repositories.ReportHotRepository import ReportRepository
from src.enums.ReportHotEnum import REPORT_ENUM
from src.banco.repositories.AgroToxicoHotRepository import AgroToxRepository

class ReportController():

    def __init__(self, ):
        self._repository = ReportRepository()
        self._agroRepository = AgroToxRepository()
        home = os.path.expanduser('~')
        self._documentPath = os.path.join(home, 'Documents')

    def getReportAction(self, func:FuncionarioDomModel):
        self._func = func

        print('============================================')   
        print('==== Central de Reports: ...................')
        print('============================================')

        print('...')
        print('[INFO] --- Selecione [0] para listar todos os Reports')
        print('[INFO] --- Selecione [1] para cadastrar um novo Report')
        print('[INFO] --- Selecione [2] para gerar um relatório de um Report')
        print('[INFO] --- Selecione [3] para gerar export massivo')
        print('[INFO] --- Selecione [4] para gerar export massivo por filtro')
        print('[INFO] --- Selecione outro botão para sair do sistema')
        print('...')
        selectedValue = input('[INPUT] --- Selecionar valor: ')

        if(selectedValue == 0):
            self.listReports()
        elif(selectedValue == 1):
            self.cadastroReport(func.getIdNivel())
        elif(selectedValue == 2):
            self.gerarRelatorio(func.getIdNivel())
        elif(selectedValue == 3):
            self.gerarRelatorioMassivo(func.getIdNivel(), selectedValue)
        elif(selectedValue == 4):
            self.gerarRelatorioMassivo(func.getIdNivel(), selectedValue)
        else:
            exit

    def listReports(self, ):
        print('============================================')   
        print('===============   REPORTS   ================')
        print('============================================')
        print('...')
        
        listReports = self._repository.findAll()

        for report in listReports:
            report:ReportHotModel
            print('[REPORT] --- ID REPORT: {} | NOME EMPRESA: {} | NOME AGROTOX: {}'.format(report.getId(),
                                                                                            report.getNomeEmpresa(),
                                                                                            report.getNomeAgro()))

        print('[INFO] --- Todos reports listados.')
        print('...')
        self.getReportAction()

    def cadastroReport(self, ):
        nivel = self._func.getIdNivel()
        print('============================================')   
        print('=========== CADASTRO DE REPORT:   ==========')
        print('============================================')
        print('...')

        nomeEmpresa = input('[INPUT] --- Nome da empresa: ')
        numeroEmpresa = input('[INPUT] --- Numero da empresa: ')
        endereco = input('[INPUT] --- Endereço do local afetado: ')
        dono = input('[INPUT] --- Nome do dono da empresa: ')
        gravidade = int(input('[INPUT] --- Gravidade: '))
        tipo_dano = input('[INPUT] --- Tipo de dano: ')
        tipo_agro = input('[INPUT] --- Tipo de agro: ')
        qt_agro = int(input('[INPUT] --- Quantidade agrotóxico'))
        
        report = ReportHotModel()

        report.setNomeEmpresa(nomeEmpresa)
        report.setNumEmpresa(numeroEmpresa)
        report.setEndereco(endereco)
        report.setDonoEmpresa(dono)
        report.setGravidade(gravidade)
        report.setTipoDano(tipo_dano)
        report.setTipoAgro(tipo_agro)
        report.setQtdAgro(qt_agro)

        if(nivel > 1):
            self._repository.save(report)
            print('[INFO] --- Report salvo com sucesso!')
        else:
            print('[INFO] --- Funcionario sem permissão para cadastro!')
            exit

    def gerarRelatorio(self, idNivel:int):
        funcName:str = self._func.getNome()
        idNivel:int = self._func.getIdNivel()
        msgSemPermissao = '[INFO] - SEM PERMISSÃO'
        dadosReport = ''

        idReport = input('[INPUT] --- Insira o codigo do REPORT: ')
        report = self._repository.findByCampo(REPORT_ENUM.ID.value, idReport)
        
        # -> Open template massivo
        with open('rsc/templates/REPORT_UNITARIO.txt') as f:
            lines = f.readlines()
        
        for index in range(0, len(lines)):
            dadosReport += str(lines[index])

        agroTox = self._agroRepository.findByCampo(AGROTOX_ENUM.ID_AGRO.value, report.getTipoAgro())

        dadosReport = dadosReport.replace(REPORT_ENUM.TAG_ID_RELATORIO.value, report.getId())
        dadosReport = dadosReport.replace(REPORT_ENUM.TAG_NOME_FUNC.value, funcName)

        if(idNivel == 1):
            dadosReport = dadosReport.replace(REPORT_ENUM.NOME_EMPRE.value, report.getNomeEmpresa())
            dadosReport = dadosReport.replace(REPORT_ENUM.NUMERO_EMPRE.value, report.getNumEmpresa())
            dadosReport = dadosReport.replace(REPORT_ENUM.EDENRECO.value, report.getEndereco())
            dadosReport = dadosReport.replace(REPORT_ENUM.TAG_DONO_EMPRESA, msgSemPermissao)

            dadosReport = dadosReport.replace(REPORT_ENUM.TAG_NOME_AGRO.value, report.getNomeAgro())
            dadosReport = dadosReport.replace(REPORT_ENUM.TAG_TIPO_AGRO.value, msgSemPermissao)
            dadosReport = dadosReport.replace(REPORT_ENUM.TAG_DESC_AGRO.value, msgSemPermissao)
            dadosReport = dadosReport.replace(REPORT_ENUM.TAG_EFEITO_ORAL.value, msgSemPermissao)
            dadosReport = dadosReport.replace(REPORT_ENUM.TAG_EFEITO_DERM.value, msgSemPermissao)
            dadosReport = dadosReport.replace(REPORT_ENUM.TAG_EFEITO_INAL.value, msgSemPermissao)
            dadosReport = dadosReport.replace(REPORT_ENUM.TAG_QT_AGRO.value, msgSemPermissao)

            dadosReport = dadosReport.replace(REPORT_ENUM.TAG_TIPO_DANO.value, msgSemPermissao)
            dadosReport = dadosReport.replace(REPORT_ENUM.TAG_GRAVIDADE, msgSemPermissao)

        elif(idNivel == 2):
            dadosReport = dadosReport.replace(REPORT_ENUM.NOME_EMPRE.value, report.getNomeEmpresa())
            dadosReport = dadosReport.replace(REPORT_ENUM.NUMERO_EMPRE.value, report.getNumEmpresa())
            dadosReport = dadosReport.replace(REPORT_ENUM.EDENRECO.value, report.getEndereco())
            dadosReport = dadosReport.replace(REPORT_ENUM.TAG_DONO_EMPRESA, msgSemPermissao)

            dadosReport = dadosReport.replace(REPORT_ENUM.TAG_NOME_AGRO.value, report.getNomeAgro())
            dadosReport = dadosReport.replace(REPORT_ENUM.TAG_TIPO_AGRO.value, agroTox.getCategoria)
            dadosReport = dadosReport.replace(REPORT_ENUM.TAG_DESC_AGRO.value, agroTox.getDescricao())
            dadosReport = dadosReport.replace(REPORT_ENUM.TAG_EFEITO_ORAL.value, agroTox.getEfeitoOral())
            dadosReport = dadosReport.replace(REPORT_ENUM.TAG_EFEITO_DERM.value, agroTox.getEfeitoDermico())
            dadosReport = dadosReport.replace(REPORT_ENUM.TAG_EFEITO_INAL.value, agroTox.getEfeitoInalar())
            dadosReport = dadosReport.replace(REPORT_ENUM.TAG_QT_AGRO.value, msgSemPermissao)

            dadosReport = dadosReport.replace(REPORT_ENUM.TAG_TIPO_DANO.value, report.getTipoDano())
            dadosReport = dadosReport.replace(REPORT_ENUM.TAG_GRAVIDADE, msgSemPermissao)
    
        elif(idNivel == 3):
            dadosReport = dadosReport.replace(REPORT_ENUM.NOME_EMPRE.value, report.getNomeEmpresa())
            dadosReport = dadosReport.replace(REPORT_ENUM.NUMERO_EMPRE.value, report.getNumEmpresa())
            dadosReport = dadosReport.replace(REPORT_ENUM.EDENRECO.value, report.getEndereco())
            dadosReport = dadosReport.replace(REPORT_ENUM.TAG_DONO_EMPRESA, report.getDonoEmpresa())

            dadosReport = dadosReport.replace(REPORT_ENUM.TAG_NOME_AGRO.value, report.getNomeAgro())
            dadosReport = dadosReport.replace(REPORT_ENUM.TAG_TIPO_AGRO.value, agroTox.getCategoria)
            dadosReport = dadosReport.replace(REPORT_ENUM.TAG_DESC_AGRO.value, agroTox.getDescricao())
            dadosReport = dadosReport.replace(REPORT_ENUM.TAG_EFEITO_ORAL.value, agroTox.getEfeitoOral())
            dadosReport = dadosReport.replace(REPORT_ENUM.TAG_EFEITO_DERM.value, agroTox.getEfeitoDermico())
            dadosReport = dadosReport.replace(REPORT_ENUM.TAG_EFEITO_INAL.value, agroTox.getEfeitoInalar())
            dadosReport = dadosReport.replace(REPORT_ENUM.TAG_QT_AGRO.value, report.getQtdAgro())

            dadosReport = dadosReport.replace(REPORT_ENUM.TAG_TIPO_DANO.value, report.getTipoDano())
            dadosReport = dadosReport.replace(REPORT_ENUM.TAG_GRAVIDADE, report.getGravidade())

    def gerarRelatorioMassivo(self, selectedValue:int):
        
        if(selectedValue == 3):
            # -> Open template massivo
            with open('rsc/templates/REPORT_MASSIVO.txt') as f:
                lines = f.readlines()
                header = ''
                body = ''

            # -> Definição de header e body a partir do template 
            for index in range(0,5):
                header += str(lines[index])

            for index in range(6, len(lines)):
                body += str(lines[index])

            listReports = self._repository.findAll()
            
            # -> Monta template a partir de lista
            dadosReport = self.replaceTagsMassivo(header, body, listReports, filtro = None)

            with open(self._documentPath + '/REPORT-MASSIVO-SEM-FILTRO.txt') as f:
                f.writelines(dadosReport)

        elif(selectedValue == 4):
            
            print('[INFO] --- Selecione [1] para fazer o filtro pelo nome da [Empresa]')
            print('[INFO] --- Selecione [2] para fazer o filtro pelo nome do [AgroToxico]')
            
            selectedValue = input('[INPUT] --- Selecione o filtro: ')
            campo = ''

            if(selectedValue == 1):
                campo = REPORT_ENUM.NOME_EMPRE.value
            elif(selectedValue == 2):
                campo = REPORT_ENUM.NOME_AGRO.value
            else:
                exit

            value = input('[INPUT] --- Insira o valor para o filtro')

             # -> Open template massivo
            with open('rsc/templates/REPORT_MASSIVO.txt') as f:
                lines = f.readlines()
                header = ''
                body = ''

            # -> Definição de header e body a partir do template 
            for index in range(0,5):
                header += str(lines[index])

            for index in range(6, len(lines)):
                body += str(lines[index])

            listReports = self._repository.findByCampo(campo, value)
            
            # -> Monta template a partir de lista
            dadosReport = self.replaceTagsMassivo(header, body, listReports, filtro = campo)

            with open(self._documentPath + '/REPORT-MASSIVO-COM-FILTRO-{}.txt'.format(campo)) as f:
                f.writelines(dadosReport)
        else:
            exit

    def replaceTagsMassivo(self, header:str, body:str, listReport:list, filtro:str):
        funcName:str = self._func.getNome()
        idNivel:int = self._func.getIdNivel()
        msgSemPermissao = '[INFO] - SEM PERMISSÃO'
        isHeaderAdicionado = False;
        retorno = []

        for report in listReport:
            reportTratado = ''
            report:ReportHotModel

            if(isHeaderAdicionado == False):
                headerTratado = ''
                headerTratado = header.replace(REPORT_ENUM.TAG_ID_RELATORIO.value, report.getId())
                headerTratado = header.replace(REPORT_ENUM.TAG_NOME_FUNC.value, funcName)
                
                if(filtro != None):
                    headerTratado = header.replace(REPORT_ENUM.TAG_FILTRO.value, filtro)
                else:
                    headerTratado = header.replace(REPORT_ENUM.TAG_FILTRO.value, 'ALL')

                reportTratado += headerTratado

                isHeaderAdicionado = True
            
            agroTox = self._agroRepository.findByCampo(AGROTOX_ENUM.ID_AGRO.value, report.getTipoAgro())

            if(idNivel == 1):
                bodyTratado = ''
                bodyTratado = body.replace(REPORT_ENUM.NOME_EMPRE.value, report.getNomeEmpresa())
                bodyTratado = bodyTratado.replace(REPORT_ENUM.NUMERO_EMPRE.value, report.getNumEmpresa())
                bodyTratado = bodyTratado.replace(REPORT_ENUM.EDENRECO.value, report.getEndereco())
                bodyTratado = bodyTratado.replace(REPORT_ENUM.TAG_DONO_EMPRESA, msgSemPermissao)

                bodyTratado = bodyTratado.replace(REPORT_ENUM.TAG_NOME_AGRO.value, report.getNomeAgro())
                bodyTratado = bodyTratado.replace(REPORT_ENUM.TAG_TIPO_AGRO.value, msgSemPermissao)
                bodyTratado = bodyTratado.replace(REPORT_ENUM.TAG_DESC_AGRO.value, msgSemPermissao)
                bodyTratado = bodyTratado.replace(REPORT_ENUM.TAG_EFEITO_ORAL.value, msgSemPermissao)
                bodyTratado = bodyTratado.replace(REPORT_ENUM.TAG_EFEITO_DERM.value, msgSemPermissao)
                bodyTratado = bodyTratado.replace(REPORT_ENUM.TAG_EFEITO_INAL.value, msgSemPermissao)
                bodyTratado = bodyTratado.replace(REPORT_ENUM.TAG_QT_AGRO.value, msgSemPermissao)

                bodyTratado = bodyTratado.replace(REPORT_ENUM.TAG_TIPO_DANO.value, msgSemPermissao)
                bodyTratado = bodyTratado.replace(REPORT_ENUM.TAG_GRAVIDADE, msgSemPermissao)

                reportTratado += bodyTratado

            elif(idNivel == 2):
                bodyTratado = ''
                bodyTratado = body.replace(REPORT_ENUM.NOME_EMPRE.value, report.getNomeEmpresa())
                bodyTratado = bodyTratado.replace(REPORT_ENUM.NUMERO_EMPRE.value, report.getNumEmpresa())
                bodyTratado = bodyTratado.replace(REPORT_ENUM.EDENRECO.value, report.getEndereco())
                bodyTratado = bodyTratado.replace(REPORT_ENUM.TAG_DONO_EMPRESA, msgSemPermissao)

                bodyTratado = bodyTratado.replace(REPORT_ENUM.TAG_NOME_AGRO.value, report.getNomeAgro())
                bodyTratado = bodyTratado.replace(REPORT_ENUM.TAG_TIPO_AGRO.value, agroTox.getCategoria)
                bodyTratado = bodyTratado.replace(REPORT_ENUM.TAG_DESC_AGRO.value, agroTox.getDescricao())
                bodyTratado = bodyTratado.replace(REPORT_ENUM.TAG_EFEITO_ORAL.value, agroTox.getEfeitoOral())
                bodyTratado = bodyTratado.replace(REPORT_ENUM.TAG_EFEITO_DERM.value, agroTox.getEfeitoDermico())
                bodyTratado = bodyTratado.replace(REPORT_ENUM.TAG_EFEITO_INAL.value, agroTox.getEfeitoInalar())
                bodyTratado = bodyTratado.replace(REPORT_ENUM.TAG_QT_AGRO.value, msgSemPermissao)

                bodyTratado = bodyTratado.replace(REPORT_ENUM.TAG_TIPO_DANO.value, report.getTipoDano())
                bodyTratado = bodyTratado.replace(REPORT_ENUM.TAG_GRAVIDADE, msgSemPermissao)

                reportTratado += bodyTratado
                
            elif(idNivel == 3):
                bodyTratado = ''
                bodyTratado = body.replace(REPORT_ENUM.NOME_EMPRE.value, report.getNomeEmpresa())
                bodyTratado = bodyTratado.replace(REPORT_ENUM.NUMERO_EMPRE.value, report.getNumEmpresa())
                bodyTratado = bodyTratado.replace(REPORT_ENUM.EDENRECO.value, report.getEndereco())
                bodyTratado = bodyTratado.replace(REPORT_ENUM.TAG_DONO_EMPRESA, report.getDonoEmpresa())

                bodyTratado = bodyTratado.replace(REPORT_ENUM.TAG_NOME_AGRO.value, report.getNomeAgro())
                bodyTratado = bodyTratado.replace(REPORT_ENUM.TAG_TIPO_AGRO.value, agroTox.getCategoria)
                bodyTratado = bodyTratado.replace(REPORT_ENUM.TAG_DESC_AGRO.value, agroTox.getDescricao())
                bodyTratado = bodyTratado.replace(REPORT_ENUM.TAG_EFEITO_ORAL.value, agroTox.getEfeitoOral())
                bodyTratado = bodyTratado.replace(REPORT_ENUM.TAG_EFEITO_DERM.value, agroTox.getEfeitoDermico())
                bodyTratado = bodyTratado.replace(REPORT_ENUM.TAG_EFEITO_INAL.value, agroTox.getEfeitoInalar())
                bodyTratado = bodyTratado.replace(REPORT_ENUM.TAG_QT_AGRO.value, report.getQtdAgro())

                bodyTratado = bodyTratado.replace(REPORT_ENUM.TAG_TIPO_DANO.value, report.getTipoDano())
                bodyTratado = bodyTratado.replace(REPORT_ENUM.TAG_GRAVIDADE, report.getGravidade())

                reportTratado += bodyTratado
            
            retorno.insert(reportTratado)
        
        return retorno