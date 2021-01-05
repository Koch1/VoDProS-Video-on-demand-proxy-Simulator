from printDados import PrintDados
from operator import itemgetter, attrgetter
class AlgoritmoLFUcomJanela:
    def __init__(self, jan):
        self.classificacao=[]
        self.janela=jan
        self.nomeAlgoritmo="LFU com janela de "+str(jan)
    

    def substituicaoBlocos(self,listaFilmes,cliente,memoria,listaClientes,solicitacoes,listaSub):
        #listaSub=self.calcularTabelaSubituicao(memoria,listaClientes,listaFilmes,solicitacoes)
        cliente.trocaBloco(listaFilmes)
        del(listaFilmes[listaSub['idFilme']].blocos[listaSub['idBloco']])
        del(listaFilmes[listaSub['idFilme']].blocoMemoria[listaSub['idBloco']])
        listaFilmes[cliente.idFilme].blocoMemoria[cliente.idBloco]=listaSub['memoria']
        memoria[listaSub['memoria']]=[cliente.idFilme,cliente.idBloco,listaFilmes[cliente.idFilme].blocos[cliente.idBloco],(self.variavelGenericaMemoriaCriacao())]

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
    def variavelGenericaMemoriaAcerto(self, valor):
        return valor+1
    def variavelGenericaMemoriaCriacao(self):
        return 1
    def organizarMemororia(self,memoria):
        return memoria;