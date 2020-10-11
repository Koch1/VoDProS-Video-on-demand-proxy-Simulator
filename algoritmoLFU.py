from printDados import PrintDados
from operator import itemgetter, attrgetter
class AlgoritmoLFU:
    def __init__(self):
        self.classificacao=[]

    def substituicaoBlocos(self,listaFilmes,cliente,memoria,listaClientes):
        listaSub=self.calcularTabelaSubituicao(memoria,listaClientes,listaFilmes)
        cliente.trocaBloco(listaFilmes)
        del(listaFilmes[listaSub['idFilme']].blocos[listaSub['idBloco']])
        del(listaFilmes[listaSub['idFilme']].blocoMemoria[listaSub['idBloco']])
        listaFilmes[cliente.idFilme].blocoMemoria[cliente.idBloco]=listaSub['memoria']
        memoria[listaSub['memoria']]=[cliente.idFilme,cliente.idBloco,listaFilmes[cliente.idFilme].blocos[cliente.idBloco],self.variavelGenericaMemoriaCriacao()]

    def calcularTabelaSubituicao(self,memoria,listaClientes,listaFilmes):
        self.classificacao=[]
        for idM, bloco in enumerate(memoria):
            pontoBloco={'idFilme':bloco[0],'idBloco':bloco[1], 'pontuacao':bloco[3], 'memoria':idM}
            self.classificacao.append(pontoBloco)
            # sorted ordena do menor para maior,  caso coloque mais um paretro reverse=True ele inverte
        self.classificacao=sorted(self.classificacao, key=itemgetter('pontuacao'))
        return self.classificacao[0]
    def variavelGenericaMemoriaAcerto(self, valor):
        return valor+1
    def variavelGenericaMemoriaCriacao(self):
        return 1
    def organizarMemororia(self,memoria):
        return memoria;