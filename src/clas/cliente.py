class Cliente:
    def __init__ (self,cliente,tempo,filme,bloco,tamanhoBloco):
        self.idCliente=int(cliente)
        self.idFilme=int(filme)
        self.tempoInicio=int(tempo)
        self.idBloco=int(bloco)
        self.tamanhoBloco=tamanhoBloco
    
    def __repr__(self):
        return 'Cliente:'+str(self.idCliente)+' Filme:'+str(self.idFilme)+" Bloco:"+str(self.idBloco)+" Tempo Inicio:"+str(self.tempoInicio)

        
    def trocaBloco(self, listaFilmes,janela):
        if(self.idBloco==-1):
            listaFilmes[self.idFilme].numeroClientes+=1
            
        else:
            if((listaFilmes[self.idFilme].blocos).get(self.idBloco)!=None):
                listaFilmes[self.idFilme].blocos[self.idBloco]-=1
        if(janela>0  and (self.idBloco-janela)>=0):
            listaFilmes[self.idFilme].classificacao[self.idBloco-janela]-=1
        self.idBloco+=1
        if((listaFilmes[self.idFilme].blocos).get(self.idBloco)!=None):
            listaFilmes[self.idFilme].blocos[self.idBloco]+=1
            listaFilmes[self.idFilme].classificacao[self.idBloco]+=1
        else:
            listaFilmes[self.idFilme].blocos[self.idBloco]=1
            listaFilmes[self.idFilme].classificacao[self.idBloco]=1