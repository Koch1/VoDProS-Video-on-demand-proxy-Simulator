class geradorGraficos:
    def __init__(self,arquivo,algoritimo):
        self.nomeAlgoritimo=algoritimo
        self.acertos=0
        self.arrayAcertos=[]
        self.erros=0
        self.arrayErros=[]
        self.arrayTempo=[]
        self.erroBandas=0
        self.arrayErroBandas=[]
        self.arquivoLeitura=arquivo
        self.totalClientes=0
        self.totalPacotesEntregues=0
        self.totalClientesAtivos=0
        self.totalClientesEspera=0
        self.arrayTotalClientes=[]
        self.arrayTotalPacotesEntregues=[]
        self.arrayTotalClientesAtivos=[]
        self.arrayTotalClientesEspera=[]

    def acerto(self):
        self.acertos=self.acertos+1
    def erro(self):
        self.erros=self.erros+1
    def erroBanda(self):
        self.erroBandas=self.erroBandas+1
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
    def adiconarTempo(self,tempo):
        self.arrayTempo.append(tempo)
        self.arrayAcertos.append(self.acertos)
        self.acertos=0
        self.arrayErros.append(self.erros)
        self.erros=0
        self.arrayErroBandas.append(self.erroBandas)
        self.erroBandas=0
        self.arrayErros.append(self.erros)
        self.erros=0
        self.arrayTotalClientes.append(self.totalClientes)
        self.totalClientes=0
        self.arrayTotalPacotesEntregues.append(self.totalPacotesEntregues)
        self.totalPacotesEntregues=0
        self.arrayTotalClientesAtivos.append(self.totalClientesAtivos)
        self.arrayTotalClientesEspera.append(self.totalClientesEspera)


    def graficoGerar(self):
        import plotly.graph_objects as go
        import numpy as np
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=self.arrayTempo, y=self.arrayAcertos,
                            mode='lines+markers',
                            name='Acertos'))
        fig.add_trace(go.Scatter(x=self.arrayTempo, y=self.arrayErros,
                            mode='lines+markers',
                            name='Erros'))
        fig.add_trace(go.Scatter(x=self.arrayTempo, y=self.totalClientes,
                            mode='lines+markers',
                            name='Total Cliente'))
        fig.add_trace(go.Scatter(x=self.arrayTempo, y=self.totalClientesAtivos,
                            mode='lines+markers',
                            name='Total Clientes Ativos'))
        fig.add_trace(go.Scatter(x=self.arrayTempo, y=self.totalPacotesEntregues,
                            mode='lines+markers',
                            name='Total Pacotes Entregues'))
        fig.add_trace(go.Scatter(x=self.arrayTempo, y=self.totalClientesEspera,
                            mode='lines+markers',
                            name='Total Cliente Espera'))
        # Edit the layout
        fig.update_layout(title=' Graficos tudo',
                        xaxis_title='Tempo',
                        yaxis_title='Demais informaçoes')
        fig.show()
    
