# -*- coding: utf-8 -*-
from clas.manipulacaoArquivo import ManipulacaoArquivo
# from algoritmoAleatorio import AlgortimoAleatorio
##from algoritmoCARTE import AlgortimoCARTE
# from algoritmoCC import AlgoritmoCC
#from algoritmoLRU import AlgoritmoLRU
#from algoritmoLFU import AlgoritmoLFU
from clas.resultado import Resultado
from clas.cliente import Cliente
from clas.filme import Filme
from clas.printDados import PrintDados
from clas.planilhaODS import PlaniliaOBS
from clas.pacote import Pacote
from clas.geradorGraficos import GeradorGraficos
import time
import threading
import csv 
import os
import math
def execucao(lock,res,arquivo,arquivoAgoritmo,classAlgoritmo,argumento,memoriaTotal,larguraBanda,tamanhoVideo):
    
    #alg="algorimo=AlgortimoAleatorio()"
    #alg="algorimo=AlgortimoCC()"
    #alg="algorimo=AlgoritmoLFU()"
    #alg="algorimo=AlgoritmoLRU()"

    #algorimo=AlgortimoAleatorio()
    #print(str("from algoritmo."+arquivoAgoritmo+" import "+classAlgoritmo))
    #print((str("algoritmo="+classAlgoritmo+"("+argumento+")")))
    
    #from algoritmo.algoritmoLRU import AlgoritmoLRU
    impor=str("from algoritmo."+arquivoAgoritmo+" import "+classAlgoritmo)
    exec(impor,globals()) 
    comand=str("algoritmo="+classAlgoritmo+"("+argumento+")")
    exec(comand,globals())
    #Lista q tem infomaçoes da memoria proxy de video
    memoria=[]

    #filaEspera=[]
    #Classe resposavel salvar os resultados finais em txt, manter historico da valores a cada segundo
    grafico=GeradorGraficos(arquivo,algoritmo.nomeAlgoritmo,memoriaTotal,larguraBanda,tamanhoVideo)

    #tempo medido tempo proxy,não funciona na escala tempo real
    instanteTempo=0
    #Isso para inciar com cliente na memoria de leitura
    leitura=ManipulacaoArquivo('./../baseLeitura/'+str(arquivo),grafico,classAlgoritmo)
    novoCliente=leitura.novoClienteLido(tamanhoVideo)
    
    
    #Contem todos cliente ativos ou em espera. Ele estao em ordem q quem chega primeiro , primeiro receber.
    listaClientes=[]
    #Matriz que  tem infomaçoes do filme e possição da memoria se encontra bloco.  Funciona como Organição de memoria Indexada
    listaFilmes={}
    #Tem os contadores  dentro, é chamada para adcionar erro ou  acertos.
    print(algoritmo.nomeAlgoritmo) 
    result=Resultado(arquivo,algoritmo.nomeAlgoritmo)
    #pri=PlaniliaOBS()
    #pri.iniciarPlanilha()
    printDados=PrintDados()
    inicio = time.time()
    
    ##Verificando  se ja tem dados salvos, carega ponto  antes de 
    # carregado=True
    # print("ola mundo 2 ")
    # if(os.path.exists(leitura.caminho)):
    #     print("ola mundo ")
    #     memoria=leitura.carregarMemoria()
    #     instanteTempo=leitura.carregarInstanteTempo()
    #     novoCliente=leitura.carregarNovoCliente()
    #     listaClientes=leitura.carregarListaClientes()
    #     listaFilmes=leitura.carregarListaFilmes()
    #     result=leitura.carregarResult()
    #     inicio=leitura.carregarInicio()
    #     grafico=leitura.carregarGrafico()
    #     carregado=False
    # leitura.abrindoSalvamentoMemoria()
    while True:
        #print(alg)
        # leitura.salvandoMemoria(memoria)
        #Leitura de novo  cliente e veirificação  de colocar na lista
        inicioTempo = time.time()
        inicio2 = time.time()
        # if(memoriaTotal>len(memoria)):
        #     leitura.salvarLocal(memoria,instanteTempo,novoCliente,listaClientes,listaFilmes,result,inicio,grafico)

        while (novoCliente!=0 and novoCliente.tempoInicio==instanteTempo):
            result.novoCliente()
            grafico.novoCliente()
            listaClientes.append(novoCliente)
            if(novoCliente.idFilme in listaFilmes):
                listaFilmes[novoCliente.idFilme].clientes[novoCliente.idCliente]=novoCliente
            else:
                listaFilmes[novoCliente.idFilme]=Filme(novoCliente.idFilme)
                listaFilmes[novoCliente.idFilme].clientes[novoCliente.idCliente]=novoCliente
            novoCliente=leitura.novoClienteLido(tamanhoVideo)
        fim2 = time.time()
        calculo=fim2 - inicio2
        grafico.tempoEntradaClienteDef(calculo)
        #print("While entrada Clientes:%.2f "%(calculo))
        #pri.AdicionarDadosPlanilha(memoria,listaClientes,instanteTempo,result.acertos,result.erros,listaFilmes,memoriaTotal)
        #printDados.intefase3(instanteTempo,result,memoria,memoriaTotal,listaClientes,listaFilmes,algoritmo.classificacao)
        #Substituição da parte dos cliente atendendo
        contadorLarguraBanda=0;
        listaEsperaCachebloco={}
        listaEsperaCacheFilme={}
        listaEsperaCacheOrdemChegada=[]
        
        inicio2 = time.time()
        #print("Segundo")
        for cliente in (listaClientes[:]):
            #Remover o cliente q terminou de assistir video da lista
            if(cliente.idBloco==cliente.tamanhoBloco):
                result.terminouCliente()
                grafico.terminouCliente()
                del listaFilmes[cliente.idFilme].clientes[cliente.idCliente]
                listaClientes.remove(cliente)
            else: 
                memoria=algoritmo.organizarMemororia(memoria)
                if(cliente.idFilme in listaFilmes):
                    if((cliente.idBloco+1) in listaFilmes[cliente.idFilme].blocos):
                        cliente.trocaBloco(listaFilmes)
                        memoria[listaFilmes[cliente.idFilme].blocoMemoria[cliente.idBloco]]=([cliente.idFilme,cliente.idBloco,listaFilmes[cliente.idFilme].blocos[cliente.idBloco],algoritmo.variavelGenericaMemoriaAcerto(memoria[listaFilmes[cliente.idFilme].blocoMemoria[cliente.idBloco]][3])])
                        result.acerto()
                        grafico.acerto()
                        grafico.cachePacote()
                    else:
                        result.erroBanda()
                        grafico.solicBanda()
                        if(cliente.idFilme in listaEsperaCacheFilme.keys()):
                            if(str(cliente.idBloco)+'-'+str(cliente.idFilme) in listaEsperaCachebloco.keys()):
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
                else:
                    result.erroBanda()
                    grafico.solicBanda()
                    if(cliente.idFilme in listaEsperaCacheFilme.keys()):
                        if(str(cliente.idBloco)+'-'+str(cliente.idFilme) in listaEsperaCachebloco.keys()):
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
        fim2 = time.time()
        calculo=fim2 - inicio2
        grafico.tempoDistribucaoNaCacheDef(calculo)
        #print("1° For :%.2f "%(calculo))
        inicio2 = time.time()
        tamLista=len(listaEsperaCachebloco)
        listaEsperaCacheblocoOrdenado=(sorted(listaEsperaCachebloco, key=lambda pac: ((((listaEsperaCachebloco[pac].contador*tamLista)+listaEsperaCacheFilme[listaEsperaCachebloco[pac].idFilme])*tamLista)+(tamLista-listaEsperaCachebloco[pac].posicao)),reverse=True))
        fim2 = time.time()
        calculo=fim2 - inicio2
        grafico.tempoOrdenacaoPedidosRequisicaoDef(calculo)
        #print("Sorted:%.2f "%(calculo))
        #listaEsperaCacheFilmeOrdenado=(sorted(listaEsperaCacheFilme, key=lambda pac: listaEsperaCacheFilme[pac],reverse=True))

        inicio2 = time.time()
        listaSub=algoritmo.calcularTabelaSubituicao(memoria,listaClientes,listaFilmes,listaEsperaCacheblocoOrdenado[:larguraBanda])
        fim2 = time.time()
        calculo=fim2 - inicio2
        # print('1')
        # print(calculo)
        # inicio2 = time.time()
        # /listaSub1=algoritmo.calcularTabelaSubituicaoComThread(memoria,listaClientes,listaFilmes,listaEsperaCacheblocoOrdenado[:larguraBanda])
        # fim2 = time.time()
        # calculo=fim2 - inicio2
        # print('2')
        # print(calculo)
        grafico.tempoGerarTabelaSubstituicaoDef(calculo)
        #print("Tabela Substuição:%.2f "%(calculo))
        #listaEsperaCacheFilme.sort(reverse=True)
        #print(listaEsperaCacheblocoOrdenado)
        #print(listaEsperaCacheFilmeOrdenado)
        inicio2 = time.time()
        for cliente in listaEsperaCacheOrdemChegada:
            if((str(cliente.idBloco+1)+'-'+str(cliente.idFilme)) in listaEsperaCacheblocoOrdenado[:larguraBanda]):
                result.acerto()
                grafico.acerto()
                if(cliente.idFilme in listaFilmes):
                    if((cliente.idBloco+1) in listaFilmes[cliente.idFilme].blocos):
                        cliente.trocaBloco(listaFilmes)
                        grafico.cachePacote()
                        memoria[listaFilmes[cliente.idFilme].blocoMemoria[cliente.idBloco]]=([cliente.idFilme,cliente.idBloco,listaFilmes[cliente.idFilme].blocos[cliente.idBloco],algoritmo.variavelGenericaMemoriaAcerto(memoria[listaFilmes[cliente.idFilme].blocoMemoria[cliente.idBloco]][3])])
                    else:
                        if(memoriaTotal>len(memoria)):
                            cliente.trocaBloco(listaFilmes)
                            listaFilmes[cliente.idFilme].blocoMemoria[cliente.idBloco]=len(memoria)
                            memoria.append([cliente.idFilme,cliente.idBloco,listaFilmes[cliente.idFilme].blocos[cliente.idBloco],algoritmo.variavelGenericaMemoriaCriacao()])
                        else:
                            # inicio3 = time.time()
                            if(len(listaSub)==0):
                                inicio3 = time.time()
                                listaSub=algoritmo.calcularTabelaSubituicao(memoria,listaClientes,listaFilmes,listaEsperaCacheblocoOrdenado[:larguraBanda])
                                fim3 = time.time()
                                calculo=fim3 - inicio3
                                inicio2=inicio2+calculo
                                grafico.tempoGerarTabelaSubstituicaoDef(calculo)
                            algoritmo.substituicaoBlocos(listaFilmes,cliente,memoria,listaClientes,listaEsperaCacheblocoOrdenado[:larguraBanda],listaSub.pop(0))
                            # fim3 = time.time()
                            # calculo=fim3 - inicio3
                            # print("Substituição1:%.2f "%(calculo))
                else:
                    listaFilmes[cliente.idFilme]=Filme(cliente.idFilme)
                    if(memoriaTotal>len(memoria)):
                        #Função dentro do cliente para habilitar o novo pacote de video
                        cliente.trocaBloco(listaFilmes)
                        #Fucão quarda possocição do memoria dentro bloco .  Reduzir tempo de busca em toda memoria
                        listaFilmes[cliente.idFilme].blocoMemoria[cliente.idBloco]=len(memoria)
                        #adiciona na memoria o bloco de video
                        memoria.append([cliente.idFilme,cliente.idBloco,listaFilmes[cliente.idFilme].blocos[cliente.idBloco],algoritmo.variavelGenericaMemoriaCriacao()])
                    else:
                        #Função dentro algoritmo de substituicao escolhido
                        # inicio3 = time.time()
                        if(len(listaSub)==0):
                            inicio3 = time.time()
                            listaSub=algoritmo.calcularTabelaSubituicao(memoria,listaClientes,listaFilmes,listaEsperaCacheblocoOrdenado[:larguraBanda])
                            fim3 = time.time()
                            calculo=fim3 - inicio3
                            inicio2=inicio2+calculo
                            grafico.tempoGerarTabelaSubstituicaoDef(calculo)
                        algoritmo.substituicaoBlocos(listaFilmes,cliente,memoria,listaClientes,listaEsperaCacheblocoOrdenado[:larguraBanda],listaSub.pop(0))
                        # fim3 = time.time()
                        # calculo=fim3 - inicio3
                        # print("Substituição2:%.2f "%(calculo))
            else:
                cliente.idBloco+=1
                result.erro()
                grafico.erro()
                #pri.AdicionarDadosPlanilha(memoria,listaClientes,instanteTempo,result.acertos,result.erros,listaFilmes,memoriaTotal)
                #printDados.intefase3(instanteTempo,result,memoria,memoriaTotal,listaClientes,listaFilmes,algorimo.classificacao)
        fim2 = time.time()
        calculo=fim2 - inicio2
        grafico.tempoDistribucaoNaRequicaoAtendidasDef(calculo)
        #print("2 For: %.2f "%(calculo))
        #Verficação final para ver se acabou  a distribuição ou  vai ter q contabilidar mais uma tempo
        if(novoCliente==0 and len(listaClientes)==0):
            #print(novoCliente)
            fim = time.time()
            calculo=fim - inicioTempo
            grafico.tempoCicloDef(calculo)
            calculo=fim - inicio
            grafico.adiconarTempo(instanteTempo,larguraBanda,tamLista)
            lock.write_acquire()
            grafico.salvarDados(calculo,instanteTempo)
            lock.write_release()
            #leitura.FechandoAbrindoSalvamentoMemoria()
            #grafico.graficoGerar(memoriaTotal,larguraBanda)
            #leitura.escritaResult(result)
            break
        else:
            fim = time.time()
            calculo=fim - inicioTempo
            grafico.tempoCicloDef(calculo)
            grafico.adiconarTempo(instanteTempo,larguraBanda,tamLista)
            instanteTempo=instanteTempo+1
            #print(instanteTempo)
            
            #print("Tempo do Ciclo %i :%.2f" %(instanteTempo,calculo))
    # pri.salvarArquivo()
class RWLock:
    #construtor
    def __init__(self):
        self.readers = 0
        self.mutex = threading.Semaphore(1) #Semáforo de leitura
        self.lock = threading.Semaphore(1)  #Semáforo de escrita
    def read_acquire(self):
        self.mutex.acquire() #bloqueia para leitura
        self.readers += 1 #soma a quantidade de leitores
        if self.readers == 1:
            self.lock.acquire() #Se você é o primeiro leitor, bloqueie o recurso dos escritores.
                                # Recurso permanece reservado para leitores subseqüentes
        self.mutex.release() # desbloqueia
    def read_release(self):
        self.mutex.acquire() #bloqueia para leitura
        self.readers -= 1
        if self.readers == 0:
            self.lock.release() #Se você for o último leitor, poderá desbloquear o recurso. 
                                # Isso torna disponível para escritores.
        self.mutex.release() #desbloqueia
    def write_acquire(self):
        self.lock.acquire() #bloqueia o semaforo de escrita
    def write_release(self):
        self.lock.release() #desbloqueia
class SharedResource:
    def __init__(self):
        self.val = 0

#Menu  de arquivo fazer

#arquivo contem 4 colunas. (idCleintes,  numero do filme q vai assistir,  tempo de chagada , parte do  video q assistir)
if __name__ == "__main__":
    # Variael do arquivo
        #Limite de memoria  em contabilizados em bloco
    memoriaTotal=22756
        #Tamanho que banda q proxy pode usar  durante aquele intervala de 1 tempo
    arq='3gerado.txt' 
    larguraBanda=700
    video=5527
    lock = RWLock()
    res = SharedResource()
    # arq='3.txt'
    # execucao(lock, res,arq,'algoritmoFifo','AlgoritmoFIFO','',memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoRandon','AlgoritmoRandon','',memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRU','AlgoritmoLRU','',memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLFU','AlgoritmoLFU','',memoriaTotal,larguraBanda,video)
    #execucao(lock, res,arq,'algoritmoCC','AlgoritmoCC','',memoriaTotal,larguraBanda,video)
    # arq='3.txt'
    # execucao(lock, res,arq,'algoritmoCC','AlgoritmoCC','',memoriaTotal,larguraBanda,video)
    # arq='3gerado.txt'
    # execucao(lock, res,arq,'algoritmoCC','AlgoritmoCC','',memoriaTotal,larguraBanda,video)
    # arq='3gerado2.txt'
    # execucao(lock, res,arq,'algoritmoCC','AlgoritmoCC','',memoriaTotal,larguraBanda,video)
    # arq='3gerador3.txt'
    # execucao(lock, res,arq,'algoritmoCC','AlgoritmoCC','',memoriaTotal,larguraBanda,video)
    # arq='3gerado4.txt'
    # execucao(lock, res,arq,'algoritmoCC','AlgoritmoCC','',memoriaTotal,larguraBanda,video)
    # arq='3gerado5.txt'
    # execucao(lock, res,arq,'algoritmoCC','AlgoritmoCC','',memoriaTotal,larguraBanda,video)
    # arq='3gerado6.txt'
    # execucao(lock, res,arq,'algoritmoCC','AlgoritmoCC','',memoriaTotal,larguraBanda,video)
    # arq='3gerado7.txt'
    # execucao(lock, res,arq,'algoritmoCC','AlgoritmoCC','',memoriaTotal,larguraBanda,video)
    # arq='3gerado8.txt'
    # execucao(lock, res,arq,'algoritmoCC','AlgoritmoCC','',memoriaTotal,larguraBanda,video)
    # arq='3gerado9.txt'
    # execucao(lock, res,arq,'algoritmoCC','AlgoritmoCC','',memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRU','AlgoritmoLRU','',memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLFU','AlgoritmoLFU','',memoriaTotal,larguraBanda,video)
    # arq='3gerado2.txt'
    # execucao(lock, res,arq,'algoritmoLRU','AlgoritmoLRU','',memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLFU','AlgoritmoLFU','',memoriaTotal,larguraBanda,video)
    # arq='3gerador3.txt'
    #execucao(lock, res,arq,'algoritmoLRU','AlgoritmoLRU','',memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLFU','AlgoritmoLFU','',memoriaTotal,larguraBanda,video)
    

    #execucao(lock, res,'texteZip2500.txt','algoritmoLRU','AlgoritmoLRU','',10,1,1)

    # execucao(lock, res,arq,'algoritmoCARTE','AlgoritmoCARTE',str(85),memoriaTotal,larguraBanda,video) 
    # #Segunda parte
    #memoriaTotal=11378
    #execucao(lock, res,"1t.txt",'algoritmoLRU','AlgoritmoLRU','',20,5,50)
    # larguraBanda=600
    # while larguraBanda<1001:
    #     execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(10),memoriaTotal,larguraBanda,video)
    #     execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(25),memoriaTotal,larguraBanda,video)
    #     execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(50),memoriaTotal,larguraBanda,video)
    #     execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(75),memoriaTotal,larguraBanda,video)
    #     execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(100),memoriaTotal,larguraBanda,video)
    #     execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(200),memoriaTotal,larguraBanda,video)
    #     execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(300),memoriaTotal,larguraBanda,video)
    #     execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(400),memoriaTotal,larguraBanda,video)
    #     execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(500),memoriaTotal,larguraBanda,video)
    #     execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(600),memoriaTotal,larguraBanda,video)
    #     execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(700),memoriaTotal,larguraBanda,video)
    #     execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(800),memoriaTotal,larguraBanda,video)
    #     execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(900),memoriaTotal,larguraBanda,video)
    #     execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(1000),memoriaTotal,larguraBanda,video)
    #     larguraBanda+=100
        
    # larguraBanda=100
    # while larguraBanda<501:
    #     # execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(10),memoriaTotal,larguraBanda,video)
    #     # execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(25),memoriaTotal,larguraBanda,video)
    #     # execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(50),memoriaTotal,larguraBanda,video)
    #     # execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(75),memoriaTotal,larguraBanda,video)
    #     execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(100),memoriaTotal,larguraBanda,video)
    #     # execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(200),memoriaTotal,larguraBanda,video)
    #     # execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(300),memoriaTotal,larguraBanda,video)
    #     # execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(400),memoriaTotal,larguraBanda,video)
    #     # execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(500),memoriaTotal,larguraBanda,video)
    #     # execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(600),memoriaTotal,larguraBanda,video)
    #     # execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(700),memoriaTotal,larguraBanda,video)
    #     execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(800),memoriaTotal,larguraBanda,video)
    #     # execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(900),memoriaTotal,larguraBanda,video)
    #     # execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(1000),memoriaTotal,larguraBanda,video)
    #     larguraBanda+=100 
    # larguraBanda=600
#    while larguraBanda<1000:
        # execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(10),memoriaTotal,larguraBanda,video)
        # execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(25),memoriaTotal,larguraBanda,video)
        # execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(50),memoriaTotal,larguraBanda,video)
        # execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(75),memoriaTotal,larguraBanda,video)
#        execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(100),memoriaTotal,larguraBanda,video)
        # execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(200),memoriaTotal,larguraBanda,video)
        # execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(300),memoriaTotal,larguraBanda,video)
        # execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(400),memoriaTotal,larguraBanda,video)
        # execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(500),memoriaTotal,larguraBanda,video)
        # execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(600),memoriaTotal,larguraBanda,video)
        # execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(700),memoriaTotal,larguraBanda,video)
#        execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(800),memoriaTotal,larguraBanda,video)
        # execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(900),memoriaTotal,larguraBanda,video)
        # execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(1000),memoriaTotal,larguraBanda,video)
#        larguraBanda+=100         
        
        
        
    # larguraBanda=700
    # memoriaTotal=1
    # while memoriaTotal<10:
    #     execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(10),int(math.ceil((memoriaTotal*1024)/0,63)),larguraBanda,video)
    #     execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(25),int(math.ceil((memoriaTotal*1024)/0,63)),larguraBanda,video)
    #     execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(50),int(math.ceil((memoriaTotal*1024)/0,63)),larguraBanda,video)
    #     execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(75),int(math.ceil((memoriaTotal*1024)/0,63)),larguraBanda,video)
    #     execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(100),int(math.ceil((memoriaTotal*1024)/0.63)),larguraBanda,video)
    #     execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(200),int(math.ceil((memoriaTotal*1024)/0,63)),larguraBanda,video)
    #     execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(300),int(math.ceil((memoriaTotal*1024)/0,63)),larguraBanda,video)
    #     execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(400),int(math.ceil((memoriaTotal*1024)/0,63)),larguraBanda,video)
    #     execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(500),int(math.ceil((memoriaTotal*1024)/0,63)),larguraBanda,video)
    #     execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(600),int(math.ceil((memoriaTotal*1024)/0,63)),larguraBanda,video)
    #     execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(700),int(math.ceil((memoriaTotal*1024)/0,63)),larguraBanda,video)
    #     execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(800),int(math.ceil((memoriaTotal*1024)/0.63)),larguraBanda,video)
    #     execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(900),int(math.ceil((memoriaTotal*1024)/0,63)),larguraBanda,video)
    #     execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(1000),int(math.ceil((memoriaTotal*1024)/0,63)),larguraBanda,video)
    #     memoriaTotal+=1
    # #Terceria parte 
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(2),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(3),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(1),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(15),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(20),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(15),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(10),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(25),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(50),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(75),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(100),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(200),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(300),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(400),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(500),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(600),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(700),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(800),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(900),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(1000),memoriaTotal,larguraBanda,video)
    
    
    # execucao(lock, res,arq,'algoritmoCC','AlgoritmoCC',"",memoriaTotal,larguraBanda,video)

    # execucao(lock, res,arq,'algoritmoCARTE','AlgoritmoCARTE',str(85),memoriaTotal,larguraBanda,video)
    
  
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(300),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(400),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(500),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(600),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(2),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(3),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(1),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(15),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(20),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(15),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(900),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(1000),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(100),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(50),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(75),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(100),memoriaTotal,larguraBanda,video)
    # memoriaTotal=6451
    # arq='3.txt' 
    # larguraBanda=20
    # video=3600
    # execucao(lock, res,'1000Texte.txt','algoritmoLRU','AlgoritmoLRU','',memoriaTotal,larguraBanda,video)
    # execucao(lock, res,'novo.txt','algoritmoLRU','AlgoritmoLRU','',memoriaTotal,larguraBanda,video)
    # execucao(lock, res,'novo.txt','algoritmoLFU','AlgoritmoLFU','',memoriaTotal,larguraBanda,video)
    # execucao(lock, res,'1000Texte.txt','algoritmoLFU','AlgoritmoLFU','',memoriaTotal,larguraBanda,video) 
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(300),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(400),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(500),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(600),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(700),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(800),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(900),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(1000),memoriaTotal,larguraBanda,video)
    #execucao(lock, res,arq,'algoritmoCARTE','AlgoritmoCARTE',str(85),memoriaTotal,larguraBanda,video) 
    
    # execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(300),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(400),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(500),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(600),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(700),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(800),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(900),memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(1000),memoriaTotal,larguraBanda,video)
    #execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(a),memoriaTotal,larguraBanda,video)
    #execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela','2',20,5,10)
    # a=103
    # execucao(lock, res,arq,'algoritmoCARTE','AlgoritmoCARTE',str(102),memoriaTotal,larguraBanda,video) 
    # while a<110:
    #     execucao(lock, res,arq,'algoritmoLRUcomJanela','AlgoritmoLRUcomJanela',str(a),memoriaTotal,larguraBanda,video)
    #     execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(a),memoriaTotal,larguraBanda,video)
    #     execucao(lock, res,arq,'algoritmoCARTE','AlgoritmoCARTE',str(a),memoriaTotal,larguraBanda,video) 
    #     print("janela"+str(a))
    #     a+=1
    #execucao(lock, res,arq,'algoritmoCARTE','AlgoritmoCARTE','2',20,5,10)
    #execucao(lock, res,'1t.txt','algoritmoLFUcomJanela','AlgoritmoLFUcomJanela','2',20,5,10)
    #execucao(lock, res,'1t.txt','algoritmoLRUcomJanela','AlgoritmoLRUcomJanela','2',20,5,10)
    #execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela','2',20,5,10)
    #execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela','2',20,5,10)
    #execucao(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela','2',20,5,10)

    #execucao(lock, res,arq,'algoritmoCC','AlgoritmoCC','',memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLRU','AlgoritmoLRU','',memoriaTotal,larguraBanda,video)
    # execucao(lock, res,arq,'algoritmoLFU','AlgoritmoLFU','',memoriaTotal,larguraBanda,video) 
    # execucao(lock, res,arq,'algoritmoCARTE','AlgoritmoCARTE','85',memoriaTotal,larguraBanda,video) 
#     listaThread=[]
#     lock = RWLock()
#     res = SharedResource()
# listaThread.append(threading.Thread(target=execucao,args=(arq,'algoritmoCC','AlgoritmoCC','',memoriaTotal,larguraBanda,video,)))
# listaThread.append(threading.Thread(target=execucao,args=(arq,'algoritmoLRU','AlgoritmoLRU','',memoriaTotal,larguraBanda,video,)))
# listaThread.append(threading.Thread(target=execucao,args=(arq,'algoritmoLFU','AlgoritmoLFU','',memoriaTotal,larguraBanda,video,)))
# listaThread.append(threading.Thread(target=execucao,args=(arq,'algoritmoCARTE','AlgoritmoCARTE','85',memoriaTotal,larguraBanda,video,)))
#     listaThread.append(threading.Thread(target=execucao,args=(lock, res,arq,'algoritmoCC','AlgoritmoCC','',50,10,20,)))
#     listaThread.append(threading.Thread(target=execucao,args=(lock, res,arq,'algoritmoLRU','AlgoritmoLRU','',50,10,20,)))
#     listaThread.append(threading.Thread(target=execucao,args=(lock, res,arq,'algoritmoLFU','AlgoritmoLFU','',50,10,20,)))
#     listaThread.append(threading.Thread(target=execucao,args=(lock, res,arq,'algoritmoCARTE','AlgoritmoCARTE','5',50,10,20,)))
#     possicao=0
#     while ( possicao<len(listaThread)):
#             listaThread[possicao].start()
#             possicao+=1
#     for t in listaThread:
#         t.join()

#listaThread.append([10,threading.Thread(target=execucao,args=(arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(10),memoriaTotal,larguraBanda,video,)))

listaThread=[]
larguraBanda=100
while larguraBanda<1001:
    listaThread.append([12,threading.Thread(target=execucao,args=(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(10),memoriaTotal,larguraBanda,video,))])
    listaThread.append([13,threading.Thread(target=execucao,args=(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(25),memoriaTotal,larguraBanda,video,))])
    listaThread.append([3,threading.Thread(target=execucao,args=(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(75),memoriaTotal,larguraBanda,video,))])
    listaThread.append([1,threading.Thread(target=execucao,args=(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(100),memoriaTotal,larguraBanda,video,))])
    listaThread.append([9,threading.Thread(target=execucao,args=(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(200),memoriaTotal,larguraBanda,video,))])
    listaThread.append([4,threading.Thread(target=execucao,args=(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(300),memoriaTotal,larguraBanda,video,))])
    listaThread.append([5,threading.Thread(target=execucao,args=(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(400),memoriaTotal,larguraBanda,video,))])
    listaThread.append([6,threading.Thread(target=execucao,args=(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(500),memoriaTotal,larguraBanda,video,))])
    listaThread.append([7,threading.Thread(target=execucao,args=(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(600),memoriaTotal,larguraBanda,video,))])
    listaThread.append([8,threading.Thread(target=execucao,args=(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(700),memoriaTotal,larguraBanda,video,))])
    listaThread.append([2,threading.Thread(target=execucao,args=(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(800),memoriaTotal,larguraBanda,video,))])
    listaThread.append([10,threading.Thread(target=execucao,args=(lock,res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(900),memoriaTotal,larguraBanda,video,))])
    listaThread.append([11,threading.Thread(target=execucao,args=(lock,res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(1000),memoriaTotal,larguraBanda,video,))])
    larguraBanda+=100 
larguraBanda=700
memoriaTotal=1
while memoriaTotal<31:
    listaThread.append([12,threading.Thread(target=execucao,args=(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(10),int(math.ceil((memoriaTotal*1024)/0.63)),larguraBanda,video,))])
    listaThread.append([13,threading.Thread(target=execucao,args=(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(25),int(math.ceil((memoriaTotal*1024)/0.63)),larguraBanda,video,))])
    listaThread.append([3,threading.Thread(target=execucao,args=(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(75),int(math.ceil((memoriaTotal*1024)/0.63)),larguraBanda,video,))])
    listaThread.append([1,threading.Thread(target=execucao,args=(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(100),int(math.ceil((memoriaTotal*1024)/0.63)),larguraBanda,video,))])
    listaThread.append([9,threading.Thread(target=execucao,args=(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(200),int(math.ceil((memoriaTotal*1024)/0.63)),larguraBanda,video,))])
    listaThread.append([4,threading.Thread(target=execucao,args=(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(300),int(math.ceil((memoriaTotal*1024)/0.63)),larguraBanda,video,))])
    listaThread.append([5,threading.Thread(target=execucao,args=(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(400),int(math.ceil((memoriaTotal*1024)/0.63)),larguraBanda,video,))])
    listaThread.append([6,threading.Thread(target=execucao,args=(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(500),int(math.ceil((memoriaTotal*1024)/0.63)),larguraBanda,video,))])
    listaThread.append([7,threading.Thread(target=execucao,args=(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(600),int(math.ceil((memoriaTotal*1024)/0.63)),larguraBanda,video,))])
    listaThread.append([8,threading.Thread(target=execucao,args=(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(700),int(math.ceil((memoriaTotal*1024)/0.63)),larguraBanda,video,))])
    listaThread.append([2,threading.Thread(target=execucao,args=(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(800),int(math.ceil((memoriaTotal*1024)/0.63)),larguraBanda,video,))])
    listaThread.append([10,threading.Thread(target=execucao,args=(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(900),int(math.ceil((memoriaTotal*1024)/0.63)),larguraBanda,video,))])
    listaThread.append([11,threading.Thread(target=execucao,args=(lock, res,arq,'algoritmoLFUcomJanela','AlgoritmoLFUcomJanela',str(1000),int(math.ceil((memoriaTotal*1024)/0.63)),larguraBanda,video,))])
    memoriaTotal+=1 
#import itemgetter, attrgetter
#listaThread=sorted(listaThread, key=itemgetter(0))
listaThread=sorted(listaThread, key=lambda student: student[0])
quantidadeNucleos=4
listaNucleio=[-1,-1,-1,-1]
contador=0
contadorLista=0
while True:
    if(listaNucleio[contador]==-1 or (listaThread[listaNucleio[contador]][1].is_alive==False and contadorLista<len(listaThread))):
        listaNucleio[contador]=contadorLista
        listaThread[listaNucleio[contador]][1].start()
        contadorLista+=1
    elif(contadorLista==len(listaThread) and listaThread[listaNucleio[contador]][1].is_alive==False):
        del listaNucleio[contador]
        if(len(listaNucleio)==0):
            break    
    contador+=1
    if(contador==len(listaNucleio)):
        contador=0

#     print ("Exiting Main Thread")
# #(arquivo,arquivoAgoritmo,classAlgoritmo,argumento,memoriaTotal,larguraBanda,tamanhoVideo):
# #Menu  de dos codicos












