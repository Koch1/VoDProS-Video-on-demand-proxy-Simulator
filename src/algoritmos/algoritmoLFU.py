from classes.printDados import PrintDados
from operator import itemgetter, attrgetter
from classes.arvore import Arvore
from classes.no import No
import time
class AlgoritmoLFU:
    def __init__(self,jan):
        self.nomeAlgoritmo="LFU"
        self.classificacao=[]

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
        if(listaFilmes[cliente.idFilme].classificacao.get(cliente.idBloco)!=None):
            listaFilmes[cliente.idFilme].classificacao[cliente.idBloco]+=1
        else:
            listaFilmes[cliente.idFilme].classificacao[cliente.idBloco]=1
        listaFilmes[listaSub['idFilme']].classificacao[listaSub['idBloco']]=0
        del(listaFilmes[listaSub['idFilme']].blocos[listaSub['idBloco']])
        del(listaFilmes[listaSub['idFilme']].blocoMemoria[listaSub['idBloco']])
        listaFilmes[cliente.idFilme].blocoMemoria[cliente.idBloco]=listaSub['memoria']
        memoria[listaSub['memoria']]=[cliente.idFilme,cliente.idBloco,listaFilmes[cliente.idFilme].blocos[cliente.idBloco],(self.variavelGenericaMemoriaCriacao(listaFilmes[cliente.idFilme],memoria,cliente.idBloco))]

    def calcularClasificacao(self,idBloco,listaFilme,arvore):
        # Classificar clientes
        inicio2 = time.time()
        pontuar=listaFilme.classificacao[idBloco]
        #arvore.inOrderLog(arvore.root,log)
        #log.escreverVerificar('classificando01')
        if(listaFilme.blocos.get((idBloco))!=None):
            if(listaFilme.endNos.get(idBloco)!=None):
                #log.escreverVerificar('classificando02') 
                if(listaFilme.endNos[idBloco].item!=pontuar):
                    #log.escreverVerificar('classificando03') 
                    nodo=No(pontuar,idBloco,listaFilme.idFilme,listaFilme.blocoMemoria[idBloco])
                    #log.escreverVerificar(listaFilme.endNos[idBloco].blocosChave)
                    if(len(listaFilme.endNos[idBloco].blocosChave)>1):
                        del listaFilme.endNos[idBloco].blocosChave[str(listaFilme.idFilme)+'-'+str(idBloco)]
                        listaFilme.endNos[idBloco]=arvore.inserir(nodo)
                        #arvore.inOrderLog(arvore.root,log)
                    else:
                        #log.escreverVerificar("tempo="+str(listaFilme.endNos[idBloco].item)+"--"+str(len(listaFilme.endNos[idBloco].blocosChave)))
                        #log.escreverVerificar('classificando05')
                        arvore.removeNos(listaFilme.endNos[idBloco])
                        #log.escreverVerificar(nodo)
                        #arvore.inOrderLog(arvore.root,log)    
                        listaFilme.endNos[idBloco]=arvore.inserir(nodo)
            else:
                #log.escreverVerificar('classificando06') 
                nodo=No(pontuar,idBloco,listaFilme.idFilme,listaFilme.blocoMemoria[idBloco])
                #log.escreverVerificar(nodo)
                listaFilme.endNos[idBloco]=arvore.inserir(nodo)
                #arvore.inOrderLog(arvore.root,log)
        fim2 = time.time()
        calculo=fim2 - inicio2

    def calcularTabelaSubituicao(self,memoria,listaClientes,listaFilmes,solicitacoes):
        for idM, bloco in enumerate(memoria):
            if(((str(bloco[1])+"-"+str(bloco[0])) not in solicitacoes) or len(memoria)<len(solicitacoes)):
                pontoBloco={'idFilme':bloco[0],'idBloco':bloco[1], 'pontuacao':bloco[3], 'memoria':idM}
                self.classificacao.append(pontoBloco)
            # sorted ordena do menor para maior,  caso coloque mais um paretro reverse=True ele inverte
        self.classificacao=sorted(self.classificacao, key=itemgetter('pontuacao'))
        return self.classificacao

    
    def variavelGenericaMemoriaAcerto(self, valor):
        return valor+1
    def variavelGenericaMemoriaCriacao(self,listaFilme,memoria,idBloco):
        return 1
    def organizarMemororia(self,memoria):
        return memoria;
    def alterarClassificar(self,argumento,listaFilmes,cliente,instanteTempo):
        if(listaFilmes[cliente.idFilme].classificacao.get(cliente.idBloco)!=None):
            listaFilmes[cliente.idFilme].classificacao[cliente.idBloco]+=1
        else:
            listaFilmes[cliente.idFilme].classificacao[cliente.idBloco]=1
            
    def saidaCliente(self,argumento,listaFilme,cliente,arvore,log,memoria):
        a=0        
