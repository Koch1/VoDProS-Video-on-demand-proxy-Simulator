from printDados import PrintDados
from operator import itemgetter, attrgetter
class AlgortimoCARTE:
    def __init__(self, janela):
        self.janelaCarte=janela
        self.classificacao=[]

    def substituicaoBlocos(self,listaFilmes,cliente,memoria,listaClientes):
        listaSub=self.calcularTabelaSubituicao(memoria,listaClientes,listaFilmes)
        cliente.trocaBloco(listaFilmes)
        del(listaFilmes[listaSub['idFilme']].blocos[listaSub['idBloco']])
        del(listaFilmes[listaSub['idFilme']].blocoMemoria[listaSub['idBloco']])
        listaFilmes[cliente.idFilme].blocoMemoria[cliente.idBloco]=listaSub['memoria']
        memoria[listaSub['memoria']]=[cliente.idFilme,cliente.idBloco,listaFilmes[cliente.idFilme].blocos[cliente.idBloco]]

    def calcularTabelaSubituicao(self,memoria,listaClientes,listaFilmes):
        self.classificacao=[]
        for idM, bloco in enumerate(memoria):
            pontoBloco={'idFilme':bloco[0],'idBloco':bloco[1], 'pontuacao':0, 'memoria':idM, 'proximoFinal':(bloco[1]-listaFilmes[bloco[0]].tamanhoFilme)}
            for client in listaClientes:
                if(client.idFilme==bloco[0] and client.idBloco<bloco[1] and client.idBloco>(bloco[1]-self.janelaCarte) and client.idBloco>=0):
                    pontoBloco['pontuacao']+=1
            self.classificacao.append(pontoBloco)
        self.classificacao=sorted(self.classificacao, key=itemgetter('pontuacao', 'proximoFinal'))
        return self.classificacao[0]