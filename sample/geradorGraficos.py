import threading
import os
from datetime import datetime
class GeradorGraficos:
    def __init__(self,arquivo,algoritimo,memoria,banda,video):
        self.nomeAlgoritimo=algoritimo
        self.memoria=memoria
        self.banda=banda
        self.tamanhovideo=video
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
        #Tempo Execucao
        self.arrayTempoExecucaoCiclo=[]
        self.tempoCiclo=0
        self.arrayTempoDistribucaoNaCache=[]
        self.tempoDistribucaoNaCache=0
        self.arrayTempoEntradaCliente=[]
        self.tempoEntradaCliente=float(0)
        self.arrayTempoOrdenacaoPedidosRequisicao=[]
        self.tempoOrdenacaoPedidosRequisicao=0
        self.arrayTempoGerarTabelaSubstituicao=[]
        self.tempoGerarTabelaSubstituicao=0
        self.arrayTempoDistribucaoNaRequicaoAtendidas=[]
        self.tempoDistribucaoNaRequicaoAtendidas=0
        

    def tempoCicloDef(self,tempo):
        self.tempoCiclo=tempo
    def tempoDistribucaoNaCacheDef(self,tempo):
        self.tempoEntradaCliente=tempo
    def tempoEntradaClienteDef(self,tempo):
        self.tempoEntradaCliente=tempo
    def tempoOrdenacaoPedidosRequisicaoDef(self,tempo):
        self.tempoOrdenacaoPedidosRequisicao=tempo
    def tempoGerarTabelaSubstituicaoDef(self,tempo):
        self.tempoGerarTabelaSubstituicao+=tempo
    def tempoDistribucaoNaRequicaoAtendidasDef(self,tempo):
        self.tempoDistribucaoNaRequicaoAtendidas=tempo
        
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
        #Tempo execução
        self.arrayTempoExecucaoCiclo.append(self.tempoCiclo)
        self.tempoCiclo=0
        self.arrayTempoDistribucaoNaCache.append(self.tempoDistribucaoNaCache)
        self.tempoDistribucaoNaCache=0
        self.arrayTempoEntradaCliente.append(self.tempoEntradaCliente)
        self.tempoEntradaCliente=0
        self.arrayTempoOrdenacaoPedidosRequisicao.append(self.tempoOrdenacaoPedidosRequisicao)
        self.tempoOrdenacaoPedidosRequisicao=0
        self.arrayTempoGerarTabelaSubstituicao.append(self.tempoGerarTabelaSubstituicao)
        self.tempoGerarTabelaSubstituicao=0
        self.arrayTempoDistribucaoNaRequicaoAtendidas.append(self.tempoDistribucaoNaRequicaoAtendidas)
        self.tempoDistribucaoNaRequicaoAtendidas=0
        
    def salvarDados(self,tempoFinal,ciclo):
        nomeArquivo=open ('resultadoGrafico.txt','a')
        nomeArquivo.write('Inicio');
        nomeArquivo.write('\n')
        nomeArquivo.write('algoritimo='+(str(self.nomeAlgoritimo)))
        nomeArquivo.write('\n')
        nomeArquivo.write('dataExecucao='+(str(str(datetime.now()))))
        nomeArquivo.write('\n')
        nomeArquivo.write('tamanhoVideo='+(str(self.tamanhovideo)))
        nomeArquivo.write('\n')
        nomeArquivo.write('arquivoLeitura='+(str(self.arquivoLeitura)))
        nomeArquivo.write('\n')
        nomeArquivo.write('memoria='+(str(self.memoria)))
        nomeArquivo.write('\n')
        nomeArquivo.write('banda='+(str(self.banda)))
        nomeArquivo.write('\n')
        nomeArquivo.write('tempoTotalCiclos='+(str(ciclo)))
        nomeArquivo.write('\n')
        nomeArquivo.write('tempoTotalExecucao='+(str(tempoFinal)))
        nomeArquivo.write('\n')
        nomeArquivo.write('arrayTempo='+(str(self.arrayTempo)))
        nomeArquivo.write('\n')
        nomeArquivo.write('arrayAcertos='+(str(self.arrayAcertos)))
        nomeArquivo.write('\n')
        nomeArquivo.write('arrayErros='+(str(self.arrayErros)))
        nomeArquivo.write('\n')
        nomeArquivo.write('arraysolicitacaoBandas='+(str(self.arraysolicitacaoBandas)))
        nomeArquivo.write('\n')
        nomeArquivo.write('arrayBandasUsada='+(str(self.arrayBandasUsada)))
        nomeArquivo.write('\n')
        nomeArquivo.write('arrayTotalClientes='+(str(self.arrayTotalClientes)))
        nomeArquivo.write('\n')
        nomeArquivo.write('arrayTotalClientesAtivos='+(str(self.arrayTotalClientesAtivos)))
        nomeArquivo.write('\n')
        nomeArquivo.write('arrayTotalPacotesNaCache='+(str(self.arrayTotalPacotesNaCache)))
        nomeArquivo.write('\n')
        nomeArquivo.write('arrayTempoExecucao='+(str(self.arrayTempoExecucaoCiclo)))
        nomeArquivo.write('\n')
        nomeArquivo.write('arrayTempoDistribucaoNaCache='+(str(self.arrayTempoDistribucaoNaCache)))
        nomeArquivo.write('\n')
        nomeArquivo.write('arrayTempoEntradaCliente='+(str(self.arrayTempoEntradaCliente)))
        nomeArquivo.write('\n')
        nomeArquivo.write('arrayTempoOrdenacaoPedidosRequisicao='+(str(self.arrayTempoOrdenacaoPedidosRequisicao)))
        nomeArquivo.write('\n')
        nomeArquivo.write('arrayTempoGerarTabelaSubstituicao='+(str(self.arrayTempoGerarTabelaSubstituicao)))
        nomeArquivo.write('\n')
        nomeArquivo.write('arrayTempoDistribucaoNaRequicaoAtendidas='+(str(self.arrayTempoDistribucaoNaRequicaoAtendidas)))
        nomeArquivo.write('\n')
        nomeArquivo.write('fim')
        nomeArquivo.write('\n')
        nomeArquivo.write('\n')

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
        fig = go.Figure(layout_title_text="A Figure Displayed with the 'png' Renderer")
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
        fig.update_layout(title=' Graficos '+self.nomeAlgoritimo+' <br> Configurações: Memoria:'+str(memoria)+' LarguraBanda:'+str(banda),
                        xaxis_title='Tempo',
                        yaxis_title='Demais informaçoes')
        fig.show(renderer="png", width=800, height=300)
    
