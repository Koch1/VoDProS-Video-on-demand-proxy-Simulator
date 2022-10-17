
import sys
sys.maxsize
sys.setrecursionlimit(10**6)


from clas.cliente import Cliente
from clas.filme import Filme
from clas.printDados import PrintDados
from clas.pacote import Pacote
from clas.resultado import Resultado
from clas.manipulacaoArquivo import ManipulacaoArquivo
from clas.arvore import Arvore
from clas.no import No
from clas.arvoreEspera import ArvoreEspera
from clas.noEspera import NoEspera
from clas.log import Log
import time
import threading
import csv 
import os
import math
import multiprocessing 
import os
from random import randrange

def execucao(interfase,lock,res,arquivoLeitura,arquivoAgoritmo,classAlgoritmo,argumento,memoriaTotal,larguraBanda,tamanhoVideo,*debug):
    #Tempo de execução
    tempoInicialFuncao = time.time()
    
    #Impormt do algoritmo
    impor=str("from algoritmo."+arquivoAgoritmo+" import "+classAlgoritmo)
    exec(impor,globals()) 
    #Iniciando class do algortimo
    comand=str("algoritmo="+classAlgoritmo+"("+argumento+")")
    exec(comand,globals())
    
    #Lista q tem infomaçoes da memoria proxy de video
    memoria=[]
    
    #Argumento,seria janela do tempo
    argumento=int(argumento)
    
    #Classe resposavel salvar os resultados finais em txt, manter historico da valores a cada segundo
    resultado=Resultado(arquivo,algoritmo.nomeAlgoritmo,memoriaTotal,larguraBanda,tamanhoVideo)

    #tempo medido tempo proxy,não funciona na escala tempo real
    instanteTempo=0
    
    #Para salvar só nome do Arquivo Sera Lido
    arquivo=(arquivoLeitura.split('/'))[-1];    
    
    #Iniciar a classe leitura do arquivo
    leitura=ManipulacaoArquivo(arquivoLeitura,resultado,classAlgoritmo)
    
    #Ler primera linha do arquivo, para inciar a execução do simulador,
    #O arquivos gerados tem a coluna tempo ordenada, assim primeiro caregado, permite saver horario de entrada dele.  Depois durante a execução tambem deixara um cliente crregado.  
    novoCliente=leitura.novoClienteLido(tamanhoVideo)
    
    #Medidore de tempo
    primeiroT=[0,0,0]
    primeiroT2=[0,0,0]
    primeiroT3=[0,0,0]
    primeiroT4=[0,0,0]
    primeiroT5=[0,0,0]
    primeiroT6=[0,0,0]
    segundoT=[0,0,0]
    segundoT2=[0,0,0]
    segundoT3=[0,0,0]
    terceiroT=[0,0,0]
    quartoT=[0,0,0]
    quartoT1=[0,0,0]
    quartoT2=[0,0,0]
    quartoT3=[0,0,0]
    quartoT4=[0,0,0]
    quartoT5=[0,0,0]
    cincoT=[0,0,0]
    
    #inicializar os salvamentodos log, para porserioriamento verificar
    log=Log(classAlgoritmo+str(inputEntrada),inputEntrada,debug)
    log.escreverTodos([arquivo,algoritmo.nomeAlgoritmo,memoriaTotal,larguraBanda,tamanhoVideo,inputEntrada])


    #Contem todos cliente ativos ou em espera. Ele estao em ordem q quem chega primeiro , primeiro receber.
    listaClientes=[]
    #Matriz que  tem infomaçoes do filme e possição da memoria se encontra bloco.  Funciona como Organição de memoria Indexada
    listaFilmes={}
    #Tem os contadores  dentro, é chamada para adicionar erro ou  acertos. Cada repetição e sempre salvo salvamentoResultados e depois zerado os valores
    result=Resultado(arquivo,algoritmo.nomeAlgoritmo)
    #Inicia class que exibe informações na tela.  Desde que esteja ativo o modo de ezibição
    printDados=PrintDados()
    
    #contado de tempo do ciclo
    inicio = time.time()
    #Inicializar Arvores
    arvore=Arvore(log)

    #Inicio do ciclo. Repedição vai para de acordo com ultimo
    while True:
        #Salvar tempo do ciclo
        inicioTempo = time.time()
        #Salvar Tempo da leitura no ciclo
        inicio2 = time.time()
        # Primeiro condição exite um cliente lido, qur dizer que acabou  a lista leitura
        #Verifica ultimo cliente lido esta na hora de entrar na lista clientes
        while (novoCliente!=0 and novoCliente.tempoInicio==instanteTempo):
            primeiroT[2]+=1
            #contado de clientes ativos
            resultado.novoCliente()
            #Adiciona clliente na lista cliente acabou iniciar filme
            listaClientes.append(novoCliente)
            #Verifica exite outro cliente ja inicio o estrutura do filme que sera lido pelo cliente
            if(listaFilmes.get(novoCliente.idFilme)):
                listaFilmes[novoCliente.idFilme].clientes[novoCliente.idCliente]=novoCliente
            else:
                listaFilmes[novoCliente.idFilme]=Filme(novoCliente.idFilme,tamanhoVideo)
                listaFilmes[novoCliente.idFilme].clientes[novoCliente.idCliente]=novoCliente
            #leutura do proximo cliente do arquivo
            novoCliente=leitura.novoClienteLido(tamanhoVideo)
        #Calculo tempo e quantidade execução       
        fim2 = time.time()
        calculo=fim2 - inicio2
        primeiroT[0]+=calculo
        primeiroT[1]+=1
        #Log escrita na tela. 
        log.escrever("While %i entrada Clientes:%.5f "%(contadoresloop,(primeiroT[0]/primeiroT[1])))
        #Salvar dados calculo tempo
        resultado.tempoEntradaClienteDef(calculo)
        
        #Verificar tem printa a interfase de terminal. Quando ativo pode fazer a simulação demara mais tempo na execução
        if(interfase):
            classificacao=[]
            arvore.mostrarClassificacao(None,False,arvore.root,classificacao)
            printDados.intefase3(instanteTempo,result,memoria,memoriaTotal,listaClientes,listaFilmes,classificacao)
        #Substituição da parte dos cliente atendendo
        contadorLarguraBanda=0;
        listaEsperaCachebloco={}
        listaEsperaCacheFilme={}
        listaEsperaCacheOrdemChegada=[]
        inicio2 = time.time()
        
        # log , para gera log dos da execução para validação
        if(log.verificar[0]):
            quant=0
            log.escreverVerificar("Verificação 01")
            quantidadeNaoEncontrado=0
            for idFilme in listaFilmes:
                quantidadeNaoEncontrado=listaFilmes[idFilme].verificar(quantidadeNaoEncontrado,log)
                quant+=len(listaFilmes[idFilme].blocos)
            quantidade={}
            quantidade['quantidade']=0
            arvore.quatidadeItems(arvore.root,quantidade)
            #log.escreverVerificar(["Diferentes 1",quantidade['quantidade'],len(memoria),quantidadeNaoEncontrado])
            if((quantidade['quantidade'])!=len(memoria) or quant!=len(memoria) ):
                print(["Diferentes 1",quantidade['quantidade'],len(memoria),quantidadeNaoEncontrado])
                breakpoint()
        
        #Leitura da lista cliente, calcular o ciclo. o : e para clona lista usada nessa execução, não tem haver alteração key da lista 
        for cliente in (listaClientes[:]):
            primeiroT2[2]+=1
            #Remover o cliente q terminou de assistir video da lista
            if((cliente.idBloco+1)==cliente.tamanhoBloco):
                #Função debugar faz a verificação dos dados, imprime quando encontra  problema
                log.debugPersoanalizado(listaFilmes,arvore,memoria,3,"Antes Saida de Clientes")
                #contado de tempo da saida cliente
                inicio3 = time.time()
                #Remove cliente do contador,
                resultado.terminouCliente()
                #excluio da lista do mapeamento do filme
                del listaFilmes[cliente.idFilme].clientes[cliente.idCliente]
                #Remove cliente da lista
                listaClientes.remove(cliente)
                #Para poder ter mais opção no algortimos quando ocorrer a saida do cliente,a uma condição interna da funcao
                algoritmo.saidaCliente(argumento,listaFilmes[cliente.idFilme],cliente,arvore,log,memoria)
                #Função debugar faz a verificação dos dados, imprime quando encontra  problema
                log.debugPersoanalizado(listaFilmes,arvore,memoria,3,"Depois Saida de Clientes")
                #Fim do contado de tempo da saida cliente
                fim2 = time.time()
                calculo2=fim2 - inicio3
                primeiroT3[0]+=calculo2
                primeiroT3[1]+=1
            else:
                #contado de tempo da novo ciclo para um cliente
                inicio3 = time.time() 

                #Verifica se o bloco esta armazenada no proxy  
                if(listaFilmes[cliente.idFilme].blocos.get((cliente.idBloco+1))!=None):
                    #Função debugar faz a verificação dos dados, imprime quando encontra  problema
                    log.debugPersoanalizado(listaFilmes,arvore,memoria,3,"Inicio do primeir loop, bloco encontrado")
                    #muda o mapeamento do cliente  dentro da lista do filme.  
                    if(cliente.idBloco==-1):
                        listaFilmes[cliente.idFilme].numeroClientes+=1
                    else:
                        if((listaFilmes[cliente.idFilme].blocos).get(cliente.idBloco)!=None):
                            listaFilmes[cliente.idFilme].blocos[cliente.idBloco]-=1
                    #Adiciona o proximo bloco
                    cliente.idBloco+=1        
                    if((listaFilmes[cliente.idFilme].blocos).get(cliente.idBloco)!=None):
                        listaFilmes[cliente.idFilme].blocos[cliente.idBloco]+=1
                    else:
                        listaFilmes[cliente.idFilme].blocos[cliente.idBloco]=1
                    #Altera a classificação do bloco do vidio na matriz calculo da pontuação, de acordo com a regra na classe do algoritmo 
                    algoritmo.alterarClassificar(argumento,listaFilmes,cliente,instanteTempo) 
                    
                    #Coloca cliente coloca cliente no bloco do memoria corretamente
                    memoria[listaFilmes[cliente.idFilme].blocoMemoria[cliente.idBloco]]=([cliente.idFilme,cliente.idBloco,listaFilmes[cliente.idFilme].blocos[cliente.idBloco],algoritmo.variavelGenericaMemoriaAcerto(memoria[listaFilmes[cliente.idFilme].blocoMemoria[cliente.idBloco]][3])])

                    #Verifica teve alteração na classificação para altera possição do cliente na memoria
                    algoritmo.calcularClasificacao(cliente.idBloco,listaFilmes[cliente.idFilme], arvore)
                    #Função debugar faz a verificação dos dados, imprime quando encontra  problema
                    if(log.verificar[2]):
                        log.debugPersoanalizado(listaFilmes,arvore,memoria,1,"depois bloco encontrado no Primeiro Loop")
                        quant=0
                        log.escreverVerificar("Verificação 2-2")
                        quantidadeNaoEncontrado
                        for idFilme in listaFilmes:
                            quantidadeNaoEncontrado=listaFilmes[idFilme].verificar(quantidadeNaoEncontrado,log)
                            quant+=len(listaFilmes[idFilme].blocos)
                            quantidade={}
                            quantidade['quantidade']=0
                            arvore.quatidadeItems(arvore.root,quantidade)
                            log.escreverVerificar(["Diferentes 2-2",quantidade['quantidade'],len(memoria),quantidadeNaoEncontrado])
                            arvore.inOrderLog(arvore.root,log)
                            log.escreverVerificar(arvore.root)
                        if((quantidade['quantidade'])!=len(memoria) or quant!=len(memoria)):        
                            print(["Diferentes 2-2",quantidade['quantidade'],len(memoria),quantidadeNaoEncontrado])
                            breakpoint()
                    #Adiciona na taxa de acerto +1
                    result.acerto()
                    resultado.acerto()
                    resultado.cachePacote()
                    #Fim do contado de tempo da cliente encontram pacote na cache
                    fim2 = time.time()
                    calculo2=fim2 - inicio3
                    primeiroT5[0]+=calculo2
                    primeiroT5[1]+=1
                    
                else:
                    #Adiciona +1 na quantidade solictações precição usar banda 
                    resultado.solicBanda()
                    #Função debugar faz a verificação dos dados, imprime quando encontra  problema
                    log.debugPersoanalizado(listaFilmes,arvore,memoria,3,"incio lista de espera")
                    #Adiciona pacote na lista espera,ele criar lista com contadores filme e blocos para dar prioridade para os pacotes que tem mais cliente solicitando  
                    if(listaEsperaCacheFilme.get(cliente.idFilme)):
                        if(listaEsperaCachebloco.get(str(cliente.idBloco)+'-'+str(cliente.idFilme))):
                            listaEsperaCachebloco[str(cliente.idBloco+1)+'-'+str(cliente.idFilme)].addContador()
                            listaEsperaCacheOrdemChegada.append(cliente)
                            listaEsperaCacheFilme[cliente.idFilme]=int(listaEsperaCacheFilme[cliente.idFilme])+1
                        else:
                            listaEsperaCacheFilme[cliente.idFilme]=int(listaEsperaCacheFilme[cliente.idFilme])+1
                            listaEsperaCachebloco[str(cliente.idBloco+1)+'-'+str(cliente.idFilme)]=Pacote(cliente.idFilme,(cliente.idBloco+1),(len(listaEsperaCachebloco)+1))
                            listaEsperaCacheOrdemChegada.append(cliente)
                    else:
                        listaEsperaCacheFilme[cliente.idFilme]=1
                        listaEsperaCachebloco[str(cliente.idBloco+1)+'-'+str(cliente.idFilme)]=Pacote(cliente.idFilme,(cliente.idBloco+1),(len(listaEsperaCachebloco)+1))
                        listaEsperaCacheOrdemChegada.append(cliente)
                        
                    #Fim do contado de tempo da cliente entraram na fila de espera    
                    fim2 = time.time()
                    calculo2=fim2 - inicio3
                    primeiroT6[0]+=calculo2
                    primeiroT6[1]+=1
                    log.debugPersoanalizado(listaFilmes,arvore,memoria,3,"Fim lista de espera")
                #Fim do contado de tempo da cliente cliente receberam bloco ou entram no fila de espera
                fim2 = time.time()
                calculo2=fim2 - inicio3
                primeiroT4[0]+=calculo2
                primeiroT4[1]+=1
                
        #Fim do contado de tempo da cliente estavam lista cliente
        fim2 = time.time()
        calculo=fim2 - inicio2
        primeiroT2[0]+=calculo
        primeiroT2[1]+=1
        resultado.tempoDistribucaoNaCacheDef(calculo)
        #contado de tempo ordezar lista de espera
        inicio2 = time.time()
        tamLista=len(listaEsperaCachebloco)
        #Ordena lista espera, priorizando os pedidos com maior numero solicitações filmes e blocos
        listaEsperaCacheblocoOrdenado=(sorted(listaEsperaCachebloco, key=lambda pac: ((((listaEsperaCachebloco[pac].contador*tamLista)+listaEsperaCacheFilme[listaEsperaCachebloco[pac].idFilme])*tamLista)+(tamLista-listaEsperaCachebloco[pac].posicao)),reverse=True))        
        
        #Fim do contado de tempo ordezar lista de espera
        fim2 = time.time()
        calculo=fim2 - inicio
        segundoT[0]+=calculo
        segundoT[1]+=1
        segundoT[2]+=1
        resultado.tempoOrdenacaoPedidosRequisicaoDef(calculo)

        #Inicio contado de tempo gerar a lista de substituição atraves da arvore
        inicio2 = time.time()
        listaSub={}
        #debug
        if(log.verificar[3]):
            quant=0
            log.escreverVerificar("Verificação 03")
            quantidadeNaoEncontrado=0
            for idFilme in listaFilmes:
                quantidadeNaoEncontrado=listaFilmes[idFilme].verificar(quantidadeNaoEncontrado,log)
                quant+=len(listaFilmes[idFilme].blocos)
            quantidade={}
            quantidade['quantidade']=0
            arvore.quatidadeItems(arvore.root,quantidade)
            log.escreverVerificar(["Diferentes 3",quantidade['quantidade'],len(memoria),len(listaSub),quantidadeNaoEncontrado])
            if((quantidade['quantidade']+len(listaSub))!=len(memoria) or quant!=len(memoria) or quantidadeNaoEncontrado!=len(listaSub)):
                print(["Diferentes 3",quantidade['quantidade'],len(memoria),len(listaSub),quantidadeNaoEncontrado])
                breakpoint()
        
        #Emcontrar a quatidade de pacotes em espera que estegam dentro limite da quantidade banda disponivel
        quantidadePacoteEspera=len(listaEsperaCacheblocoOrdenado[:larguraBanda])
        #Traz a quantidade de item tera substuidos 
        quantidaNosTirar=quantidadePacoteEspera-((memoriaTotal-len(memoria)))
        #essa condição verifica  quantidade iremos tirar maior que 0 e olha se arvore esta vazia 
        if (arvore.root!=None and quantidaNosTirar>0):
             #debug
            if(log.verificar[4]):
                print("Quantidade tirada",quantidaNosTirar)
                print("largura banda: %i"%(len(listaEsperaCacheblocoOrdenado[:larguraBanda])))
                log.escreverVerificar("InicioLeitura")
                arvore.inOrderLog(arvore.root,log)
                log.escreverVerificar("InicioLeituraRemocao")
            arvore.removerQuantidade(arvore.root,listaSub,quantidaNosTirar,listaFilmes,log)
             #debug
            if(log.verificar[4]):
                arvore.inOrderLog(arvore.root,log)
                log.escreverVerificar("Fimleitura")
                arvore.inOrder(arvore.root)
                print("")
        #Fim do contado de tempo gerar a lista de substituição atraves da arvore
        fim2 = time.time()
        calculo=fim2 - inicio2
        terceiroT[0]+=calculo
        terceiroT[1]+=1
        resultado.tempoGerarTabelaSubstituicaoDef(calculo)

        #debug
        if(log.verificar[4]):
            log.escrever("Lista substituição:",len(listaSub))
            log.escrever("Lista TotalEspera:",len(listaEsperaCacheOrdemChegada))
            log.escrever("Lista Total banda:",len(listaEsperaCacheblocoOrdenado[:larguraBanda]))
        
            quant=0
            log.escreverVerificar("Verificação 04")
            quantidadeNaoEncontrado=0 
            for idFilme in listaFilmes:
                quantidadeNaoEncontrado=listaFilmes[idFilme].verificar(quantidadeNaoEncontrado,log)
                quant+=len(listaFilmes[idFilme].blocos)
            quantidade={}
            quantidade['quantidade']=0
            log.escrever("")
            arvore.quatidadeItems(arvore.root,quantidade)            
            log.escreverVerificar(["Diferentes 4",quantidade['quantidade'],len(memoria),len(listaSub),quantidadeNaoEncontrado])
            if((quantidade['quantidade']+len(listaSub))!=len(memoria) or quantidadeNaoEncontrado!=len(listaSub)):
                print(["Diferentes 4",quantidade['quantidade'],len(memoria),len(listaSub),quantidadeNaoEncontrado])
                breakpoint()
        


        inicio2 = time.time()      
        #distribuindo os pacotes foram recebidos
        for cliente in listaEsperaCacheOrdemChegada:
            quartoT[2]+=1
            inicio4 = time.time()
            #verifica se o bloco foi selecionado para usar a banda de dados
            if(((str(cliente.idBloco+1)+'-'+str(cliente.idFilme))) in listaEsperaCacheblocoOrdenado[:larguraBanda]):
                #Inicio contado 
                inicio3 = time.time()
                #Adicona +1 na taxa de acerto se pacote foi selecionado para uso da banda
                resultado.acerto()
                #muda o mapeamento do cliente  dentro da lista do filme.  
                if(listaFilmes[cliente.idFilme].blocos.get((cliente.idBloco+1))):
                    if(cliente.idBloco==-1):
                        listaFilmes[cliente.idFilme].numeroClientes+=1
                    else:
                        if((listaFilmes[cliente.idFilme].blocos).get(cliente.idBloco)!=None):
                            listaFilmes[cliente.idFilme].blocos[cliente.idBloco]-=1
                    cliente.idBloco+=1        
                    
                    if((listaFilmes[cliente.idFilme].blocos).get(cliente.idBloco)!=None):
                        listaFilmes[cliente.idFilme].blocos[cliente.idBloco]+=1
                    else:
                        listaFilmes[cliente.idFilme].blocos[cliente.idBloco]=1
                    #Ja mexe na classificação do bloco
                    algoritmo.alterarClassificar(argumento,listaFilmes,cliente,instanteTempo) 
                    
                    resultado.cachePacote()
                    #log.escrever(listaFilmes[cliente.idFilme].classificacao)
                    memoria[listaFilmes[cliente.idFilme].blocoMemoria[cliente.idBloco]]=([cliente.idFilme,cliente.idBloco,listaFilmes[cliente.idFilme].blocos[cliente.idBloco],algoritmo.variavelGenericaMemoriaAcerto(memoria[listaFilmes[cliente.idFilme].blocoMemoria[cliente.idBloco]][3])])
                else:
                    if(memoriaTotal>len(memoria)):
                        #muda o mapeamento do cliente  dentro da lista do filme.  
                        if(cliente.idBloco==-1):
                            listaFilmes[cliente.idFilme].numeroClientes+=1
                        else:
                            if((listaFilmes[cliente.idFilme].blocos).get(cliente.idBloco)!=None):
                                listaFilmes[cliente.idFilme].blocos[cliente.idBloco]-=1
                        cliente.idBloco+=1
                        
                        if((listaFilmes[cliente.idFilme].blocos).get(cliente.idBloco)!=None):
                            listaFilmes[cliente.idFilme].blocos[cliente.idBloco]+=1
                        else:
                            listaFilmes[cliente.idFilme].blocos[cliente.idBloco]=1
                        #Ja mexe na classificação do bloco
                        algoritmo.alterarClassificar(argumento,listaFilmes,cliente,instanteTempo)    
                        
                        #Adiciona bloco na matriz filmex bloo .  dizer que o bloco esta na memoria
                        listaFilmes[cliente.idFilme].blocoMemoria[cliente.idBloco]=len(memoria)
                        #adicona no bloco na memoria, se a memoria não estiver cheia ainda
                        memoria.append([cliente.idFilme,cliente.idBloco,listaFilmes[cliente.idFilme].blocos[cliente.idBloco],algoritmo.variavelGenericaMemoriaCriacao(listaFilmes[cliente.idFilme],memoriaTotal,cliente.idBloco)])
                    else:
                        algoritmo.substituicaoBlocos(listaFilmes,cliente,memoria,listaClientes,listaEsperaCacheblocoOrdenado[:larguraBanda],listaSub.pop((list(listaSub)).pop(0)),instanteTempo)
                #Fim contado 
                fim3 = time.time()
                calculo2=fim3 - inicio3
                quartoT1[0]+=calculo2
                quartoT1[1]+=1

            else:
                #inicio Contador
                inicio3 = time.time()
                #Pular de bloco
                cliente.idBloco+=1
                #Ja mexe na classificação do bloco
                algoritmo.alterarClassificar(argumento,listaFilmes,cliente,instanteTempo)
                
                #Para adicoiona erro na taxa de erros
                resultado.erro()
                #fim contador 
                fim3 = time.time()
                calculo2=fim3 - inicio3
                quartoT3[0]+=calculo2
                quartoT3[1]+=1
                #pri.AdicionarDadosPlanilha(memoria,listaClientes,instanteTempo,result.acertos,result.erros,listaFilmes,memoriaTotal)
                #printDados.intefase3(instanteTempo,result,memoria,memoriaTotal,listaClientes,listaFilmes,algorimo.classificacao)
        #fim contador  loop da fila de espera
        fim2 = time.time()
        calculo=fim2 - inicio2
        quartoT[0]+=calculo
        quartoT[1]+=1
        #Uma validação, para verificar lista substuição removida da arvore, não removeu item amais que a lista espera
        if(len(listaSub)!=0):
            log.escrever("Lista Esta Errada %i"%(len(listaSub)))
            breakpoint()
        #Inicion contasadores arrumar a classificação na arvores, colocado aqui, pois evitar q seja nessario fazer modificação na arvore mais que uma vez no loop final
        inicio2 = time.time()
        #for value in listaEsperaCacheblocoOrdenado[:larguraBanda]:
        for value in listaEsperaCacheblocoOrdenado:
            dado=value.split('-')
            algoritmo.calcularClasificacao(int(dado[0]),listaFilmes[int(dado[1])], arvore)
            cincoT[2]+=1
        #Debug
        if(log.verificar[5]):
            quant=0
            log.escreverVerificar("Verificação 05")
            quantidadeNaoEncontrado=0
            for idFilme in listaFilmes:
                quantidadeNaoEncontrado=listaFilmes[idFilme].verificar(quantidadeNaoEncontrado,log)
                quant+=len(listaFilmes[idFilme].blocos)
            quantidade={}
            quantidade['quantidade']=0
            arvore.quatidadeItems(arvore.root,quantidade)
            log.escreverVerificar(["Diferentes 5",quantidade['quantidade'],len(memoria),len(listaSub),quantidadeNaoEncontrado])
            if((quantidade['quantidade']+len(listaSub))!=len(memoria) or quant!=len(memoria) or quantidadeNaoEncontrado!=len(listaSub)):
                print(["Diferentes 5",quantidade['quantidade'],len(memoria),len(listaSub),quantidadeNaoEncontrado])
                breakpoint()
        #Fim contasadores arrumar a classificação na arvores    
        fim2 = time.time()
        calculo=fim2 - inicio2
        cincoT[0]+=calculo
        cincoT[1]+=1
        
        
        resultado.tempoDistribucaoNaRequicaoAtendidasDef(calculo)
        
        #Para a simulação nesse numero ciclos,  aprota tiraremos é do ciclo 5600 a 6600
        if((instanteTempo>6610)):
            #Salva os dados dos tempos, tambem podem aparece printado na tela            
            log.escreverTempo("1)"+str(primeiroT))
            log.escreverTempo("1-2)"+str(primeiroT2))
            log.escreverTempo("1-3)"+str(primeiroT3))
            log.escreverTempo("1-4)"+str(primeiroT4))
            log.escreverTempo("1-5)"+str(primeiroT5))
            log.escreverTempo("1-6)"+str(primeiroT6))
            log.escreverTempo("2)"+str(segundoT))
            log.escreverTempo("2-2)"+str(segundoT2))
            log.escreverTempo("2-3)"+str(segundoT3))
            log.escreverTempo("3)"+str(terceiroT))
            log.escreverTempo("4)"+str(quartoT))
            log.escreverTempo("5)"+str(cincoT))
            log.escreverTempo("4-1)"+str(quartoT1))
            log.escreverTempo("4-2)"+str(quartoT2))
            log.escreverTempo("4-3)"+str(quartoT3))
            log.escreverTempo("4-4)"+str(quartoT4))
            log.escreverTempo("4-5)"+str(quartoT5))
            log.fechar()
            
            #Fim do contador do inicio do ciclo
            fim = time.time()
            calculo=fim - inicioTempo
            resultado.tempoCicloDef(calculo)
            calculo=fim - inicio
            resultado.adiconarTempo(instanteTempo,larguraBanda,tamLista)
            #Bloqueia  no momento salvar, inpedir salvamento de dois dados ao mesmo tempo por causa do treads paralelos
            lock.acquire()
            #Salva os resultados da similução de todos os ciclos
            resultado.salvarDados(calculo,instanteTempo,classAlgoritmo+str(inputEntrada))
            #Desbloqueio
            lock.release()

            #Fim do contador de tempo de todas os ciclos
            tempoFinalFuncao= time.time()
            calculoSimulacao=tempoFinalFuncao - tempoInicialFuncao
            log.escreverVerificarSimulacao(calculoSimulacao)
            #Para a simulação, saido do while true da função
            break
        else:
            #Fim contador tempo  do ciclo
            fim = time.time()
            calculo=fim - inicioTempo
            resultado.tempoCicloDef(calculo)
            resultado.adiconarTempo(instanteTempo,larguraBanda,tamLista)
            #Adiciona +1 para ciclo
            instanteTempo=instanteTempo+1
           
  
#Função da escolha algoritmos
def parametroInput(opcaoALgoritmo,lock,pasta,memoriaTotal,larguraBanda,video,inputEntrada):
    res=0
    listaThread=[]
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            arq=pasta+"/"+arquivo
            if(opcaoALgoritmo==1):
                thread=(multiprocessing.Process(target=execucao,args=(False,lock, res,arq,'algoritmoLRU','AlgoritmoLRU','0',int(math.ceil((memoriaTotal*1024)/0.63)),int(math.ceil(((larguraBanda*1024)/0.63)/8)),int(math.ceil((video*1024)/0.63)),inputEntrada,False,False)))
                listaThread.append(thread)
            elif(opcaoALgoritmo==2):
                thread=(multiprocessing.Process(target=execucao,args=(False,lock, res,arq,'algoritmoLFU','AlgoritmoLFU','0',int(math.ceil((memoriaTotal*1024)/0.63)),int(math.ceil(((larguraBanda*1024)/0.63)/8)),int(math.ceil((video*1024)/0.63)),inputEntrada,False,False)))
                listaThread.append(thread)
            elif(opcaoALgoritmo==3):
                thread=(multiprocessing.Process(target=execucao,args=(False,lock, res,arq,'algoritmoFifo','AlgoritmoFIFO','0',int(math.ceil((memoriaTotal*1024)/0.63)),int(math.ceil(((larguraBanda*1024)/0.63)/8)),int(math.ceil((video*1024)/0.63)),inputEntrada,False,False)))
                listaThread.append(thread)
            elif(opcaoALgoritmo==4):
                thread=(multiprocessing.Process(target=execucao,args=(False,lock, res,arq,'algoritmoRandon','AlgoritmoRandon','0',int(math.ceil((memoriaTotal*1024)/0.63)),int(math.ceil(((larguraBanda*1024)/0.63)/8)),int(math.ceil((video*1024)/0.63)),inputEntrada,False,False)))
                listaThread.append(thread)
            elif(opcaoALgoritmo==8):
                thread=(multiprocessing.Process(target=execucao,args=(False,lock, res,arq,'algoritmoCC','AlgoritmoCC',"0",int(math.ceil((memoriaTotal*1024)/0.63)),int(math.ceil(((larguraBanda*1024)/0.63)/8)),int(math.ceil((video*1024)/0.63)),inputEntrada,False,False)))
                listaThread.append(thread)  
            #Aqui vc configura sobre as janela.  Função que vai gerar muitas simulações de janela variavel  
            elif(opcaoALgoritmo==5):
                janela=10
                while janela<110:
                    thread=(multiprocessing.Process(target=execucao,args=(False,lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(janela),int(math.ceil((memoriaTotal*1024)/0.63)),int(math.ceil(((larguraBanda*1024)/0.63)/8)),int(math.ceil((video*1024)/0.63)),inputEntrada,False,False)))
                    listaThread.append(thread)
                    janela+=10
            elif(opcaoALgoritmo==6):
                janela=10
                while janela<3000:
                    thread=(multiprocessing.Process(target=execucao,args=(False,lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(janela),int(math.ceil((memoriaTotal*1024)/0.63)),int(math.ceil(((larguraBanda*1024)/0.63)/8)),int(math.ceil((video*1024)/0.63)),inputEntrada,False,False)))
                    listaThread.append(thread) 
                    janela+=50
            elif(opcaoALgoritmo==7):
                janela=10   
                while janela<300:
                    thread=(multiprocessing.Process(target=execucao,args=(False,lock, res,arq,'algoritmoCARTE','AlgoritmoCarte',str(janela),int(math.ceil((memoriaTotal*1024)/0.63)),int(math.ceil(((larguraBanda*1024)/0.63)/8)),int(math.ceil((video*1024)/0.63)),inputEntrada,False,False)))
                    listaThread.append(thread)
                    janela+=10
    return listaThread

if __name__ == "__main__":

    #Listas a diretorio de leitura, tem "baseLeitura"
    print("Diretorio Leuturia")
    listaDiretorios=[]
    for diretorio, subpastas, arquivos in os.walk("../",topdown=False):
        if("../baseLeitura" in diretorio):
            print(str(len(listaDiretorios))+"-"+"("+diretorio+")")
            listaDiretorios.append(diretorio)
    print(len(sys.argv))
    if(len(sys.argv)<2):
        diretoriaDeLeitura=input()
    else:        
        diretoriaDeLeitura=sys.argv[1]
    #opcao execução
    print("1-Varia memoria 1GB a 25 GB  pulos 1GB")
    print("2-Varia memoria 25GB a 50 GB pulos 1GB ")
    print("3-Varia banda 0,4Gb a 4Gb blocos pulos 50 blocos")
    print("5-Varia video 0.5GB a 10GB  pulos 0.5GB  Operacao:")
    print("6-ConfiguraçãoPadrao")
    try:
        #Pega o valor por agumentos ou pelo terminal
        if(len(sys.argv)<3):
            inputEntrada=input()
        else:        
            inputEntrada=sys.argv[2]
        inputEntrada=int(inputEntrada)
        listaThread=[]
        lock = multiprocessing.Lock()
        #parametroFixo, pode mudar de acorodo opção escolida
        memoriaTotal=14
        larguraBanda=3.4
        video=3.4
        #Caminho dos arquivos leitura 
        pasta = listaDiretorios[diretoriaDeLeitura]
        
        if(inputEntrada==1):
            print("1)LRU 2)LFU 3)FIFO 4)Randon 5)LRU com Janela 6)LFU com Janela 7)Carte 8)CC ")
            if(len(sys.argv)<4):
                opcaoALgoritmo=input()
            else:        
                opcaoALgoritmo=sys.argv[2]
            opcaoALgoritmo=int(opcaoALgoritmo)
            #Iniciar variavel de valor inicial simulação
            memoriaTotal=1            
            while memoriaTotal<=25:
                listaThread+=parametroInput(opcaoALgoritmo,lock,pasta,memoriaTotal,larguraBanda,video,inputEntrada)
                memoriaTotal+=1
        elif(inputEntrada==2):
            print("1)LRU 2)LFU 3)FIFO 4)Randon 5)LRU com Janela 6)LFU com Janela 7)Carte 7)CC ")
            if(len(sys.argv)<4):
                opcaoALgoritmo=input()
            else:        
                opcaoALgoritmo=sys.argv[2]
            opcaoALgoritmo=int(opcaoALgoritmo)
            memoriaTotal=26            
            while memoriaTotal<=50:
                listaThread+=parametroInput(opcaoALgoritmo,lock,pasta,memoriaTotal,larguraBanda,video,inputEntrada)
                memoriaTotal+=1    
        elif(inputEntrada==3):
            print("1)LRU 2)LFU 3)FIFO 4)Randon 5)LRU com Janela 6)LFU com Janela 7)Carte 7)CC ")
            if(len(sys.argv)<4):
                opcaoALgoritmo=input()
            else:        
                opcaoALgoritmo=sys.argv[2]
            opcaoALgoritmo=int(opcaoALgoritmo)
            larguraBanda=0.4          
            while memoriaTotal<=4:
                listaThread+=parametroInput(opcaoALgoritmo,lock,pasta,memoriaTotal,larguraBanda,video,inputEntrada)
                larguraBanda+=0.5
        elif(inputEntrada==5):
            print("1)LRU 2)LFU 3)FIFO 4)Randon 5)LRU com Janela 6)LFU com Janela 7)Carte 7)CC ")
            if(len(sys.argv)<4):
                opcaoALgoritmo=input()
            else:        
                opcaoALgoritmo=sys.argv[2]
            opcaoALgoritmo=int(opcaoALgoritmo)
            video=0.5          
            while memoriaTotal<=10:
                listaThread+=parametroInput(opcaoALgoritmo,lock,pasta,memoriaTotal,larguraBanda,video,inputEntrada)
                larguraBanda+=0.5
        elif(inputEntrada==6):
            print("1)LRU 2)LFU 3)FIFO 4)Randon 5)LRU com Janela 6)LFU com Janela 7)Carte 7)CC ")
            if(len(sys.argv)<4):
                opcaoALgoritmo=input()
            else:        
                opcaoALgoritmo=sys.argv[2]
            opcaoALgoritmo=int(opcaoALgoritmo)        
            listaThread+=parametroInput(opcaoALgoritmo,lock,pasta,memoriaTotal,larguraBanda,video,inputEntrada)
         
        
        #Primeiro é criado todas as thread nessecitam e depois executadas

        #Aqui vc control as thread
        #lista com tread ativas. Limitado pela varaivel tread
        listaTreadAtivos=[]
        #Valor de quantas thead vc disponibilizara para simualção
        numeorThreadMax=20
        #For inicialia as primeira thread ficarem ativas
        for k,value in enumerate(listaThread):
            if(len(listaTreadAtivos)<numeorThreadMax):
                thread=listaThread.pop(0)
                thread.start()
                print(thread)
                listaTreadAtivos.append(thread)
        #Tupe verifica as thread acabaram e vai controcandas lugar para proxima thread.  Cada thread é uma simualçao diferentes executando
        while True: 
            for key, value in enumerate(listaTreadAtivos[:]):
                if(value.is_alive() is False):
                    value.join() 
                    print("\nfim da thread "+str(key)+" - Tem mais "+str(len(listaThread)))
                    if(len(listaThread)>0):
                        thread=listaThread.pop(0)
                        thread.start();
                        print("\nmais trad")
                        listaTreadAtivos[key]=thread
                    else:
                        del listaTreadAtivos[key]
            #espera a lista tread ativas acapara  finalizar o loop
            if(len(listaTreadAtivos)==0):
                print("\nFim"+str(len(listaTreadAtivos)))
                break
                    
        #Aqui imprimit no fina executação.  Para que não seja fechado a execução de ocorreu um erro ou acabou todas as simualções.  Para ter controle das simulações que finalizaram            
        print("Finalizado Execução")
        print("Opcao configuraçao:",inputEntrada,"Algoritmos:",opcaoALgoritmo)
        arquivo1=open("./Execucao.txt","a")
        arquivo1.write("Finalizado Execução \n")
        arquivo1.write("Opcao configuraçao:"+str(inputEntrada)+"Algoritmos:"+str(opcaoALgoritmo)+"\n")
    except Exception as e:
        arquivo1 = open("./Execucao.txt", "a")
        arquivo1.write("Erro\n")
        arquivo1.write("Opcao configuraçao:"+str(inputEntrada)+"Algoritmos:"+str(opcaoALgoritmo)+"\n")
        arquivo1.write(str(e)+"\n")
    finally:
        arquivo1.close()
    