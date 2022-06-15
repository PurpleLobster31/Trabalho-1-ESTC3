#region Bibliotecas
from secrets import choice
import numpy as np
import os 
from Funcionario import Funcionario
from Projeto import Projeto
import pickle
import datetime
from dateutil.relativedelta import relativedelta
#endregion

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

#region Algoritmos de Ordenação
def insertionSortBonificados(lista):
    if len(lista) == 1:
        return lista
    
    for i in range(1, len(lista)):
        a = lista[i]
        j = i - 1
	
    while j>=0 and a.salario > lista[j].salario:
        lista[j+1] = lista[j]
        j-=1

    lista[j+1] = a

    return lista

def insertionSortNomes(lista):
    if len(lista) == 1:
        return lista
    
    for i in range(1, len(lista)):
        a = lista[i]
        j = i - 1
	
    while j>=0 and a < lista[j]:
        lista[j+1] = lista[j]
        j-=1

    lista[j+1] = a

    return lista

def insertionSortAtraso(lista):
    if len(lista) == 1:
        return lista
    
    for i in range(1, len(lista)):
        a = lista[i]
        j = i - 1
	
    while j>=0 and a.atraso > lista[j].atraso:
        lista[j+1] = lista[j]
        j-=1

    lista[j+1] = a

    return lista

def partition(lista, esquerda, direita):
    pivot = lista[direita]
    i = esquerda - 1

    for j in range(esquerda, direita):
        if lista[j].valorEstimado <= pivot.valorEstimado:
            i = i + 1
            (lista[i], lista[j]) = (lista[j], lista[i])

    (lista[i + 1], lista[direita]) = (lista[direita], lista[i + 1])

    return i + 1

def quickSort(lista, esquerda, direita):
    if esquerda < direita:
        pi = partition(lista, esquerda, direita)

        quickSort(lista, esquerda, pi - 1)

        quickSort(lista, pi + 1, direita)
#endregion

def process_project():
    tabelaProjetos = loadProjectPickle()
    os.system('cls || clear')
    print('MENU DE PROJETOS:\n')
    print('[1] BUSCAR')
    print('[2] ADICIONAR')
    print('[3] PROJETOS EM ANDAMENTO')
    print('[4] PROJETOS ATRASADOS (FINALIZADOS E EM ANDAMENTO)')
    print('[5] FUNCIONARIOS BONIFICADOS')
    print('[6] REMOVER')
    print('[7] EDITAR PROJETO')
    print('[8] VOLTAR AO MENU\n')
    option = int(input('Sua escolha: '))

    if option == 1: #buscar
        os.system('cls || clear')
        nomeProjeto = input('Digite o nome do projeto que deseja obter informacoes: ').upper()

        if nomeProjeto in tabelaProjetos:
            os.system('cls || clear')
            projeto = tabelaProjetos[nomeProjeto]
            print('Nome: ' + projeto.nome)
            print('Data de Inicio: {}'.format(projeto.dataInicio))
            if(projeto.finalizado == True):
                print('Data de Termino: {}'.format(projeto.dataTermino))
            else:
                print('Data de Termino: Projeto nao finalizado.')
            print('Tempo estimado: {:d} meses'.format(projeto.tempoEstimado))
            print('Valor estimado: {:.2f} R$'.format(projeto.valorEstimado))
            print('Numero funcional do funcionario responsavel: {:d}'.format(projeto.funcionarioResponsavel))
            print('\nPressione qualquer tecla para continuar.')

        else:
            os.system('cls || clear')
            print('Nao ha projeto com esse.\nAperte qualquer tecla para voltar ao menu.')

        input()

    elif option == 2: #adicionar
        if(len(tabelaProjetos) >= 2000):
            os.system('cls || clear')
            print('Já existem 2000 projetos registrados. Pressione qualquer tecla para continuar.')
            input()
        
        else:
            os.system('cls || clear')
            nomeProjeto = input('Digite o nome do novo projeto: ').upper()
            if nomeProjeto in tabelaProjetos:
                os.system('cls || clear')
                print('Ja existe um projeto com esse nome.\nAperte qualquer tecla para voltar ao menu.')
                input()

            else:
                os.system('cls || clear')
                dataI = input('Digite a data de inicio no formato AAAA-MM-DD: ')
                anoI, mesI, diaI = map(int, dataI.split('-'))
                dataInicio = datetime.date(anoI, mesI, diaI)

                os.system('cls || clear')
                dataT = input('Digite a data de termino no formato AAAA-MM-DD (ou digite 0000-00-00 se o projeto não foi finalizado): ')
                if dataT == '0000-00-00':
                    dataTermino = None
                    finalizado = False
                else:
                    anoT, mesT, diaT = map(int, dataT.split('-'))
                    dataTermino = datetime.date(anoT, mesT, diaT)
                    finalizado = True

                os.system('cls || clear')
                tempoEstimado = int(input('Digite o tempo estimado de finalização em meses: '))

                os.system('cls || clear')
                valorEstimado = float(input('Digite o valor estimado do projeto: '))
                
                escolha = ''
                while escolha != 'q':
                    escolha = ''
                    os.system('cls || clear')
                    funcionarioResponsavel = int(input('Digite o numero funcional do funcionario responsavel pelo projeto: '))
                    tabelaFuncionarios = loadWorkerPickle()
                    if funcionarioResponsavel in tabelaFuncionarios:
                        novoProjeto = Projeto(nomeProjeto, dataInicio, dataTermino, tempoEstimado, valorEstimado, funcionarioResponsavel, finalizado)
                        tabelaProjetos[novoProjeto.nome] = novoProjeto
                        dumpProjectPickle(tabelaProjetos)
                        escolha = 'q'
                    else:
                        os.system('cls || clear')
                        print('Nao existe funcionario com esse numero funcional registrado.\nDigite "q" se deseja voltar ao menu, ou aperte enter para tentar colocar outro numero funcional valido.')                
                        escolha = input()

    elif option == 3: #em andamento
        os.system('cls || clear')
        tabelaProjetos = loadProjectPickle()
        preSortProjetosEmAndamento = []
        
        for nome in tabelaProjetos:
            if tabelaProjetos[nome].valorEstimado > 500000 and tabelaProjetos[nome].finalizado == False:
                preSortProjetosEmAndamento.append(tabelaProjetos[nome])
        
        if len(preSortProjetosEmAndamento) == 0:
            print('Nao ha projetos em aberto com valor estimado maior que 500000.00R$.')
        
        else:
            print('Projetos em andamento com valor estimado maior que 500000.00 R$: ')
            quickSort(preSortProjetosEmAndamento, 0, len(preSortProjetosEmAndamento) - 1)
            for proj in preSortProjetosEmAndamento:
                print('Nome do projeto: {} - Valor estimado: {:.2f} R$'.format(proj.nome, proj.valorEstimado))
        
        print('Aperte qualquer tecla para voltar ao menu.')
        input()
            
    elif option == 4: #atrasados
        os.system('cls || clear')
        dataAtual = datetime.date.today()
        tabelaProjetos = loadProjectPickle()
        preSortProjetosAtrasadosFinalizados = []
        preSortProjetosAtrasadosNaoFinalizados = []
        
        for nome in tabelaProjetos:
            dataEstimada = tabelaProjetos[nome].dataInicio + relativedelta(months=+tabelaProjetos[nome].tempoEstimado)
            if (tabelaProjetos[nome].finalizado == True) and (dataEstimada < tabelaProjetos[nome].dataTermino):
                tabelaProjetos[nome].atraso = (tabelaProjetos[nome].dataTermino - dataEstimada).days
                preSortProjetosAtrasadosFinalizados.append(tabelaProjetos[nome])
            elif (tabelaProjetos[nome].finalizado == False) and (dataEstimada < dataAtual):
                tabelaProjetos[nome].atraso = (dataAtual - dataEstimada).days
                preSortProjetosAtrasadosNaoFinalizados.append(tabelaProjetos[nome])
        
        if(len(preSortProjetosAtrasadosFinalizados) == 0):
            print('Nao ha projetos finalizados atrasados.\n')
        else: 
            sortedProjetosAtrasadosFinalizados = insertionSortAtraso(preSortProjetosAtrasadosFinalizados)
            print('Projetos finalizados atrasados: ')
            for proj in sortedProjetosAtrasadosFinalizados:
                print('Nome do projeto: {} - Tempo de atraso: {:d} dias.'.format(proj.nome, proj.atraso))
        
        if(len(preSortProjetosAtrasadosNaoFinalizados) == 0):
            print('Nao ha projetos nao finalizados atrasados.\n')
        else: 
            sortedProjetosAtrasadosNaoFinalizados = insertionSortAtraso(preSortProjetosAtrasadosNaoFinalizados)
            print('Projetos nao finalizados atrasados: ')
            for proj in sortedProjetosAtrasadosNaoFinalizados:
                print('Nome do projeto: {} - Tempo de atraso: {:d} dias.'.format(proj.nome, proj.atraso))
            
        print('Aperte qualquer tecla para continuar.')
        input()

    elif option == 5: #bonificados
        preSetFuncionariosResponsaveis = []
        nomeFuncionariosResponsaveis = []
        tabelaProjetos = loadProjectPickle()
        tabelaFuncionarios = loadWorkerPickle()
        
        for key in tabelaProjetos:
            if tabelaProjetos[key].finalizado == False:
                preSetFuncionariosResponsaveis.append(tabelaProjetos[key].funcionarioResponsavel)
        
        os.system('cls || clear')

        if(len(preSetFuncionariosResponsaveis) == 0):
            print('Nao ha funcionarios trabalhando em projetos nao finalizados.') 
        else:
            setFuncionariosResponsaveis = set(preSetFuncionariosResponsaveis)
        
            for numFuncionalResponsaveis in setFuncionariosResponsaveis:
                nomeFuncionariosResponsaveis.append(tabelaFuncionarios[numFuncionalResponsaveis].nome)
            
            nomeFuncionariosResponsaveis = insertionSortNomes(nomeFuncionariosResponsaveis)

            print("Funcionarios responsaveis por projetos nao finalizados: ")
            for nome in nomeFuncionariosResponsaveis:
                print(nome)
        
        print('Aperte qualquer tecla para voltar ao menu.')
        input()

    elif option == 6: #remover
        os.system('cls || clear')
        nomeProjeto = input('Digite o nome do projeto que deseja apagar: ').upper()
        if nomeProjeto in tabelaProjetos:
            os.system('cls || clear')
            tabelaProjetos.pop(nomeProjeto)
            print('O projeto entitulado {} foi deletado.\nAperte qualquer tecla para voltar ao menu.'.format(nomeProjeto))
            dumpProjectPickle(tabelaProjetos)
            input()
        else:
            os.system('cls || clear')
            print('Nao ha projeto com esse nome.\nAperte qualquer tecla para voltar ao menu.')
            input()
    
    elif option == 7: #editar
        os.system('cls || clear')
        nomeProjeto = input('Digite o nome do projeto que deseja editar os dados: ').upper()
        if nomeProjeto in tabelaProjetos:
            os.system('cls || clear')
            projeto = tabelaProjetos[nomeProjeto]
            
            print('A data de inicio atual e: {}. Deseja alterar?'.format(projeto.dataInicio))
            escolha = input('Digite S ou N: ').upper()
            if escolha == 'S':
                os.system('cls || clear')
                dataI = input('Digite a nova data de inicio no formato AAAA-MM-DD: ')
                anoI, mesI, diaI = map(int, dataI.split('-'))
                projeto.dataInicio = datetime.date(anoI, mesI, diaI)
                os.system('cls || clear')
            else:
                os.system('cls || clear')
            
            if projeto.dataTermino == None:
                print('O projeto nao foi finalizado, entao nao possui data de termino. Deseja alterar?')
            else:
                print('A data de termino atual e: {}. Deseja alterar?'.format(projeto.dataTermino))
            escolha = input('Digite S ou N: ').upper()
            if escolha == 'S':
                os.system('cls || clear')
                
                dataT = input('Digite a nova data de termino no formato AAAA-MM-DD (ou digite 0000-00-00 se o projeto não foi finalizado): ')
                if dataT == '0000-00-00':
                    projeto.dataTermino = None
                    projeto.finalizado = False
                else:
                    anoT, mesT, diaT = map(int, dataT.split('-'))
                    projeto.dataTermino = datetime.date(anoT, mesT, diaT)
                    projeto.finalizado = True
                os.system('cls || clear')
            else:
                os.system('cls || clear')
            
            print('O tempo estimado de finalizacao atual e: {} meses. Deseja alterar?'.format(projeto.tempoEstimado))
            escolha = input('Digite S ou N: ').upper()
            if escolha == 'S':
                os.system('cls || clear')
                projeto.tempoEstimado = int(input('Digite o novo tempo estimado de finalização em meses: '))
                os.system('cls || clear')
            else:
                os.system('cls || clear')
            
            print('O atual numero funcional do fucionario responsavel e: {}. Deseja alterar?'.format(projeto.funcionarioResponsavel))
            escolha = input('Digite S ou N: ').upper()
            if escolha == 'S':
                os.system('cls || clear')
                while escolha != 'q':
                    escolha = ''
                    os.system('cls || clear')
                    numFuncionarioResponsavel = int(input('Digite o numero funcional do novo funcionario responsavel pelo projeto: '))
                    tabelaFuncionarios = loadWorkerPickle()
                    if numFuncionarioResponsavel in tabelaFuncionarios:
                        projeto.funcionarioResponsavel = numFuncionarioResponsavel
                        escolha = 'q'
                    else:
                        os.system('cls || clear')
                        print('Nao existe funcionario com esse numero funcional registrado.\nDigite "q" se deseja continuar sem fazer alteracoes, ou aperte enter para tentar colocar outro numero funcional valido.')                
                        escolha = input()
                os.system('cls || clear')
            else:
                os.system('cls || clear')
            
            print('Os dados foram alterados.\nAperte qualquer tecla para voltar ao menu.')
            dumpProjectPickle(tabelaProjetos)
            input()
        
        else:
            os.system('cls || clear')
            print('Nao ha projeto com esse numero funcional.\nAperte qualquer tecla para voltar ao menu.')
            input()

    else: #voltar
        pass    

def process_worker():
    tabelaFuncionarios = loadWorkerPickle()
    os.system('cls || clear')
    print('MENU DE FUNCIONÁRIOS:\n')
    print('[1] BUSCAR')
    print('[2] ADICIONAR')
    print('[3] VER BONIFICADOS')
    print('[4] REMOVER')
    print('[5] EDITAR FUNCIONARIO')
    print('[6] VOLTAR AO MENU\n')
    choice = int(input('Sua escolha: '))
    
    if choice == 1: #buscar
        os.system('cls || clear')
        num = int(input('Digite o numero funcional do funcionario que deseja obter informacoes: '))

        if num in tabelaFuncionarios:
            os.system('cls || clear')
            funcionario = tabelaFuncionarios[num]
            print('Nome: ' + funcionario.nome)
            print('Numero Funcional: {:d}'.format(funcionario.numFuncional))
            print('Salario: {:.2f} R$'.format(funcionario.salario))
            print('E-mail: ' + funcionario.email)
            print('\nPressione qualquer tecla para continuar.')

        else:
            os.system('cls || clear')
            print('Nao ha funcionario com esse numero funcional.\nAperte qualquer tecla para voltar ao menu.')

        input()

    elif choice == 2: #adicionar
        if(len(tabelaFuncionarios) >= 500):
            os.system('cls || clear')
            print('Já existem 500 funcionarios registrados. Pressione qualquer tecla para continuar.')
            input()

        else:
            os.system('cls || clear')
            numFuncional = int(input('Digite o numero funcional do novo funcionario: '))
            if numFuncional in tabelaFuncionarios:
                os.system('cls || clear')
                print('Ja existe um funcionario com esse numero funcional.\n Aperte qualquer tecla para voltar ao menu.')
                input()

            else:
                os.system('cls || clear')
                nome = input('Digite o nome do novo funcionario: ').upper()
                os.system('cls || clear')
                salario = float(input('Declare o valor do salario do novo funcionario: '))
                os.system('cls || clear')
                email = input('Digite o e-mail do novo funcionario: ')
                novoFuncionario = Funcionario(numFuncional, nome, salario, email)
                tabelaFuncionarios[novoFuncionario.numFuncional] = novoFuncionario
        
        dumpWorkerPickle(tabelaFuncionarios)

    elif choice == 3: #ver bonificados
        os.system('cls || clear')
        tabelaFuncionarios = loadWorkerPickle()
        preSortFuncionariosBonificados = []
        sortedFuncionariosBonificados = []
        for numFunc in tabelaFuncionarios:
            if tabelaFuncionarios[numFunc].salario < 10000.00:
                preSortFuncionariosBonificados.append(tabelaFuncionarios[numFunc])
        if len(preSortFuncionariosBonificados) == 0 :
            print('Nao ha funcionarios com salario menor que 10000.00R$.')
        else:
            print('Funcionarios bonificados: ')
            sortedFuncionariosBonificados = insertionSortBonificados(preSortFuncionariosBonificados)
        
            for func in sortedFuncionariosBonificados:
                print('Nome: {} - Salario: {:.2f}R$'.format(func.nome, func.salario))
        
        print('Aperte qualquer tecla para voltar ao menu.')
        input()

    elif choice == 4: #remover
        os.system('cls || clear')
        num = int(input('Digite o numero funcional do funcionario que deseja apagar: '))
        if num in tabelaFuncionarios:
            os.system('cls || clear')
            tabelaFuncionarios.pop(num)
            print('O funcionario de numero funcional {:d} foi deletado.\nAperte qualquer tecla para voltar ao menu.'.format(num))
            dumpWorkerPickle(tabelaFuncionarios)
            input()
        else:
            os.system('cls || clear')
            print('Nao ha funcionario com esse numero funcional.\nAperte qualquer tecla para voltar ao menu.')
            input()

    elif choice == 5: #editar
        os.system('cls || clear')
        num = int(input('Digite o numero funcional do funcionario que deseja editar os dados: '))
        if num in tabelaFuncionarios:
            os.system('cls || clear')
            funcionario = tabelaFuncionarios[num]
            print('O nome atual e: {}. Deseja alterar?'.format(funcionario.nome))
            escolha = input('Digite S ou N: ').upper()
            if escolha == 'S':
                os.system('cls || clear')
                funcionario.nome = input('Digite o novo nome: ').upper()
                os.system('cls || clear')
            else:
                os.system('cls || clear')
            print('O salario atual e: {:.2f} R$. Deseja alterar?'.format(funcionario.salario))
            escolha = input('Digite S ou N: ').upper()
            if escolha == 'S':
                os.system('cls || clear')
                funcionario.salario = float(input('Digite o novo salario: '))
                os.system('cls || clear')
            else:
                os.system('cls || clear')
            print('O e-mail atual e: {}. Deseja alterar?'.format(funcionario.email))
            escolha = input('Digite S ou N: ').upper()
            if escolha == 'S':
                os.system('cls || clear')
                funcionario.email = input('Digite o novo e-mail: ')
                os.system('cls || clear')
            else:
                os.system('cls || clear')
            print('Os dados foram alterados.\nAperte qualquer tecla para voltar ao menu.')
            dumpWorkerPickle(tabelaFuncionarios)
            input()
        else:
            os.system('cls || clear')
            print('Nao ha funcionario com esse numero funcional.\nAperte qualquer tecla para voltar ao menu.')
            input()

    else:   #voltar
        pass

def menu():
    option = 0

    while(option != 3):
        os.system('cls || clear')
        print('='*30)
        print('SISTEMA DE CONTROLE EMPRESARIAL')
        print('='*30)

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
            os.system('cls || clear')
            print('ERRO: OPÇÃO INVÁLIDA!')
            print('Pressione qualquer tecla para voltar ao menu...')
            option = 0
            input()
