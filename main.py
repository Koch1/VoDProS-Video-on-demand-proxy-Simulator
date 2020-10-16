from manipulacaoArquivo import ManipulacaoArquivo
# from algoritmoAleatorio import AlgortimoAleatorio
# from algoritmoCARTE import AlgortimoCARTE
# from algoritmoCC import AlgoritmoCC
from algoritmoLFU import AlgoritmoLFU
from resultado import Resultado
from cliente import Cliente
from filme import Filme
from printDados import PrintDados
from planilhaODS import PlaniliaOBS
from pacote import Pacote
from geradorGraficos import GeradorGraficos
import time

#Menu  de arquivo fazer

#arquivo contem 4 colunas. (idCleintes,  numero do filme q vai assistir,  tempo de chagada , parte do  video q assistir)
if __name__ == "__main__":
    # Variael do arquivo
    arq='3.txt'
    #alg="algorimo=AlgortimoAleatorio()"
    #alg="algorimo=AlgortimoCARTE(3)"
    #alg="algorimo=AlgortimoCC()"
    alg="algorimo=AlgoritmoLFU()"
    leitura=ManipulacaoArquivo('./baseLeitura/'+str(arq))
    #algorimo=AlgortimoAleatorio()
    print(alg)
    exec(alg)
    #Limite de memoria  em contabilizados em bloco
    memoriaTotal=4500    #Lista q tem infomaçoes da memoria proxy de video
    memoria=[]
    #Tamanho que banda q proxy pode usar  durante aquele intervala de 1 tempo 
    larguraBanda=150
    #filaEspera=[]
    #tempo medido tempo proxy,não funciona na escala tempo real
    instanteTempo=0
    #Isso para inciar com cliente na memoria de leitura
    novoCliente=leitura.novoClienteLido()
    #Contem todos cliente ativos ou em espera. Ele estao em ordem q quem chega primeiro , primeiro receber.
    listaClientes=[]
    #Matriz que  tem infomaçoes do filme e possição da memoria se encontra bloco.  Funciona como Organição de memoria Indexada
    listaFilmes={}
    #Tem os contadores  dentro, é chamada para adcionar erro ou  acertos. 
    result=Resultado(arq,alg)
    #pri=PlaniliaOBS()
    #pri.iniciarPlanilha()
    printDados=PrintDados()
    grafico=GeradorGraficos(arq,alg)
    inicio = time.time()
    while True:
        #Leitura de novo  cliente e veirificação  de colocar na lista
        while (novoCliente!=0 and novoCliente.tempoInicio==instanteTempo):
            result.novoCliente()
            grafico.novoCliente()
            listaClientes.append(novoCliente)
            novoCliente=leitura.novoClienteLido()
        #pri.AdicionarDadosPlanilha(memoria,listaClientes,instanteTempo,result.acertos,result.erros,listaFilmes,memoriaTotal)
        #printDados.intefase3(instanteTempo,result,memoria,memoriaTotal,listaClientes,listaFilmes,algorimo.classificacao)
        #Substituição da parte dos cliente atendendo
        contadorLarguraBanda=0;
        listaEsperaCachebloco={}
        listaEsperaCacheFilme={}
        listaEsperaCacheOrdemChegada=[]
        for cliente in (listaClientes[:]):
            #Remover o cliente q terminou de assistir video da lista
            if(cliente.idBloco==cliente.tamanhoBloco):
                result.terminouCliente()
                grafico.terminouCliente()
                listaClientes.remove(cliente)
            else: 
                memoria=algorimo.organizarMemororia(memoria)
                if(cliente.idFilme in listaFilmes):
                    if((cliente.idBloco+1) in listaFilmes[cliente.idFilme].blocos):
                        cliente.trocaBloco(listaFilmes)
                        memoria[listaFilmes[cliente.idFilme].blocoMemoria[cliente.idBloco]]=([cliente.idFilme,cliente.idBloco,listaFilmes[cliente.idFilme].blocos[cliente.idBloco],algorimo.variavelGenericaMemoriaAcerto(memoria[listaFilmes[cliente.idFilme].blocoMemoria[cliente.idBloco]][3])])
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
        
        tamLista=len(listaEsperaCachebloco)
        listaEsperaCacheblocoOrdenado=(sorted(listaEsperaCachebloco, key=lambda pac: ((((listaEsperaCachebloco[pac].contador*tamLista)+listaEsperaCacheFilme[listaEsperaCachebloco[pac].idFilme])*tamLista)+(tamLista-listaEsperaCachebloco[pac].posicao)),reverse=True))
        #listaEsperaCacheFilmeOrdenado=(sorted(listaEsperaCacheFilme, key=lambda pac: listaEsperaCacheFilme[pac],reverse=True))

        #listaEsperaCacheFilme.sort(reverse=True)
        #print(listaEsperaCacheblocoOrdenado)
        #print(listaEsperaCacheFilmeOrdenado)
        for cliente in listaEsperaCacheOrdemChegada:
            if((str(cliente.idBloco+1)+'-'+str(cliente.idFilme)) in listaEsperaCacheblocoOrdenado[:larguraBanda]):
                result.acerto()
                grafico.acerto()
                if(cliente.idFilme in listaFilmes):
                    if((cliente.idBloco+1) in listaFilmes[cliente.idFilme].blocos):
                        cliente.trocaBloco(listaFilmes)
                        grafico.cachePacote()
                        memoria[listaFilmes[cliente.idFilme].blocoMemoria[cliente.idBloco]]=([cliente.idFilme,cliente.idBloco,listaFilmes[cliente.idFilme].blocos[cliente.idBloco],algorimo.variavelGenericaMemoriaAcerto(memoria[listaFilmes[cliente.idFilme].blocoMemoria[cliente.idBloco]][3])])
                    else:
                        if(memoriaTotal>len(memoria)):
                            cliente.trocaBloco(listaFilmes)
                            listaFilmes[cliente.idFilme].blocoMemoria[cliente.idBloco]=len(memoria)
                            memoria.append([cliente.idFilme,cliente.idBloco,listaFilmes[cliente.idFilme].blocos[cliente.idBloco],algorimo.variavelGenericaMemoriaCriacao()])
                        else:
                            algorimo.substituicaoBlocos(listaFilmes,cliente,memoria,listaClientes,listaEsperaCacheblocoOrdenado[:larguraBanda])
                else:
                    listaFilmes[cliente.idFilme]=Filme(cliente.idFilme)
                    if(memoriaTotal>len(memoria)):
                        #Função dentro do cliente para habilitar o novo pacote de video
                        cliente.trocaBloco(listaFilmes)
                        #Fucão quarda possocição do memoria dentro bloco .  Reduzir tempo de busca em toda memoria
                        listaFilmes[cliente.idFilme].blocoMemoria[cliente.idBloco]=len(memoria)
                        #adiciona na memoria o bloco de video
                        memoria.append([cliente.idFilme,cliente.idBloco,listaFilmes[cliente.idFilme].blocos[cliente.idBloco],algorimo.variavelGenericaMemoriaCriacao()])
                    else:
                        #Função dentro algoritmo de substituicao escolhido
                        algorimo.substituicaoBlocos(listaFilmes,cliente,memoria,listaClientes,listaEsperaCacheblocoOrdenado[:larguraBanda])
            else:
                cliente.idBloco+=1
                result.erro()
                grafico.erro()
                #pri.AdicionarDadosPlanilha(memoria,listaClientes,instanteTempo,result.acertos,result.erros,listaFilmes,memoriaTotal)
                #printDados.intefase3(instanteTempo,result,memoria,memoriaTotal,listaClientes,listaFilmes,algorimo.classificacao)

        #Verficação final para ver se acabou  a distribuição ou  vai ter q contabilidar mais uma tempo
        if(novoCliente==0 and len(listaClientes)==0):
            #print(novoCliente)
            grafico.adiconarTempo(instanteTempo,larguraBanda,tamLista)
            grafico.graficoGerar(memoriaTotal,larguraBanda)
            #leitura.escritaResult(result)
            break
        else:
            grafico.adiconarTempo(instanteTempo,larguraBanda,tamLista)
            instanteTempo=instanteTempo+1
            print(instanteTempo)
            #print("Tempo %i" %instanteTempo)
    # pri.salvarArquivo()
    fim = time.time()
    print(fim - inicio)
#Menu  de dos codicos
