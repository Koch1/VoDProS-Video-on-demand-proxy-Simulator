# -*- coding: utf-8 -*-
from manipulacaoArquivo import ManipulacaoArquivo
# from algoritmoAleatorio import AlgortimoAleatorio
##from algoritmoCARTE import AlgortimoCARTE
# from algoritmoCC import AlgoritmoCC
#from algoritmoLRU import AlgoritmoLRU
#from algoritmoLFU import AlgoritmoLFU
from resultado import Resultado
from cliente import Cliente
from filme import Filme
from printDados import PrintDados
from planilhaODS import PlaniliaOBS
from pacote import Pacote
from geradorGraficos import GeradorGraficos
import time

def execucao(arquivo,arquivoAgoritmo,classAlgoritmo,argumento,memoriaTotal,larguraBanda,tamanhoVideo):
    
    #alg="algorimo=AlgortimoAleatorio()"
    #alg="algorimo=AlgortimoCC()"
    #alg="algorimo=AlgoritmoLFU()"
    #alg="algorimo=AlgoritmoLRU()"
    leitura=ManipulacaoArquivo('./baseLeitura/'+str(arquivo))
    #algorimo=AlgortimoAleatorio()
    print(str("from algoritmo."+arquivoAgoritmo+" import "+classAlgoritmo))
    print((str("algoritmo="+classAlgoritmo+"("+argumento+")")))
    
    #from algoritmo.algoritmoLRU import AlgoritmoLRU
    impor=str("from algoritmo."+arquivoAgoritmo+" import "+classAlgoritmo)
    exec(impor,globals()) 
    comand=str("algoritmo="+classAlgoritmo+"("+argumento+")")
    exec(comand,globals())
    #Lista q tem infomaçoes da memoria proxy de video
    memoria=[]

    #filaEspera=[]
    #tempo medido tempo proxy,não funciona na escala tempo real
    instanteTempo=0
    #Isso para inciar com cliente na memoria de leitura
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
    grafico=GeradorGraficos(arquivo,algoritmo.nomeAlgoritmo,memoriaTotal,larguraBanda)
    inicio = time.time()
    while True:
        #print(alg)
        #Leitura de novo  cliente e veirificação  de colocar na lista
        inicioTempo = time.time()
        inicio2 = time.time()
        while (novoCliente!=0 and novoCliente.tempoInicio==instanteTempo):
            result.novoCliente()
            grafico.novoCliente()
            listaClientes.append(novoCliente)
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
        for cliente in (listaClientes[:]):
            #Remover o cliente q terminou de assistir video da lista
            if(cliente.idBloco==cliente.tamanhoBloco):
                result.terminouCliente()
                grafico.terminouCliente()
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
        grafico.tempoDistribucaoNaCahcheDef(calculo)
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
        grafico.tempoGerarTabelaTubstituicaoDef(calculo)
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
                                grafico.tempoGerarTabelaTubstituicaoDef(calculo)
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
                            grafico.tempoGerarTabelaTubstituicaoDef(calculo)
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
            grafico.salvarDados(calculo,instanteTempo)
            grafico.graficoGerar(memoriaTotal,larguraBanda)
            #leitura.escritaResult(result)
            break
        else:
            fim = time.time()
            calculo=fim - inicioTempo
            grafico.tempoCicloDef(calculo)
            grafico.adiconarTempo(instanteTempo,larguraBanda,tamLista)
            instanteTempo=instanteTempo+1
            #print(instanteTempo)
            
            print("Tempo do Ciclo %i :%.2f" %(instanteTempo,calculo))
    # pri.salvarArquivo()



#Menu  de arquivo fazer

#arquivo contem 4 colunas. (idCleintes,  numero do filme q vai assistir,  tempo de chagada , parte do  video q assistir)
if __name__ == "__main__":
    # Variael do arquivo
        #Limite de memoria  em contabilizados em bloco
    memoriaTotal=22756
        #Tamanho que banda q proxy pode usar  durante aquele intervala de 1 tempo
    arq='3.txt' 
    larguraBanda=700
    video=5400
    execucao(arq,'algoritmoCC','AlgoritmoCC','',memoriaTotal,larguraBanda,video)
    execucao(arq,'algoritmoLRU','AlgoritmoLRU','',memoriaTotal,larguraBanda,video)
    execucao(arq,'algoritmoLFU','AlgoritmoLFU','',memoriaTotal,larguraBanda,video) 
    execucao(arq,'algoritmoCARTE','AlgoritmoCARTE','85',memoriaTotal,larguraBanda,video) 
    #(arquivo,arquivoAgoritmo,classAlgoritmo,argumento,memoriaTotal,larguraBanda,tamanhoVideo):
#Menu  de dos codicos
