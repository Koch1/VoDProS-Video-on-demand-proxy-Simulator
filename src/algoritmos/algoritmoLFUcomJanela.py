from classes.printDados import PrintDados
from operator import itemgetter, attrgetter
from classes.arvore import Arvore
from classes.no import No
import time

class AlgoritmoLFUcomJanela:
    def __init__(self, jan):
        self.janela=jan
        self.nomeAlgoritmo="LFU com janela de "+str(jan)
    

    def substituicaoBlocos(self,listaFilmes,cliente,memoria,listaClientes,solicitacoes,listaSub,instanteTempo):
        #listaSub=self.calcularTabelaSubituicao(memoria,listaClientes,listaFilmes,solicitacoes)
        #cliente.trocaBloco(listaFilmes,self.janela)
        if(cliente.idBloco==-1):
            listaFilmes[cliente.idFilme].numeroClientes+=1
        else:
            if((listaFilmes[cliente.idFilme].blocos).get(cliente.idBloco)!=None):
                listaFilmes[cliente.idFilme].blocos[cliente.idBloco]-=1
        cliente.idBloco+=1
        if(self.janela>0  and (cliente.idBloco-self.janela)>=0):
            listaFilmes[cliente.idFilme].classificacao[cliente.idBloco-self.janela]-=1
        if((listaFilmes[cliente.idFilme].blocos).get(cliente.idBloco)!=None):
            listaFilmes[cliente.idFilme].blocos[cliente.idBloco]+=1
        else:
            listaFilmes[cliente.idFilme].blocos[cliente.idBloco]=1
        if((listaFilmes[cliente.idFilme].classificacao).get(cliente.idBloco)!=None):
            listaFilmes[cliente.idFilme].classificacao[cliente.idBloco]+=1
        else:
            listaFilmes[cliente.idFilme].classificacao[cliente.idBloco]=1    
        del(listaFilmes[listaSub['idFilme']].blocos[listaSub['idBloco']])
        del(listaFilmes[listaSub['idFilme']].blocoMemoria[listaSub['idBloco']])
        #del(listaFilmes[listaSub['idFilme']].endNos[listaSub['idBloco']])

        listaFilmes[cliente.idFilme].blocoMemoria[cliente.idBloco]=listaSub['memoria']
        memoria[listaSub['memoria']]=[cliente.idFilme,cliente.idBloco,listaFilmes[cliente.idFilme].blocos[cliente.idBloco],(self.variavelGenericaMemoriaCriacao(listaFilmes[cliente.idFilme],memoria,cliente.idBloco))]
        #if(len(listaFilmes[listaSub['idFilme']].endNos[listaSub['idBloco']].blocosChave)>1):
        #   del listaFilmes[listaSub['idFilme']].endNos[listaSub['idBloco']].blocos[listaFilmes[listaSub['idFilme']].endNos[listaSub['idBloco']].blocosChave[str(listaSub['idFilme']+'-'+listaSub['idBloco'])]]
        #   del listaFilmes[listaSub['idFilme']].endNos[listaSub['idBloco']].blocosChave[str(listaFilme.idFilme+'-'+listaSub['idBloco'])]
        #else:
        #    listaFilmes[listaSub['idFilme']].endNos[listaSub['idBloco']].removeNos()
        #    del listaFilmes[listaSub['idFilme']].endNos[listaSub['idBloco']];

    def calcularTabelaSubituicao(self,memoria,listaClientes,listaFilmes,solicitacoes):
        self.classificacao=[]
        for idM, bloco in enumerate(memoria):
            if(((str(bloco[1])+"-"+str(bloco[0])) not in solicitacoes) or len(memoria)<len(solicitacoes)):
                pontuar=0
                # filtered_dictionary = {key: value for key, value in listaFilmes[bloco[0]].clientes.items() if ((self.janela+bloco[1])>value.idBloco and value.idBloco>=bloco[1])}
                for cliente in listaFilmes[bloco[0]].clientes:
                    valor=listaFilmes[bloco[0]].clientes[cliente].idBloco-int(bloco[1])
                    if(valor>-1 and self.janela>valor):
                        pontuar=pontuar+1
                pontoBloco={'idFilme':bloco[0],'idBloco':bloco[1], 'pontuacao':pontuar,'pontuacao2':bloco[3], 'memoria':idM, 'proximoFinal':(bloco[1]-listaFilmes[bloco[0]].tamanhoFilme)}
                self.classificacao.append(pontoBloco)
        self.classificacao=sorted(self.classificacao, key=itemgetter('pontuacao','pontuacao2'))
        return self.classificacao
    def calcularClasificacao(self,idBloco,listaFilme,arvore):
        # Classificar clientes
        inicio2 = time.time()
        
        if((idBloco-self.janela)>=0 and (listaFilme.endNos.get((idBloco-self.janela))!=None)):
            if(listaFilme.blocos.get((idBloco-self.janela))!=None and listaFilme.classificacao[(idBloco-self.janela)]!=listaFilme.endNos[(idBloco-self.janela)].item):
                nodo=No((listaFilme.classificacao[(idBloco-self.janela)]),(idBloco-self.janela),listaFilme.idFilme,listaFilme.blocoMemoria[(idBloco-self.janela)])
                if(len(listaFilme.endNos[(idBloco-self.janela)].blocosChave)>1):             
                    del listaFilme.endNos[(idBloco-self.janela)].blocosChave[str(listaFilme.idFilme)+'-'+str((idBloco-self.janela))]
                    listaFilme.endNos[(idBloco-self.janela)]=arvore.inserir(nodo)
                else:
                    arvore.removeNos(listaFilme.endNos[(idBloco-self.janela)])
                    listaFilme.endNos[(idBloco-self.janela)]=arvore.inserir(nodo)
        if(listaFilme.blocos.get((idBloco))!=None): 
            pontuar=listaFilme.classificacao[idBloco]           
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
        #print("Classificacao :%.2f "%(calculo))
    def calcularClassificao1(self,idBloco,listaFilme,arvore):
        # Classificar clientes
        
        pontuar=0
        for cliente in listaFilme.clientes:   
            valor=listaFilme.clientes[cliente].idBloco
            #calcula pontuação
            if(listaFilme.clientes[cliente].idBloco>=idBloco and listaFilme.clientes[cliente].idBloco<(idBloco+self.janela)):
                pontuar=listaFilme.clientes[cliente].idBloco
            #remover pontuação de bloco fora do tamanho da janela
        if((idBloco-self.janela)>=0 and listaFilme.clientes[cliente].idBloco==(idBloco-self.janela)):
            nodo=No((listaFilme.endNos[(idBloco-self.janela)].item-1),(idBloco-self.janela),listaFilme.idFilme,listaFilme.blocoMemoria[(idBloco-self.janela)])
            if(len(listaFilme.endNos[(idBloco-self.janela)].blocosChave)>1):
                #print("aqui",str(listaFilme.idFilme)+'-'+str((idBloco-self.janela)))
                #print(listaFilme.endNos[(idBloco-self.janela)].blocos)
                #print(listaFilme.endNos[(idBloco-self.janela)].blocosChave)
                valorPosicao=listaFilme.endNos[(idBloco-self.janela)].blocosChave[str(listaFilme.idFilme)+'-'+str((idBloco-self.janela))]
                del listaFilme.endNos[(idBloco-self.janela)].blocos[valorPosicao]
                del listaFilme.endNos[(idBloco-self.janela)].blocosChave[str(listaFilme.idFilme)+'-'+str((idBloco-self.janela))]
                for elemento in listaFilme.endNos[(idBloco-self.janela)].blocosChave:
                    valorVindo=listaFilme.endNos[(idBloco-self.janela)].blocosChave[elemento];
                    if(valorPosicao<valorVindo):
                        listaFilme.endNos[(idBloco-self.janela)].blocosChave[elemento]=valorVindo-1
                listaFilme.endNos[(idBloco-self.janela)]=arvore.inserir(nodo)
            else:
                arvore.removeNos(listaFilme.endNos[(idBloco-self.janela)])
                listaFilme.endNos[(idBloco-self.janela)]=arvore.inserir(nodo)
        if(idBloco in listaFilme.endNos): 
            #print(listaFilme.endNos)
            if(listaFilme.endNos[idBloco].item!=pontuar):
                nodo=No(pontuar,idBloco,listaFilme.idFilme,listaFilme.blocoMemoria[idBloco])
                if(len(listaFilme.endNos[idBloco].blocos)>1):
                    #print(listaFilme.endNos[idBloco].blocosChave)
                    #print(listaFilme.endNos[idBloco].blocos)
                    #print(str(listaFilme.idFilme)+'-'+str(idBloco))
                    valorPosicao=listaFilme.endNos[idBloco].blocosChave[str(listaFilme.idFilme)+'-'+str(idBloco)]
                    del listaFilme.endNos[idBloco].blocos[valorPosicao]
                    del listaFilme.endNos[idBloco].blocosChave[str(listaFilme.idFilme)+'-'+str(idBloco)]
                    for elemento in listaFilme.endNos[idBloco].blocosChave:
                        valorVindo=listaFilme.endNos[idBloco].blocosChave[elemento];
                        if(valorPosicao<valorVindo):
                            listaFilme.endNos[idBloco].blocosChave[elemento]=valorVindo-1
                    listaFilme.endNos[idBloco]=arvore.inserir(nodo)
                else:
                    arvore.removeNos(listaFilme.endNos[idBloco])
                    listaFilme.endNos[idBloco]=arvore.inserir(nodo)
        else:
            nodo=No(pontuar,idBloco,listaFilme.idFilme,listaFilme.blocoMemoria[idBloco])
            listaFilme.endNos[idBloco]=arvore.inserir(nodo)
    
    
    def variavelGenericaMemoriaAcerto(self, valor):
        return valor+1
    def variavelGenericaMemoriaCriacao(self,listaFilme,memoria,idBloco):
        return 1
    def organizarMemororia(self,memoria):
        return memoria;
    
    def alterarClassificar(self,argumento,listaFilmes,cliente,instanteTempo):
        if(argumento>0  and (cliente.idBloco-argumento)>=0):
            listaFilmes[cliente.idFilme].classificacao[cliente.idBloco-argumento]-=1
        if(listaFilmes[cliente.idFilme].classificacao.get(cliente.idBloco)!=None):
            listaFilmes[cliente.idFilme].classificacao[cliente.idBloco]+=1
        else:
            listaFilmes[cliente.idFilme].classificacao[cliente.idBloco]=1
            
    def saidaCliente(self,argumento,listaFilme,cliente,arvore,log,memoria):
            contado=0
            while(contado<argumento):
                if(listaFilme.classificacao[(cliente.idBloco-contado)]>0):
                    listaFilme.classificacao[(cliente.idBloco-contado)]-=1
                if((listaFilme.blocos).get((cliente.idBloco-contado))!=None):
                    pontuar=listaFilme.classificacao[(cliente.idBloco-contado)]        
                    if(listaFilme.endNos[(cliente.idBloco-contado)].item!=pontuar):
                        nodo=No(pontuar,(cliente.idBloco-contado),listaFilme.idFilme,listaFilme.blocoMemoria[(cliente.idBloco-contado)])
                        if(len(listaFilme.endNos[(cliente.idBloco-contado)].blocosChave)>1):
                            del listaFilme.endNos[(cliente.idBloco-contado)].blocosChave[str(listaFilme.idFilme)+'-'+str((cliente.idBloco-contado))]
                            listaFilme.endNos[(cliente.idBloco-contado)]=arvore.inserir(nodo)
                        else:
                            arvore.removeNos(listaFilme.endNos[(cliente.idBloco-contado)])
                            listaFilme.endNos[(cliente.idBloco-contado)]=arvore.inserir(nodo)
                contado+=1
