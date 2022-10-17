from clas.printDados import PrintDados
from operator import itemgetter, attrgetter
from clas.arvore import Arvore
from clas.no import No
import time


class AlgoritmoLRU:
    def __init__(self,jan):
        self.valorMaior=0
        self.nomeAlgoritmo="LRU"
        
    # def substituicaoBlocos(self,listaFilmes,cliente,memoria,listaClientes,solicitacoes,listaSub):
    #     #listaSub=self.calcularTabelaSubituicao(memoria,listaClientes,listaFilmes,solicitacoes)
    #     cliente.trocaBloco(listaFilmes)
    #     listaFilmes[listaSub['idFilme']].classificacao[listaSub['idBloco']]=0
    #     del(listaFilmes[listaSub['idFilme']].blocos[listaSub['idBloco']])
    #     del(listaFilmes[listaSub['idFilme']].blocoMemoria[listaSub['idBloco']])
    #     listaFilmes[cliente.idFilme].blocoMemoria[cliente.idBloco]=listaSub['memoria']
    #     memoria[listaSub['memoria']]=[cliente.idFilme,cliente.idBloco,listaFilmes[cliente.idFilme].blocos[cliente.idBloco],self.variavelGenericaMemoriaCriacao()]

    def substituicaoBlocos(self,listaFilmes,cliente,memoria,listaClientes,solicitacoes,listaSub,instanteTempo):
        #listaSub=self.calcularTabelaSubituicao(memoria,listaClientes,listaFilmes,solicitacoes)
        #cliente.trocaBloco(listaFilmes)
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
        self.valorMaior+=1
        listaFilmes[cliente.idFilme].classificacao[cliente.idBloco]=self.valorMaior
        del(listaFilmes[listaSub['idFilme']].blocos[listaSub['idBloco']])
        del(listaFilmes[listaSub['idFilme']].blocoMemoria[listaSub['idBloco']])
        listaFilmes[cliente.idFilme].blocoMemoria[cliente.idBloco]=listaSub['memoria']
        memoria[listaSub['memoria']]=[cliente.idFilme,cliente.idBloco,listaFilmes[cliente.idFilme].blocos[cliente.idBloco],self.valorMaior]







    def calcularTabelaSubituicao(self,memoria,listaClientes,listaFilmes,solicitacoes):
        self.classificacao=[]
        for idM, bloco in enumerate(memoria):
            if(((str(bloco[1])+"-"+str(bloco[0])) not in solicitacoes) or len(memoria)<len(solicitacoes)):
                pontoBloco={'idFilme':bloco[0],'idBloco':bloco[1], 'pontuacao':bloco[3], 'memoria':idM, 'proximoFinal':(bloco[1]-listaFilmes[bloco[0]].tamanhoFilme)}
                self.classificacao.append(pontoBloco)
        self.classificacao=sorted(self.classificacao, key=itemgetter('pontuacao'))
        return self.classificacao
    

    def calcularClasificacao(self,idBloco,listaFilme,arvore):
        # Classificar clientes
        inicio2 = time.time()
        pontuar=listaFilme.classificacao[idBloco]
        if(listaFilme.blocos.get((idBloco))!=None):
            if(listaFilme.endNos.get(idBloco)!=None): 
                if(listaFilme.endNos[idBloco].item!=pontuar):
                    nodo=No(pontuar,idBloco,listaFilme.idFilme,listaFilme.blocoMemoria[idBloco])
                    if(len(listaFilme.endNos[idBloco].blocosChave)>1):
                        del listaFilme.endNos[idBloco].blocosChave[str(listaFilme.idFilme)+'-'+str(idBloco)]
                        listaFilme.endNos[idBloco]=arvore.inserir(nodo)
                    else:
                        arvore.removeNos(listaFilme.endNos[idBloco])  
                        listaFilme.endNos[idBloco]=arvore.inserir(nodo)
            else:
                nodo=No(pontuar,idBloco,listaFilme.idFilme,listaFilme.blocoMemoria[idBloco])
                listaFilme.endNos[idBloco]=arvore.inserir(nodo)
        fim2 = time.time()
        calculo=fim2 - inicio2
        
    
    def calcularTabelaSubituicaoComThread(self,memoria,listaClientes,listaFilmes,solicitacoes):
        self.classificacao=[]
        threads = list()
        cont=0
        while (cont<(len(memoria)/1000)):
            inicio=(cont*1000)
            fim=((cont+1)*1000)
            if(fim>len(memoria)):
                fim=len(memoria)
            parteMemoria=memoria[inicio:fim]
            x = threading.Thread(target=self.calcularTabelaSubituicaoFuncaoParaThread, args=(parteMemoria,self.classificacao,listaClientes,listaFilmes,solicitacoes,))
            threads.append(x)
            x.start()
            cont=cont+1
        for index, thread in enumerate(threads):
            thread.join()
        self.classificacao=sorted(self.classificacao, key=itemgetter('pontuacao'))
        return self.classificacao    
    
        
    def calcularTabelaSubituicaoFuncaoParaThread(self,memoria,classificacao,listaClientes,listaFilmes,solicitacoes):
        for idM, bloco in enumerate(memoria):
            if(((str(bloco[1])+"-"+str(bloco[0])) not in solicitacoes) or len(memoria)<len(solicitacoes)):
                pontoBloco={'idFilme':bloco[0],'idBloco':bloco[1], 'pontuacao':bloco[3], 'memoria':idM, 'proximoFinal':(bloco[1]-listaFilmes[bloco[0]].tamanhoFilme)}
                self.classificacao.append(pontoBloco)
        

    def variavelGenericaMemoriaAcerto(self, valor):
        return self.valorMaior
    

    def variavelGenericaMemoriaCriacao(self,listaFilme,memoria,idBloco):
        return self.valorMaior

    def organizarMemororia(self,memoria):
        # novaMemoria=[]
        # for bloco in memoria:
        #     novaMemoria.append([bloco[0],bloco[1],bloco[2],(bloco[3]+1)])
        return memoria;
    

    def alterarClassificar(self,argumento,listaFilmes,cliente,instanteTempo):
        self.valorMaior+=1
        listaFilmes[cliente.idFilme].classificacao[cliente.idBloco]=self.valorMaior

    def saidaCliente(self,argumento,listaFilme,cliente,arvore,log,memoria):
        a=0