class Resultado:
    def __init__(self,arquivo,algoritimo):
        self.nomeAlgoritimo=algoritimo
        self.acertos=0
        self.erros=0
        self.arquivoLeitura=arquivo
        self.totalClientes=0
        self.totalPacotesEntregues=0
        self.totalClientesAtivos=0
        self.totalClientesEspera=0

    def acerto(self):
        self.acertos=self.acertos+1
    def erro(self):
        self.erros=self.erros+1
    def novoCliente(self):
        self.totalClientes=self.totalClientes+1
        self.totalClientesAtivos=self.totalClientesAtivos+1
    def terminouCliente(self):
        self.totalClientesAtivos=self.totalClientesAtivos-1
    def entreguePacote(self):
        self.totalPacotesEntregues=self.totalPacotesEntregues+1
    def clienteNaEspera(self):
        self.totalClientesEspera=self.totalClientesEspera+1
    def clienteSaioDaEspera(self):
        self.totalClientesEspera=self.totalClientesEspera-1
    
