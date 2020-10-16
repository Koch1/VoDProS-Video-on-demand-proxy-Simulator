class Cliente:
    def __init__ (self,cliente,tempo,filme,bloco):
        self.idCliente=int(cliente)
        self.idFilme=int(filme)
        self.tempoInicio=int(tempo)
        self.idBloco=int(bloco)
        self.tamanhoBloco=1000
    def trocaBloco(self, listaFilmes):
        if(self.idBloco==-1):
            listaFilmes[self.idFilme].numeroClientes+=1
        else:
            if(self.idBloco in listaFilmes[self.idFilme].blocos):
                listaFilmes[self.idFilme].blocos[self.idBloco]-=1
        self.idBloco+=1
        if(self.idBloco in listaFilmes[self.idFilme].blocos):
            listaFilmes[self.idFilme].blocos[self.idBloco]+=1
        else:
            listaFilmes[self.idFilme].blocos[self.idBloco]=1