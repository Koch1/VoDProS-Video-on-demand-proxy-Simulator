from classes.printDados import PrintDados
from operator import itemgetter, attrgetter
from classes.arvore import Arvore
from classes.no import No
import time

class AlgoritmoCarte:
    def __init__(self, jan):
        self.janela=jan
        self.nomeAlgoritmo="Carte com janela de "+str(jan)
    
    def substituicaoBlocos(self,listaFilmes,cliente,memoria,listaClientes,solicitacoes,listaSub,instanteTempo):
        #listaSub=self.calcularTabelaSubituicao(memoria,listaClientes,listaFilmes,solicitacoes)
        #cliente.trocaBloco(listaFilmes,self.janela)
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
        self.alterarClassificar(self.janela,listaFilmes,cliente,instanteTempo)
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

    def calcularClasificacao(self,idBloco,listaFilme,arvore):
        # Classificar clientes
        inicio2 = time.time()
        
        if((idBloco+self.janela)<5527 and (listaFilme.endNos.get((idBloco+self.janela))!=None)):
            if(listaFilme.blocos.get((idBloco+self.janela))!=None and listaFilme.classificacao[(idBloco+self.janela)]!=listaFilme.endNos[(idBloco+self.janela)].item):
                nodo=No((listaFilme.classificacao[(idBloco+self.janela)]),(idBloco+self.janela),listaFilme.idFilme,listaFilme.blocoMemoria[(idBloco+self.janela)])
                if(len(listaFilme.endNos[(idBloco+self.janela)].blocosChave)>1):             
                    del listaFilme.endNos[(idBloco+self.janela)].blocosChave[str(listaFilme.idFilme)+'-'+str((idBloco+self.janela))]
                    listaFilme.endNos[(idBloco+self.janela)]=arvore.inserir(nodo)
                else:
                    arvore.removeNos(listaFilme.endNos[(idBloco+self.janela)])
                    listaFilme.endNos[(idBloco+self.janela)]=arvore.inserir(nodo)
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
        # idBloco=idBloco-1            
        # if(listaFilme.blocos.get((idBloco))!=None): 
        #     pontuar=listaFilme.classificacao[idBloco]           
        #     if(listaFilme.endNos.get(idBloco)!=None):
        #         if(listaFilme.endNos[idBloco].item!=pontuar):
        #             nodo=No(pontuar,idBloco,listaFilme.idFilme,listaFilme.blocoMemoria[idBloco])
        #             if(len(listaFilme.endNos[idBloco].blocosChave)>1):
        #                 del listaFilme.endNos[idBloco].blocosChave[str(listaFilme.idFilme)+'-'+str(idBloco)]
        #                 listaFilme.endNos[idBloco]=arvore.inserir(nodo)
        #             else:
        #                 arvore.removeNos(listaFilme.endNos[idBloco])  
        #                 listaFilme.endNos[idBloco]=arvore.inserir(nodo)
        #     else:
        #         nodo=No(pontuar,idBloco,listaFilme.idFilme,listaFilme.blocoMemoria[idBloco])
        #         listaFilme.endNos[idBloco]=arvore.inserir(nodo)
            
        fim2 = time.time()
        calculo=fim2 - inicio2
        #print("Classificacao :%.2f "%(calculo))
    
    def variavelGenericaMemoriaAcerto(self, valor):
        return valor+1
    def variavelGenericaMemoriaCriacao(self,listaFilme,memoria,idBloco):
        return 1
    def organizarMemororia(self,memoria):
        return memoria;
    
    def alterarClassificar(self,argumento,listaFilmes,cliente,instanteTempo):
        if(cliente.idBloco==0):
            contBloco=0;
            while (contBloco<=argumento):
                if((listaFilmes[cliente.idFilme].classificacao).get(contBloco)!=None):
                    listaFilmes[cliente.idFilme].classificacao[contBloco]+=1
                else:
                    listaFilmes[cliente.idFilme].classificacao[contBloco]=1
                contBloco+=1
            listaFilmes[cliente.idFilme].classificacao[(cliente.idBloco)]-=1
        else:
            if(argumento>0  and (cliente.idBloco)!=0):
                listaFilmes[cliente.idFilme].classificacao[(cliente.idBloco)]-=1
            if((cliente.idBloco+argumento)<cliente.tamanhoBloco):
                if(listaFilmes[cliente.idFilme].classificacao.get(cliente.idBloco+argumento)!=None):
                    listaFilmes[cliente.idFilme].classificacao[cliente.idBloco+argumento]+=1
                else:
                    listaFilmes[cliente.idFilme].classificacao[cliente.idBloco+argumento]=1            
    def saidaCliente(self,argumento,listaFilme,cliente,arvore,log,memoria):
            contado=0
            # if(listaFilme.classificacao[(cliente.idBloco)]>0):
            #     listaFilme.classificacao[(cliente.idBloco)]-=1
            # if((listaFilme.blocos).get((cliente.idBloco))!=None):
            #     pontuar=listaFilme.classificacao[(cliente.idBloco)]        
            #     if(listaFilme.endNos[(cliente.idBloco)].item!=pontuar):
            #         nodo=No(pontuar,(cliente.idBloco),listaFilme.idFilme,listaFilme.blocoMemoria[(cliente.idBloco)])
            #         if(len(listaFilme.endNos[(cliente.idBloco-contado)].blocosChave)>1):
            #             del listaFilme.endNos[(cliente.idBloco)].blocosChave[str(listaFilme.idFilme)+'-'+str((cliente.idBloco))]
            #             listaFilme.endNos[(cliente.idBloco)]=arvore.inserir(nodo)
            #         else:
            #             arvore.removeNos(listaFilme.endNos[(cliente.idBloco)])
            #             listaFilme.endNos[(cliente.idBloco)]=arvore.inserir(nodo)
