from classes.printDados import PrintDados
from operator import itemgetter, attrgetter
from classes.arvore import Arvore
from classes.no import No
import time


class AlgoritmoLRUcomJanela:
    def __init__(self, jan):
        self.janela=jan
        self.valorMaior=0
        self.nomeAlgoritmo="LRU com janela de "+str(jan)
    def substituicaoBlocos(self,listaFilmes,cliente,memoria,listaClientes,solicitacoes,listaSub,instanteTempo):        
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
        tamanhoJanela=self.janela
        blocoParaPontuar=cliente.idBloco
        while(0<=blocoParaPontuar and blocoParaPontuar>=(cliente.idBloco-self.janela)):
            if(listaFilmes[cliente.idFilme].classificacao.get(cliente.idBloco)==None or listaFilmes[cliente.idFilme].classificacao[blocoParaPontuar]<tamanhoJanela or listaFilmes[cliente.idFilme].tempoClassificacao[blocoParaPontuar]<instanteTempo):
                listaFilmes[cliente.idFilme].classificacao[blocoParaPontuar]=tamanhoJanela
                listaFilmes[cliente.idFilme].tempoClassificacao[blocoParaPontuar]=instanteTempo
            if(listaFilmes[cliente.idFilme].blocos.get((blocoParaPontuar-1))!=None and listaFilmes[cliente.idFilme].blocos[(blocoParaPontuar-1)]>0):
                break
            tamanhoJanela-=1;  
            blocoParaPontuar-=1     
        del(listaFilmes[listaSub['idFilme']].blocos[listaSub['idBloco']])
        del(listaFilmes[listaSub['idFilme']].blocoMemoria[listaSub['idBloco']])
        #del(listaFilmes[listaSub['idFilme']].endNos[listaSub['idBloco']])

        listaFilmes[cliente.idFilme].blocoMemoria[cliente.idBloco]=listaSub['memoria']
        memoria[listaSub['memoria']]=[cliente.idFilme,cliente.idBloco,listaFilmes[cliente.idFilme].blocos[cliente.idBloco],(self.variavelGenericaMemoriaCriacao(listaFilmes[cliente.idFilme],memoria,cliente.idBloco))]
        
        
        
    def calcularClasificacao(self,idBloco,listaFilme,arvore):
            # Classificar clientes
        inicio2 = time.time()
        blocoParaPontuar=idBloco
        
        while(0<=blocoParaPontuar and blocoParaPontuar>=(idBloco-self.janela)):
    
            pontuar=listaFilme.classificacao[blocoParaPontuar]
            if(listaFilme.blocos.get((blocoParaPontuar))!=None):
                if((listaFilme.endNos.get(blocoParaPontuar)!=None)):
                    if(listaFilme.endNos[blocoParaPontuar].item!=pontuar):
                        nodo=No((listaFilme.classificacao[blocoParaPontuar]),(blocoParaPontuar),listaFilme.idFilme,listaFilme.blocoMemoria[blocoParaPontuar])
                        if(len(listaFilme.endNos[blocoParaPontuar].blocosChave)>1):             
                            del listaFilme.endNos[blocoParaPontuar].blocosChave[str(listaFilme.idFilme)+'-'+str(blocoParaPontuar)]
                            listaFilme.endNos[blocoParaPontuar]=arvore.inserir(nodo)
                        else:
                            arvore.removeNos(listaFilme.endNos[blocoParaPontuar])
                            listaFilme.endNos[blocoParaPontuar]=arvore.inserir(nodo)
                else:
                    #print(pontuar,idBloco,listaFilme.idFilme)
                    nodo=No(pontuar,idBloco,listaFilme.idFilme,listaFilme.blocoMemoria[idBloco])
                    listaFilme.endNos[idBloco]=arvore.inserir(nodo)
            if(listaFilme.blocos.get((blocoParaPontuar-1))!=None and listaFilme.blocos[(blocoParaPontuar-1)]>0):
                break
            blocoParaPontuar-=1 
            
        fim2 = time.time()
        calculo=fim2 - inicio2
        #print("Classificacao :%.2f "%(calculo))



    def calcularTabelaSubituicao(self,memoria,listaClientes,listaFilmes,solicitacoes):
        self.classificacao=[]
        for idM, bloco in enumerate(memoria):
            if(((str(bloco[1])+"-"+str(bloco[0])) not in solicitacoes) or len(memoria)<len(solicitacoes)):
                pontuar=0
                #print(listaFilmes[bloco[0]].clientes)
                #filtered_dictionary = {key: value for key, value in listaFilmes[bloco[0]].clientes.items() if ((self.janela+bloco[1])>value.idBloco and value.idBloco>=bloco[1])}
                for cliente in listaFilmes[bloco[0]].clientes:
                    valor=listaFilmes[bloco[0]].clientes[cliente].idBloco-bloco[1]
                    if(valor>-1 and self.janela>valor and pontuar<((self.janela)-valor)):
                        pontuar=((self.janela)-valor) 
                pontoBloco={'idFilme':bloco[0],'idBloco':bloco[1], 'pontuacao':pontuar,'pontuacao2':bloco[3], 'memoria':idM, 'proximoFinal':(bloco[1]-listaFilmes[bloco[0]].tamanhoFilme)}
                self.classificacao.append(pontoBloco)
        self.classificacao=sorted(self.classificacao, key=itemgetter('pontuacao','pontuacao2'))
        return self.classificacao

    def variavelGenericaMemoriaAcerto(self, valor):
        return self.valorMaior+1

    def variavelGenericaMemoriaCriacao(self,listaFilme,memoria,idBloco):
        return self.valorMaior+1

    def organizarMemororia(self,memoria):
        # novaMemoria=[]
        # for bloco in memoria:
        #     novaMemoria.append([bloco[0],bloco[1],bloco[2],(bloco[3]+1)])
        return memoria;

    def alterarClassificar(self,argumento,listaFilmes,cliente,instanteTempo):
        # Classificar clientes
        tamanhoJanela=self.janela
        blocoParaPontuar=cliente.idBloco
        while(0<=blocoParaPontuar and blocoParaPontuar>=(cliente.idBloco-self.janela)):

            if(listaFilmes[cliente.idFilme].classificacao.get(blocoParaPontuar)==None or  listaFilmes[cliente.idFilme].classificacao[blocoParaPontuar]<tamanhoJanela or  listaFilmes[cliente.idFilme].tempoClassificacao[blocoParaPontuar]<instanteTempo):
                listaFilmes[cliente.idFilme].classificacao[blocoParaPontuar]=tamanhoJanela
                listaFilmes[cliente.idFilme].tempoClassificacao[blocoParaPontuar]=instanteTempo
            if(listaFilmes[cliente.idFilme].blocos.get((blocoParaPontuar-1))!=None and listaFilmes[cliente.idFilme].blocos[blocoParaPontuar-1]>0):
                break
            tamanhoJanela-=1;  
            blocoParaPontuar-=1 
    
    def saidaCliente(self,argumento,listaFilme,cliente,arvore,log,memoria):
            contado=0
            while(contado<argumento):
                if(listaFilme.classificacao[(cliente.idBloco-contado)]>0):
                    listaFilme.classificacao[(cliente.idBloco-contado)]=0
                pontuar=listaFilme.classificacao[(cliente.idBloco-contado)]    
                if(listaFilme.endNos.get((cliente.idBloco-contado))!=None and listaFilme.endNos.get((cliente.idBloco-contado))!=None and listaFilme.endNos[(cliente.idBloco-contado)].item!=pontuar):
                    nodo=No((listaFilme.classificacao[(cliente.idBloco-contado)]),((cliente.idBloco-contado)),listaFilme.idFilme,listaFilme.blocoMemoria[(cliente.idBloco-contado)])
                    if(len(listaFilme.endNos[(cliente.idBloco-contado)].blocosChave)>1):             
                        del listaFilme.endNos[(cliente.idBloco-contado)].blocosChave[str(listaFilme.idFilme)+'-'+str((cliente.idBloco-contado))]
                        listaFilme.endNos[(cliente.idBloco-contado)]=arvore.inserir(nodo)
                    else:
                        arvore.removeNos(listaFilme.endNos[(cliente.idBloco-contado)])
                        listaFilme.endNos[(cliente.idBloco-contado)]=arvore.inserir(nodo)
                if(listaFilme.blocos.get(((cliente.idBloco-contado)-1))!=None and listaFilme.blocos[((cliente.idBloco-contado)-1)]>0):
                    break
                contado+=1
