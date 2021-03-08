class Pacote:
    def __init__ (self,filme,bloco,tam):
        self.idFilme=int(filme)
        self.idBloco=int(bloco)
        self.contador=1
        self.posicao=tam
    def addContador(self):
        self.contador+=1
    def __repr__(self):
        return 'Filme:'+str(self.idFilme)+" Bloco:"+str(self.idBloco)+" Contador:"+str(self.contador)