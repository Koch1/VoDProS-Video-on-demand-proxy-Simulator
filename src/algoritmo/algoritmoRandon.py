from printDados import PrintDados
from operator import itemgetter, attrgetter
import random 

class AlgoritmoRandon:
    def __init__(self):
        self.classificacao=[]
        self.valorMaior=0
        self.nomeAlgoritmo="Randon"
        
    def substituicaoBlocos(self,listaFilmes,cliente,memoria,listaClientes,solicitacoes,listaSub):
        #listaSub=self.calcularTabelaSubituicao(memoria,listaClientes,listaFilmes,solicitacoes)
        # cliente.trocaBloco(listaFilmes)
        # del(listaFilmes[listaSub['idFilme']].blocos[listaSub['idBloco']])
        # del(listaFilmes[listaSub['idFilme']].blocoMemoria[listaSub['idBloco']])
        # listaFilmes[cliente.idFilme].blocoMemoria[cliente.idBloco]=listaSub['memoria']
        # memoria[listaSub['memoria']]=[cliente.idFilme,cliente.idBloco,listaFilmes[cliente.idFilme].blocos[cliente.idBloco],self.variavelGenericaMemoriaCriacao()]
        r1 = random.randint(0, (len(memoria)-1))
        cliente.trocaBloco(listaFilmes)
        del(listaFilmes[memoria[r1][0]].blocos[memoria[r1][1]])
        del(listaFilmes[memoria[r1][0]].blocoMemoria[memoria[r1][1]])
        listaFilmes[cliente.idFilme].blocoMemoria[cliente.idBloco]=r1
        memoria[r1]=[cliente.idFilme,cliente.idBloco,listaFilmes[cliente.idFilme].blocos[cliente.idBloco],self.variavelGenericaMemoriaCriacao()]


    def calcularTabelaSubituicao(self,memoria,listaClientes,listaFilmes,solicitacoes):
        self.classificacao=[]
        for idM, bloco in enumerate(memoria):
            if(((str(bloco[1])+"-"+str(bloco[0])) not in solicitacoes) or len(memoria)<len(solicitacoes)):
                pontoBloco={'idFilme':bloco[0],'idBloco':bloco[1], 'pontuacao':bloco[3], 'memoria':idM, 'proximoFinal':(bloco[1]-listaFilmes[bloco[0]].tamanhoFilme)}
                self.classificacao.append(pontoBloco)
        #self.classificacao=sorted(self.classificacao, key=itemgetter('pontuacao'))
        return self.classificacao
    def variavelGenericaMemoriaAcerto(self, valor):
        self.valorMaior+=1
        return self.valorMaior
    def variavelGenericaMemoriaCriacao(self):
        self.valorMaior+=1
        return self.valorMaior
    def organizarMemororia(self,memoria):
        # novaMemoria=[]
        # for bloco in memoria:
        #     novaMemoria.append([bloco[0],bloco[1],bloco[2],(bloco[3]+1)])
        return memoria;