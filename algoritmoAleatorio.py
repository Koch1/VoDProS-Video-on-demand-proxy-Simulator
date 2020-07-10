import random 

class AlgortimoAleatorio:
    def substituicaoBlocos(self,listaFilmes,cliente,memoria,listaClientes,classificacao):
        r1 = random.randint(0, (len(memoria)-1))
        cliente.trocaBloco(listaFilmes)
        print(len(memoria))
        del(listaFilmes[memoria[r1][0]].blocos[memoria[r1][1]])
        del(listaFilmes[memoria[r1][0]].blocoMemoria[memoria[r1][1]])
        listaFilmes[cliente.idFilme].blocoMemoria[cliente.idBloco]=r1
        memoria[r1]=[cliente.idFilme,cliente.idBloco,listaFilmes[cliente.idFilme].blocos[cliente.idBloco]]
        


       
