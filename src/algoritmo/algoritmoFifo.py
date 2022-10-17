from clas.printDados import PrintDados
from operator import itemgetter, attrgetter
from clas.arvore import Arvore
from clas.no import No
import time

class AlgoritmoFIFO:
    def __init__(self,jan):
        self.classificacao=[]
        self.valorMaior=0
        self.nomeAlgoritmo="FIFO"
        
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
        self.valorMaior+=1
        listaFilme.classificacao[idBloco]=self.valorMaior
        return self.valorMaior
    def calcularClasificacao(self,idBloco,listaFilme,arvore):
        # Classificar clientes
        inicio2 = time.time()
        if(listaFilme.blocos.get((idBloco))!=None):
            pontuar=listaFilme.classificacao[idBloco]
            if(listaFilme.endNos.get(idBloco)==None): 
                nodo=No(pontuar,idBloco,listaFilme.idFilme,listaFilme.blocoMemoria[idBloco])
                listaFilme.endNos[idBloco]=arvore.inserir(nodo)
        fim2 = time.time()
        calculo=fim2 - inicio2
    

    def alterarClassificar(self,argumento,listaFilmes,cliente,instanteTempo):
        a=0

    def saidaCliente(self,argumento,listaFilme,cliente,arvore,log,memoria):
        a=0