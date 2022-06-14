from secrets import choice
import numpy as np
import os 
from Funcionario import Funcionario
from Projeto import Projeto
import pickle
import datetime

#region PickleList
def dumpWorkerPickle(tabelaFuncionarios):
    with open('tabelaFuncionarios.pickle', 'wb') as handle:
        pickle.dump(tabelaFuncionarios, handle, protocol=pickle.HIGHEST_PROTOCOL)

def loadWorkerPickle():
    with open('tabelaFuncionarios.pickle', 'rb') as handle:
            return pickle.load(handle)

def dumpProjectPickle(tabelaProjetos):
    with open('tabelaProjetos.pickle', 'wb') as handle:
            pickle.dump(tabelaProjetos, handle, protocol=pickle.HIGHEST_PROTOCOL)

def loadProjectPickle():
    with open('tabelaProjetos.pickle', 'rb') as handle:
            return pickle.load(handle)
#endregion

def process_project():
    tabelaProjetos = loadProjectPickle()
    os.system('cls')
    print('MENU DE PROJETOS:\n')
    print('[1] BUSCAR')
    print('[2] ADICIONAR')
    print('[3] PROJETOS EM ANDAMENTO')
    print('[4] PROJETOS ATRASADOS')
    print('[5] FUNCIONARIOS BONIFICADOS')
    print('[6] REMOVER')
    print('[7] VOLTAR AO MENU\n')
    option = int(input('Sua escolha: '))

    if option == 1: #buscar
        pass
    elif option == 2: #adicionar
        if(len(tabelaProjetos) >= 2000):
            os.system('cls')
            print('Já existem 2000 projetos registrados. Pressione qualquer tecla para continuar.')
            input()
        
        else:
            os.system('cls')
            nomeProjeto = input('Digite o nome do novo projeto: ')
            if nomeProjeto in tabelaProjetos:
                os.system('cls')
                print('Ja existe um projeto com esse nome.\nAperte qualquer tecla para voltar ao menu')
                input()

            else:
                os.system('cls')
                dataI = input('Digite a data de inicio no formato AAAA-MM-DD: ')
                anoI, mesI, diaI = map(int, dataI.split('-'))
                dataInicio = datetime.date(anoI, mesI, diaI)

                os.system('cls')
                dataT = input('Digite a data de termino no formato AAAA-MM-DD (ou digite 0000-00-00 se o projeto não foi finalizado): ')
                if dataT == '0000-00-00':
                    dataTermino = None
                else:
                    anoT, mesT, diaT = map(int, dataT.split('-'))
                    dataTermino = datetime.date(anoT, mesT, diaT)

                os.system('cls')
                tempoEstimado = int(input('Digite o tempo estimadod e finalização em meses '))

                os.system('cls')
                valorEstimado = float(input('Digite o valor estimado do projeto: '))

                os.system('cls')
                funcionarioResponsavel = int(input('Digite o numero funcional do funcionario responsavel pelo projeto: '))
                
                novoProjeto = Projeto(nomeProjeto, dataInicio, dataTermino, tempoEstimado, valorEstimado, funcionarioResponsavel)
                tabelaProjetos[novoProjeto.nome] = novoProjeto

    elif option == 3: #em andamento
        pass
    elif option == 4: #atrasados
        pass
    elif option == 5: #bonificados
        pass
    elif option == 6: #remover
        pass
    else: #voltar
        pass    

def process_worker():
    tabelaFuncionarios = loadWorkerPickle()
    os.system('cls')
    print('MENU DE FUNCIONÁRIOS:\n')
    print('[1] BUSCAR')
    print('[2] ADICIONAR')
    print('[3] VER BONIFICADOS')
    print('[4] REMOVER')
    print('[5] VOLTAR AO MENU\n')
    choice = int(input('Sua escolha: '))
    
    if choice == 1: #buscar
        os.system('cls')
        num = int(input('Digite o numero funcional do funcionario que deseja obter informacoes: '))

        if num in tabelaFuncionarios:
            os.system('cls')
            print('Nome: ' + tabelaFuncionarios[num].nome)
            print('Numero Funcional: {:d}'.format(num))
            print('Salario: {:.2f}'.format(tabelaFuncionarios[num].salario))
            print('E-mail: ' + tabelaFuncionarios[num].email)
            print('\nPressione qualquer tecla para continuar.')

        else:
            os.system('cls')
            print('Nao ha funcionario com esse numero funcional.\nAperte qualquer tecla para voltar ao menu.')

        input()

    elif choice == 2: #adicionar
        if(len(tabelaFuncionarios) >= 500):
            os.system('cls')
            print('Já existem 500 funcionarios registrados. Pressione qualquer tecla para continuar.')
            input()

        else:
            os.system('cls')
            numFuncional = int(input('Digite o numero funcional do novo funcionario: '))
            if numFuncional in tabelaFuncionarios:
                os.system('cls')
                print('Ja existe um funcionario com esse numero funcional.\n Aperte qualquer tecla para voltar ao menu.')
                input()

            else:
                os.system('cls')
                nome = input('Digite o nome do novo funcionario: ')
                os.system('cls')
                salario = float(input('Declare o valor do salario do novo funcionario: '))
                os.system('cls')
                email = input('Digite o e-mail do novo funcionario: ')
                novoFuncionario = Funcionario(numFuncional, nome, salario, email)
                tabelaFuncionarios[novoFuncionario.numFuncional] = novoFuncionario
        
        dumpWorkerPickle(tabelaFuncionarios)

    elif choice == 3: #ver bonificados
        pass

    elif choice == 4: #remover
        os.system('cls')
        num = int(input('Digite o numero funcional do funcionario que deseja apagar: '))
        if num in tabelaFuncionarios:
            os.system('cls')
            tabelaFuncionarios.pop(num)
            print('O funcionario de numero funcional {:d} foi deletado.\nAperte qualquer tecla para voltar ao menu.'.format(num))
            dumpWorkerPickle(tabelaFuncionarios)
            input()
        else:
            os.system('cls')
            print('Nao ha funcionario com esse numero funcional.\nAperte qualquer tecla para voltar ao menu.')
            input()

    else:   #voltar
        pass

def menu():
    option = 0

    while(option != 3):
        os.system('cls')
        print('='*20)
        print('CONTROLE DE DADOS V1')
        print('='*20)

        print('[1] MENU DE FUNCIONÁRIOS')
        print('[2] MENU DE PROJETOS')
        print('[3] SAIR')

        option = int(input('Sua escolha: '))

        if(option == 1):
            process_worker()
            

        elif(option == 2):
            process_project()

        elif(option == 3):
            exit()

        else:
            os.system('cls')
            print('ERRO: OPÇÃO INVÁLIDA!')
            print('Pressione qualquer tecla para voltar ao menu...')
            option = 0
            input()
