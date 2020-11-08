class Filme:
    def __init__ (self,filme):
        self.idFilme=filme
        self.blocos={}
        self.blocoMemoria={}
        self.clientes={}
        self.numeroClientes=0
        self.tamanhoFilme=10
    def __repr__(self):
        return 'Filme:'+str(self.idFilme)+" Bloco:"+str(self.blocos)+" Bloco Memoria:"+str(self.blocoMemoria)+" Numero Cliente:"+str(self.numeroClientes)
