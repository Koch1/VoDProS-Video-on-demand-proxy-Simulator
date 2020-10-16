class GeradorGraficos:
    def __init__(self,arquivo,algoritimo):
        self.nomeAlgoritimo=algoritimo
        self.acertos=0
        self.arrayAcertos=[]
        self.erros=0
        self.arrayErros=[]
        self.arrayTempo=[]
        self.solicitacaoBandas=0
        self.arraysolicitacaoBandas=[]
        self.arrayBandasUsada=[]
        self.arquivoLeitura=arquivo
        self.totalClientes=0
        self.totalPacotesNaCache=0
        self.totalClientesAtivos=0
        self.arrayTotalClientes=[]
        self.arrayTotalPacotesNaCache=[]
        self.arrayTotalClientesAtivos=[]


    def acerto(self):
        self.acertos=self.acertos+1
    def erro(self):
        self.erros=self.erros+1
    def solicBanda(self):
        self.solicitacaoBandas=self.solicitacaoBandas+1
    def novoCliente(self):
        self.totalClientes=self.totalClientes+1
        self.totalClientesAtivos=self.totalClientesAtivos+1
    def terminouCliente(self):
        self.totalClientesAtivos=self.totalClientesAtivos-1
    def cachePacote(self):
        self.totalPacotesNaCache=self.totalPacotesNaCache+1

    def adiconarTempo(self,tempo,banda,solicBanda):
        self.arrayTempo.append(tempo)
        self.arrayAcertos.append(self.acertos)
        self.acertos=0
        self.arrayErros.append(self.erros)
        self.erros=0
        self.arraysolicitacaoBandas.append(self.solicitacaoBandas)
        self.solicitacaoBandas=0
        if(banda>solicBanda):
            self.arrayBandasUsada.append(solicBanda)
        else: 
            self.arrayBandasUsada.append(banda)
        self.arrayTotalPacotesNaCache.append(self.totalPacotesNaCache)
        self.totalPacotesNaCache=0
        self.arrayTotalClientesAtivos.append(self.totalClientesAtivos)
        self.arrayTotalClientes.append(self.totalClientes)

    def graficoGerar(self, memoria, banda):
        # print(self.arrayTempo)
        # print(self.arrayAcertos)
        # print(self.arrayErros)
        # print(self.arraysolicitacaoBandas)
        # print(self.arrayBandasUsada)
        # print(self.arrayTotalClientes)
        # print(self.arrayTotalClientesAtivos)
        #print(self.arrayTotalPacotesNaCache)
        
        import plotly.graph_objects as go
        import numpy as np
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=self.arrayTempo, y=self.arrayAcertos,
                            mode='lines+markers',
                            name='Acertos',line=dict(width=1)))
        fig.add_trace(go.Scatter(x=self.arrayTempo, y=self.arrayErros,
                            mode='lines+markers',
                            name='Erros',line=dict(width=1)))
        fig.add_trace(go.Scatter(x=self.arrayTempo, y=self.arraysolicitacaoBandas,
                            mode='lines+markers',
                            name='Solicitação de Banda',line=dict(width=1)))
        fig.add_trace(go.Scatter(x=self.arrayTempo, y=self.arrayBandasUsada,
                            mode='lines+markers',
                            name='Banda Usada',line=dict(width=1)))
        fig.add_trace(go.Scatter(x=self.arrayTempo, y=self.arrayTotalClientesAtivos,
                            mode='lines+markers',
                            name='Total Clientes Ativos',line=dict(width=1)))
        fig.add_trace(go.Scatter(x=self.arrayTempo, y=self.arrayTotalPacotesNaCache,
                            mode='lines+markers',
                            name='Total Pacotes da Cache' ,line=dict(width=1)))
        fig.add_trace(go.Scatter(x=self.arrayTempo, y=self.arrayTotalClientes,
                            mode='lines+markers',
                            name='Total Cliente ',line=dict(width=1)))
        # # Edit the layout
        fig.update_layout(title=' Graficos tudo <br> Configurações: Memoria:'+str(memoria)+' LarguraBanda:'+str(banda),
                        xaxis_title='Tempo',
                        yaxis_title='Demais informaçoes')
        fig.show()
    
