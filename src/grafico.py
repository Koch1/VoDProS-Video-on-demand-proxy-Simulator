import os
from datetime import datetime
class grafico:
    import matplotlib.pyplot as plt
    def __init__(self):
        self.plt.figure()
    def gerarGrafico(self,nomeArquivo):
        self.plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,wspace=0.35)
        self.plt.savefig(nomeArquivo+'.png') 
        self.plt.close()
        
    def inciarGrafico(self,x,y,nomeGrafico,numero):
        self.plt.subplot(16, 1,numero )
        self.plt.plot(x, y)
        #self.plt.yscale('linear')
        self.plt.title(nomeGrafico)
        self.plt.grid(True)


class graficoUnico:
    import matplotlib.pyplot as plt
    def __init__(self,nomeArquivo,x,y,nomeGrafico,algorimos):
        self.fig, self.ax = self.plt.subplots()
        self.ax.plot(x, y)
        self.ax.set(xlabel='Tempo(s)', ylabel='Taxa acertos %',title=algorimos)
        self.ax.set_title(nomeGrafico)
        # self.plt.grid(b=True, which='major', color='black', linestyle='-',linewidth='1',alpha=2000)
        # # Show the minor grid lines with very faint and almost transparent grey lines
        # self.plt.minorticks_on()
        # self.plt.grid(b=True, which='minor', color='black', linestyle='-',linewidth='0.5',alpha=250)
        self.ax.minorticks_on()
        # Customize the major grid
        self.ax.grid(which='major', linestyle='-', linewidth='0.8', color='black')
        # Customize the minor grid
        self.ax.grid(which='minor', linestyle=':', linewidth='0.4', color='black')
        self.fig.savefig(nomeArquivo+'.png')
        self.plt.close()
        

class manipulacao:
    def __init__(self,arquivoLeitura):
            self.nomeArquivoLer=open (arquivoLeitura, 'r')
    def leituraLinha(self):
        a=str(self.nomeArquivoLer.readline())
        return a



def CalcularTaxaArray(PrimeiroArray,SegundoArray):
    taxa=[]
    cont=0
    while cont<len(PrimeiroArray):
        if(SegundoArray[cont]==0):
            taxa.append(0)
        else:
            taxa.append((PrimeiroArray[cont]/SegundoArray[cont])*100)
        cont+=1
    return taxa;
leitura='0'
a=manipulacao("resultadoGrafico3.txt")
while leitura.strip()!="":
    leitura=a.leituraLinha()
    if(leitura.strip()==""):
        leitura=a.leituraLinha()
    if(leitura.strip()=='Inicio'):
        while True:
            leitura=a.leituraLinha()
            if(leitura.strip()=='fim'):
                break
            if(leitura[-1]!=']'):
                stringNovo=""
                for idx,letra in enumerate(leitura):
                    if(letra=="=" and leitura[(idx+1)]!='[' and leitura[(idx+1)]!="'" and leitura[(idx+1):].isnumeric()==False):
                            stringNovo=stringNovo+"='"+leitura[(idx+1):-1]
                            stringNovo=stringNovo+"'"
                            break
                    stringNovo=stringNovo+letra
                #print(stringNovo)
                exec(stringNovo)
            else:
                exec(leitura)
        
        now = str(datetime.now())
        caminho="resultado9/"
        os.mkdir("./"+caminho+now+"-"+algoritimo)
        arquivoLido=arquivoLeitura.replace(".","")
        graficoUnico("./"+caminho+now+"-"+algoritimo+"/"+"Numero Acertos- Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,arrayAcertos,"Numero Acertos ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)
        graficoUnico("./"+caminho+now+"-"+algoritimo+"/"+"Taxa Acertos- Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,CalcularTaxaArray(arrayAcertos,arrayTotalClientesAtivos),"Taxa Acertos ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)
        graficoUnico("./"+caminho+now+"-"+algoritimo+"/"+"Taxa Acertos Pacotes- Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,CalcularTaxaArray(arrayTotalPacotesNaCache,arrayTotalClientesAtivos),"Taxa Acertos ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)

        graficoUnico("./"+caminho+now+"-"+algoritimo+"/"+"Numero Erros- Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,arrayErros,"Numero Erros ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)
        graficoUnico("./"+caminho+now+"-"+algoritimo+"/"+"Taxa Erros- Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,CalcularTaxaArray(arrayErros,arrayTotalClientesAtivos),"Taxa Erros ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)
        graficoUnico("./"+caminho+now+"-"+algoritimo+"/"+"Numero Solicitacao Bandas- Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,arraysolicitacaoBandas,"Numero Solicitacao Bandas ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)
        graficoUnico("./"+caminho+now+"-"+algoritimo+"/"+"Taxa Solicitacao Bandas- Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,CalcularTaxaArray(arraysolicitacaoBandas,arrayTotalClientesAtivos),"Taxa Solicitacao Bandas ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)
        graficoUnico("./"+caminho+now+"-"+algoritimo+"/"+"Numero Bandas Usada - Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,arrayBandasUsada,"Numero Bandas Usada ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)
        graficoUnico("./"+caminho+now+"-"+algoritimo+"/"+"Taxa Bandas Usada - Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,CalcularTaxaArray(arrayBandasUsada,arrayTotalClientesAtivos),"Taxa Bandas Usada ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)
        graficoUnico("./"+caminho+now+"-"+algoritimo+"/"+"Total Clientes- Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,arrayTotalClientes,"Total Clientes ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)
        graficoUnico("./"+caminho+now+"-"+algoritimo+"/"+"Total Clientes Ativos- Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,arrayTotalClientesAtivos,"Total Clientes Ativos ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)
        graficoUnico("./"+caminho+now+"-"+algoritimo+"/"+"Total Pacotes na Cache- Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,arrayTotalPacotesNaCache,"Total Pacotes na Cache ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)
        graficoUnico("./"+caminho+now+"-"+algoritimo+"/"+"Tempo Execucao- Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,arrayTempoExecucao,"Tempo Execucao ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)
        graficoUnico("./"+caminho+now+"-"+algoritimo+"/"+"Tempo Distribucao- Na Cahche- Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,arrayTempoDistribucaoNaCache,"Tempo Distribucao Na Cahche ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)
        graficoUnico("./"+caminho+now+"-"+algoritimo+"/"+"Tempo Entrada Cliente- Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,arrayTempoEntradaCliente,"Tempo Entrada Cliente ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)
        graficoUnico("./"+caminho+now+"-"+algoritimo+"/"+"Tempo Ordenacao Pedidos- Requisicao- Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,arrayTempoOrdenacaoPedidosRequisicao,"Tempo Ordenacao Pedidos Requisicao ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)    
        graficoUnico("./"+caminho+now+"-"+algoritimo+"/"+"Tempo Gerar Tabela Substituicao- Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,arrayTempoGerarTabelaSubstituicao,"Tempo Gerar Tabela Substituicao ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)
        graficoUnico("./"+caminho+now+"-"+algoritimo+"/"+"Tempo Distribucao Na Requicao Atendidas- Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,arrayTempoDistribucaoNaRequicaoAtendidas,"Tempo Distribucao Na Requicao Atendidas ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)
        media=0
        contt=0
        cliente=0
        for aa in arrayTempo:
            if(aa>5600 and aa<6600):
                media+=arrayAcertos[aa]
                cliente+=arrayTotalClientesAtivos[aa]
                contt+=1
        arquivoEscrita = open("./"+caminho+now+"-"+algoritimo+"/"+"Dados da simulação.txt", "w")
        if(media>0 and contt>0 and cliente>0):
            arquivoEscrita.write('Media Acertos='+str(((media/contt)/(cliente/contt))))
        arquivoEscrita.write('\n')
        arquivoEscrita.write('Algorimo Usado:'+algoritimo)
        arquivoEscrita.write('\n')
        arquivoEscrita.write('DataExecusao:'+dataExecucao)
        arquivoEscrita.write('\n')
        arquivoEscrita.write('Tamanho Video:'+tamanhoVideo)
        arquivoEscrita.write('\n')
        arquivoEscrita.write('Nome Arquivo Lido:'+str(arquivoLeitura))
        arquivoEscrita.write('\n')
        arquivoEscrita.write('Tamanho  Memoria'+str(memoria))
        arquivoEscrita.write('\n')
        arquivoEscrita.write('Numero de ciclos tempos:'+str(tempoTotalCiclos)+" segundos simulados ")
        arquivoEscrita.write('\n')
        arquivoEscrita.write('Tempo para execução :'+str(tempoTotalExecucao)+" segundos")
        arquivoEscrita.close()

##        now = datetime.now()
##        arquivoLido=arquivoLeitura.replace(".","")
##        b=grafico()
##        b.inciarGrafico(arrayTempo,arrayAcertos,"Acertos-"+algoritimo,1)
##        b.inciarGrafico(arrayTempo,arrayErros,"Erros-"+algoritimo,2)
##        b.inciarGrafico(arrayTempo,arraysolicitacaoBandas,"SolicitacaoBandas-"+algoritimo,3)
##        b.inciarGrafico(arrayTempo,arrayBandasUsada,"Bandas Usada-"+algoritimo,4)
##        b.gerarGrafico("1-Memoria:"+str(memoria)+"-Banda:"+str(banda)+"-Banda:"+str(algoritimo)+"-Arquivo:"+str(arquivoLido)+"Horario"+str(now))
##        b=grafico()
##        b.inciarGrafico(arrayTempo,arrayTotalClientes," Total Clientes-"+algoritimo,1)
##        b.inciarGrafico(arrayTempo,arrayTotalClientesAtivos,"Total Clientes Ativos-"+algoritimo,2)
##        b.inciarGrafico(arrayTempo,arrayTotalPacotesNaCache,"Total Pacotes Na Cache-"+algoritimo,3)
##        b.gerarGrafico("2-Memoria:"+str(memoria)+"-Banda:"+str(banda)+"-Banda:"+str(algoritimo)+"-Arquivo:"+str(arquivoLido)+"Horario"+str(now))
##        b=grafico()
##        b.inciarGrafico(arrayTempo,arrayTempoExecucao,"Tempo Execucao-"+algoritimo,1)
##        b.inciarGrafico(arrayTempo,arrayTempoDistribucaoNaCahche,"Tempo Distribucao Na Cahche-"+algoritimo,2)
##        b.inciarGrafico(arrayTempo,arrayTempoEntradaCliente,"Tempo Entrada Cliente-"+algoritimo,3)
##        b.gerarGrafico("3-Memoria:"+str(memoria)+"-Banda:"+str(banda)+"-Banda:"+str(algoritimo)+"-Arquivo:"+str(arquivoLido)+"Horario"+str(now))
##        b=grafico()
##        b.inciarGrafico(arrayTempo,arrayTempoOrdenacaoPedidosRequisicao,"Tempo Ordenacao Pedidos Requisicao-"+algoritimo,1)
##        b.inciarGrafico(arrayTempo,arrayTempoGerarTabelaTubstituicao,"TempoGerar Tabela Substituicao-"+algoritimo,2)
##        b.inciarGrafico(arrayTempo,arrayTempoDistribucaoNaRequicaoAtendidas,"Tempo Distribucao Na Requicao Atendidas-"+algoritimo,3)
##        b.gerarGrafico("4-Memoria:"+str(memoria)+"-Banda:"+str(banda)+"-Banda:"+str(algoritimo)+"-Arquivo:"+str(arquivoLido)+"Horario"+str(now))        


# import matplotlib.pyplot as plt

# # The Data
# x = [1, 2, 3, 4]
# y = [234, 124,368, 343]

# # Create the figure and axes objects
# fig, ax = plt.subplots()
# fig.suptitle('Example Of Plot With Major and Minor Grid Lines')

# # Plot the data
# ax.plot(x,y)

# # Show the major grid lines with dark grey lines
# plt.grid(b=True, which='major', color='#666666', linestyle='-', alpha=0.5)

# # Show the minor grid lines with very faint and almost transparent grey lines
# plt.minorticks_on()
# plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.1)

# plt.show()