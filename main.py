from src.controllers.cadastro import Cadastro
from src.controllers.login import Login 

def teste():
    cadastro = Cadastro()

    cadastro.testeAction()

def main():   
    cadastro = Cadastro()
    login = Login
    
    def spaces(count, char):
        for x in range(0, int(count)):
            print(char)

    print('============================================')
    print('=========         AgroSafe         =========')
    print('============================================')
    
    spaces(3, '...')

    print('[INFO] --- [1] = Login')
    print('[INFO] --- [2] = Cadastro')
    
    spaces(1, '...')
    
    valueSelected = int(input('[INPUT] --- Selecionar acao: '))
    
    if(valueSelected == 1):
        print('[SISTEMA] --- Iniciando Login')
        #Action Login
        login.loginAction()
        
    elif(valueSelected == 2):
        print('[SISTEMA] --- Iniciando Cadastro')
        #Action Cadastro
        cadastro.cadastroAction()

    else:
        print('[ERRO] --- Valor inválido: ' + str(valueSelected))
        exit
    
main()



    

