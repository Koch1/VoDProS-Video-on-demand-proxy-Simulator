from clas.printDados import PrintDados
from operator import itemgetter, attrgetter
import random 
from clas.arvore import Arvore
from clas.no import No
import time


class AlgoritmoRandon:
    def __init__(self,jan):
        self.classificacao=[]
        self.valorMaior=0
        self.nomeAlgoritmo="Randon"
        
    def substituicaoBlocos(self,listaFilmes,cliente,memoria,listaClientes,solicitacoes,listaSub,instanteTempo):
        #listaSub=self.calcularTabelaSubituicao(memoria,listaClientes,listaFilmes,solicitacoes)

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

        del(listaFilmes[listaSub['idFilme']].blocos[listaSub['idBloco']])
        del(listaFilmes[listaSub['idFilme']].blocoMemoria[listaSub['idBloco']])
        listaFilmes[cliente.idFilme].blocoMemoria[cliente.idBloco]=listaSub['memoria']
        memoria[listaSub['memoria']]=[cliente.idFilme,cliente.idBloco,listaFilmes[cliente.idFilme].blocos[cliente.idBloco],self.variavelGenericaMemoriaCriacao(listaFilmes[cliente.idFilme],memoria,cliente.idBloco)]

    def variavelGenericaMemoriaAcerto(self, valor):
        #self.valorMaior+=1
        return valor
    def variavelGenericaMemoriaCriacao(self,listaFilme,memoria,idBloco):
        if(isinstance(memoria, list)):
            r1 = random.randint(0, (len(memoria)-1))
        else:
            r1 = random.randint(0,(memoria-1))
        listaFilme.classificacao[idBloco]=r1
        return r1
    def calcularClasificacao(self,idBloco,listaFilme,arvore):
        # Classificar clientes
        inicio2 = time.time()
        
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
    

    def alterarClassificar(self,argumento,listaFilmes,cliente,instanteTempo):
        a=0

    def saidaCliente(self,argumento,listaFilme,cliente,arvore,log,memoria):
        a=0        
        
