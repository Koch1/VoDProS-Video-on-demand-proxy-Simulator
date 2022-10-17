import os
from datetime import datetime
# import math
# from operator import itemgetter

# class grafico:
#     import matplotlib.pyplot as plt
#     def __init__(self):
#         self.plt.figure()
#     def gerarGrafico(self,nomeArquivo):
#         self.plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,wspace=0.35)
#         self.plt.savefig(nomeArquivo+'.png') 
#         self.plt.close()
        
#     def inciarGrafico(self,x,y,nomeGrafico,numero):
#         self.plt.subplot(16, 1,numero )
#         self.plt.plot(x, y)
#         #self.plt.yscale('linear')
#         self.plt.title(nomeGrafico)
#         self.plt.grid(True)


# class graficoUnico:
#     import matplotlib.pyplot as plt
#     def __init__(self,nomeArquivo,x,y,nomeGrafico,algorimos):
#         self.fig, self.ax = self.plt.subplots()
#         self.ax.plot(x, y)
#         self.ax.set(xlabel='Tempo(s)', ylabel='Taxa acertos %',title=algorimos)
#         self.ax.set_title(nomeGrafico)
#         # self.plt.grid(b=True, which='major', color='black', linestyle='-',linewidth='1',alpha=2000)
#         # # Show the minor grid lines with very faint and almost transparent grey lines
#         # self.plt.minorticks_on()
#         # self.plt.grid(b=True, which='minor', color='black', linestyle='-',linewidth='0.5',alpha=250)
#         self.ax.minorticks_on()
#         # Customize the major grid
#         self.ax.grid(which='major', linestyle='-', linewidth='0.8', color='black')
#         # Customize the minor grid
#         self.ax.grid(which='minor', linestyle=':', linewidth='0.4', color='black')
#         self.fig.savefig(nomeArquivo+'.png')
#         self.plt.close()
        
# class graficoConjuntoDadosxy:
#     import matplotlib.pyplot as plt
#     def __init__(self,nomeArquivo,x,y,nomeGrafico,algorimos,eixox):
#         self.fig, self.ax = self.plt.subplots()
#         self.ax.plot(x, y)
#         self.ax.set(xlabel=eixox, ylabel='Taxa acertos %',title=algorimos)
#         self.ax.set_title(nomeGrafico)
#         # self.plt.grid(b=True, which='major', color='black', linestyle='-',linewidth='1',alpha=2000)
#         # # Show the minor grid lines with very faint and almost transparent grey lines
#         # self.plt.minorticks_on()
#         # self.plt.grid(b=True, which='minor', color='black', linestyle='-',linewidth='0.5',alpha=250)
#         self.ax.minorticks_on()
#         # Customize the major grid
#         self.ax.grid(which='major', linestyle='-', linewidth='0.8', color='black')
#         # Customize the minor grid
#         self.ax.grid(which='minor', linestyle=':', linewidth='0.4', color='black')
#         self.fig.savefig(nomeArquivo+'.png')
#         self.plt.close()        
# class graficoConjuntoResultados:
#     import matplotlib.pyplot as plt
#     def __init__(self,nomeArquivo,x,y,z,nomeGrafico,algorimos,eixox):
#         #self.fig, self.ax = self.plt.subplots()
#         #self.ax.plot(x, y)
#         #self.ax.set(xlabel='Tempo(s)', ylabel='Taxa acertos %',title=algorimos)
#         #self.ax.set_title(nomeGrafico)
#         # self.plt.grid(b=True, which='major', color='black', linestyle='-',linewidth='1',alpha=2000)
#         # # Show the minor grid lines with very faint and almost transparent grey lines
#         # self.plt.minorticks_on()
#         # self.plt.grid(b=True, which='minor', color='black', linestyle='-',linewidth='0.5',alpha=250)
#         #self.ax.minorticks_on()
#         # Customize the major grid
#         #self.ax.grid(which='major', linestyle='-', linewidth='0.8', color='black')
#         # Customize the minor grid
#         #self.ax.grid(which='minor', linestyle=':', linewidth='0.4', color='black')
#         self.fig, self.ax = self.plt.subplots()
#         self.ax.plot(x, y,'o-')
#         a=0
#         desvio=0
#         maior=y[0]
#         menor=y[0]
#         for val in y:
#             if(maior<val):
#                 maior=val
#             elif(menor>val):
#                 menor=val
#         desvio=((maior-menor)*0.5)/10
#         a=0
#         while a<len(z):
#             self.ax.annotate(z[a],(x[a], y[a]+desvio),horizontalalignment='center',verticalalignment='top',)
#             a+=1
#         self.ax.set(xlabel=eixox, ylabel='Taxa acertos %',title=algorimos)
#         self.ax.set_title(nomeGrafico)
#         self.ax.grid()
#         self.fig.savefig(nomeArquivo+'.png')
#         #self.plt.show()
#         self.plt.close()

class manipulacao:
    def __init__(self,arquivoLeitura):
            self.fimArquivo=self.procurarFimArquivo(arquivoLeitura)
            self.nomeArquivoLer=open (arquivoLeitura, 'r')
            self.nomeArquivo=""
            self.numeroLinhas=0
            
            #self.linha=0
    def verificarFimArquivo(self):
        if(self.fimArquivo<self.numeroLinhas):
            return True
        else:
            return False
        
    def procurarFimArquivo(self,arquivoLeitura):
        arquivo=open (arquivoLeitura, 'r')
        contador=-25
        fimArquivos=0
        a=""
        while (a!="" or fimArquivos<10):
            a=str(arquivo.readline())
            if(a==""):
                fimArquivos+=1
            else:
                fimArquivos=0
            contador+=1
        arquivo.close()
            
        return contador
        
    def leituraLinha(self):
        a=str(self.nomeArquivoLer.readline())
        self.numeroLinhas+=1
        #self.linha+=1
        #print(self.linha)
        return a
    def fechar(self):
        self.nomeArquivoLer.close()



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
a=manipulacao("../resultados/resultados/resultadoGraficoAlgoritmoRandon1-memoria-zip1-1.txt.txt")
a.nomeArquivo="resultadoGraficoAlgoritmoRandon1-memoria-zip1"
listaAquivosLista=[]
listaAquivosLista.append("resultadoGraficoAlgoritmoRandon1-memoria-zip1-1.txt.txt")
algoritmosEscolhido="resultadoGraficoAlgoritmoRandon1-memoria-zip1"
arquivoEscolida=1
now = str(datetime.now())
InicioCaminho="../resultados/resultadosGraficos/"+now
os.mkdir(InicioCaminho)
graf=2
listaPontosx={}
listaPontosy={}
listaPontosJanela={}
mediaDado={}
contador=0
fimArquivos=0


while (leitura.strip()!="" and fimArquivos<10):
    #print("1")
    #print("TO AQUI")
    leitura=a.leituraLinha()
    
    
    #if(contador>497):
        #print("2")
        #breakpoint
    #if(leitura.strip()==""):
    #    leitura=a.leituraLinha()
    #    fimArquivos+=1
    while(leitura.strip()=="" and fimArquivos<10):
        leitura=a.leituraLinha()
        fimArquivos+=1
        #print("3")
    #print("TO AQUI 1")
    #print(leitura)
    #print("TO AQUI 1")
    if(leitura.strip()=='Inicio'):
        fimArquivos=0
        contador+=1
        print(contador)
        if(contador<-1):
            while leitura.strip()!='fim':
                leitura=a.leituraLinha()
            ##leitura dados de uma simuação
            #print("4")
        else:
            #print("8")
            while True:
                leitura=a.leituraLinha()
                #print(leitura)
                #if(contador>497):
                #    breakpoint
                #    print("5")
                if(leitura.strip()=='fim' or leitura.strip()==""):
                 #   print("7")
                    break
                if(len(leitura)>0 and leitura[-1]!=']'):
                    stringNovo=""
                  #  print("6")
                    for idx,letra in enumerate(leitura):
                        if(letra=="=" and leitura[(idx+1)]!='[' and leitura[(idx+1)]!="'" and leitura[(idx+1):].isnumeric()==False):
                                stringNovo=stringNovo+"='"+leitura[(idx+1):-1]
                                stringNovo=stringNovo+"'"
                                break
                        stringNovo=stringNovo+letra
                    #print(stringNovo)
                    exec(stringNovo)
                else:
                   # print("7")
                   # print(leitura)
                    exec(leitura)
            now = str(datetime.now())
            if(graf==1 or graf==3):
                os.mkdir("./"+InicioCaminho+"/"+now+"-"+algoritimo)
                arquivoLido=arquivoLeitura.replace(".","")
                graficoUnico("./"+InicioCaminho+"/"+now+"-"+algoritimo+"/"+"Numero Acertos- Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,arrayAcertos,"Numero Acertos ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)
                graficoUnico("./"+InicioCaminho+"/"+now+"-"+algoritimo+"/"+"Taxa Acertos- Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,CalcularTaxaArray(arrayAcertos,arrayTotalClientesAtivos),"Taxa Acertos ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)
                graficoUnico("./"+InicioCaminho+"/"+now+"-"+algoritimo+"/"+"Taxa Acertos Pacotes- Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,CalcularTaxaArray(arrayTotalPacotesNaCache,arrayTotalClientesAtivos),"Taxa Acertos ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)
                graficoUnico("./"+InicioCaminho+"/"+now+"-"+algoritimo+"/"+"Numero Erros- Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,arrayErros,"Numero Erros ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)
                graficoUnico("./"+InicioCaminho+"/"+now+"-"+algoritimo+"/"+"Taxa Erros- Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,CalcularTaxaArray(arrayErros,arrayTotalClientesAtivos),"Taxa Erros ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)
                graficoUnico("./"+InicioCaminho+"/"+now+"-"+algoritimo+"/"+"Numero Solicitacao Bandas- Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,arraysolicitacaoBandas,"Numero Solicitacao Bandas ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)
                graficoUnico("./"+InicioCaminho+"/"+now+"-"+algoritimo+"/"+"Taxa Solicitacao Bandas- Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,CalcularTaxaArray(arraysolicitacaoBandas,arrayTotalClientesAtivos),"Taxa Solicitacao Bandas ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)
                graficoUnico("./"+InicioCaminho+"/"+now+"-"+algoritimo+"/"+"Numero Bandas Usada - Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,arrayBandasUsada,"Numero Bandas Usada ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)
                graficoUnico("./"+InicioCaminho+"/"+now+"-"+algoritimo+"/"+"Taxa Bandas Usada - Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,CalcularTaxaArray(arrayBandasUsada,arrayTotalClientesAtivos),"Taxa Bandas Usada ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)
                graficoUnico("./"+InicioCaminho+"/"+now+"-"+algoritimo+"/"+"Total Clientes- Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,arrayTotalClientes,"Total Clientes ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)
                graficoUnico("./"+InicioCaminho+"/"+now+"-"+algoritimo+"/"+"Total Clientes Ativos- Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,arrayTotalClientesAtivos,"Total Clientes Ativos ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)
                graficoUnico("./"+InicioCaminho+"/"+now+"-"+algoritimo+"/"+"Total Pacotes na Cache- Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,arrayTotalPacotesNaCache,"Total Pacotes na Cache ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)
                graficoUnico("./"+InicioCaminho+"/"+now+"-"+algoritimo+"/"+"Tempo Execucao- Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,arrayTempoExecucao,"Tempo Execucao ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)
                graficoUnico("./"+InicioCaminho+"/"+now+"-"+algoritimo+"/"+"Tempo Distribucao- Na Cahche- Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,arrayTempoDistribucaoNaCache,"Tempo Distribucao Na Cahche ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)
                graficoUnico("./"+InicioCaminho+"/"+now+"-"+algoritimo+"/"+"Tempo Entrada Cliente- Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,arrayTempoEntradaCliente,"Tempo Entrada Cliente ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)
                graficoUnico("./"+InicioCaminho+"/"+now+"-"+algoritimo+"/"+"Tempo Ordenacao Pedidos- Requisicao- Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,arrayTempoOrdenacaoPedidosRequisicao,"Tempo Ordenacao Pedidos Requisicao ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)    
                graficoUnico("./"+InicioCaminho+"/"+now+"-"+algoritimo+"/"+"Tempo Gerar Tabela Substituicao- Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,arrayTempoGerarTabelaSubstituicao,"Tempo Gerar Tabela Substituicao ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)
                graficoUnico("./"+InicioCaminho+"/"+now+"-"+algoritimo+"/"+"Tempo Distribucao Na Requicao Atendidas- Memoria:"+memoria+" Limite Banda:"+banda+" Arquivo:"+str(arquivoLido),arrayTempo,arrayTempoDistribucaoNaRequicaoAtendidas,"Tempo Distribucao Na Requicao Atendidas ",algoritimo+" Memoria:"+memoria+" Limite Banda:"+banda)
                media=0
                contt=0
                cliente=0
                for aa in arrayTempo:
                    if(aa>5600 and aa<6600):
                        media+=arrayAcertos[aa]
                        cliente+=arrayTotalClientesAtivos[aa]
                        contt+=1
                arquivoEscrita = open("./"+InicioCaminho+"/"+now+"-"+algoritimo+"/"+"Dados da simulação.txt", "w")
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
            if(graf==2 or graf==3):
                media=0
                contt=0
                cliente=0
                for aa in arrayTempo:
                    if(aa>5600 and aa<6600):
                        media+=arrayAcertos[aa]
                        cliente+=arrayTotalClientesAtivos[aa]
                        contt+=1
                mediaPorcentagem=100*(((media/contt)/(cliente/contt)))
                if(media>0 and contt>0 and cliente>0):
                    if(algoritimo=="LFU" or algoritimo=="LRU"  or algoritimo=="FIFO" or algoritimo=="Randon" or algoritimo=="CC com janela de 0"):
                        
                        if((arquivoEscolida==1 or arquivoEscolida==2)):
                            negativo2=-4
                            #print(arquivoLeitura[negativo2:-4])
                            while arquivoLeitura[negativo2]!="-":
                                negativo2=negativo2-1
                            negativo22=negativo2-1
                            #print(((media/contt)/(cliente/contt)))
                            memoria=int((int(memoria)*0.63)/1024)
                            #print(memoria)
                            permi=False
                            if(memoria not in list(mediaDado.keys())):
                                mediaDado[memoria]={}
                                permi=True
                            mediaDado[memoria][arquivoLeitura[(negativo2+1):-4]]=mediaPorcentagem
                            if(a.verificarFimArquivo()): 
                                pasta = '../resultados/resultados/'
                                for diretorio, subpastas, arquivos in os.walk(pasta):
                                    #print(arquivos)
                                    for arquivo in arquivos:
                                        if(arquivo.find("txt")!=-1 and arquivo.find(algoritmosEscolhido)!=-1 and arquivo not in listaAquivosLista):
                                            leitura='0'
                                            a.fechar()
                                            a=manipulacao("./../resultados/resultados/"+str(arquivo))
                                            a.nomeArquivo=(arquivo.split("-"))[0]
                                            listaAquivosLista.append(arquivo)
                                            print(str(arquivo))
                                            break
                                            break
                        elif((arquivoEscolida==3 or arquivoEscolida==4 )):
                            negativo2=-4
                            #print(arquivoLeitura[negativo2:-4])
                            while arquivoLeitura[negativo2]!="-":
                                negativo2=negativo2-1
                            negativo22=negativo2-1
                            
                            permi=False
                            #int(math.ceil(((larguraBanda*1024)/0.63)/8))
                            banda=float("{:.2f}".format(float(((int(banda)*0.63)/1024)*8)))
                            if(banda not in list(mediaDado.keys())):
                                mediaDado[banda]={}
                                permi=True
                            #mediaDado[banda]=mediaPorcentagem
                            mediaDado[banda][arquivoLeitura[(negativo2+1):-4]]=mediaPorcentagem
                            if(a.verificarFimArquivo()): 
                                pasta = '../resultados/resultados14/'
                                for diretorio, subpastas, arquivos in os.walk(pasta):
                                    #print(arquivos)
                                    for arquivo in arquivos:
                                        if(arquivo.find("txt")!=-1 and arquivo.find(algoritmosEscolhido)!=-1 and arquivo not in listaAquivosLista):
                                            leitura='0'
                                            a.fechar()
                                            a=manipulacao("./../resultados/resultados14/"+str(arquivo))
                                            a.nomeArquivo=(arquivo.split("-"))[0]
                                            listaAquivosLista.append(arquivo)
                                            print(str(arquivo))
                                            break
                                            break
                            
                            
                        elif(arquivoEscolida==5 ):
                            permi=False
                            tamanhoVideo=int((int(tamanhoVideo)*0.63)/1024)
                            if(tamanhoVideo not in list(mediaDado.keys())):
                                mediaDado[tamanhoVideo]={}
                                permi=True
                            mediaDado[tamanhoVideo]=mediaPorcentagem

                        elif((arquivoEscolida==6 or arquivoEscolida==7 or arquivoEscolida==8)):
                            negativo2=-4
                            #print(arquivoLeitura[negativo2:-4])
                            while arquivoLeitura[negativo2]!="-":
                                negativo2=negativo2-1
                            negativo22=negativo2-1
                             
                            while arquivoLeitura[negativo22]!="-":
                                negativo22=negativo22-1      
                            negativo22=negativo22+1
                            permi=False
                            #print(arquivoLeitura)
                            #print(arquivoLeitura[negativo22:negativo2])
                            #print(arquivoLeitura[(negativo2+1):-4])
                            if(arquivoLeitura[negativo22:negativo2] not in list(mediaDado.keys())):
                                mediaDado[arquivoLeitura[negativo22:negativo2]]={}
                                listaPontosy[arquivoLeitura[negativo22:negativo2]]={}
                                permi=True
                            
                            #print(mediaPorcentagem,'-',int(algoritimo[negativo:len(algoritimo)]))
                            #print(mediaDado)
                            mediaDado[arquivoLeitura[negativo22:negativo2]][arquivoLeitura[(negativo2+1):-4]]=mediaPorcentagem
                            #if(permi or mediaPorcentagem>listaPontosy[arquivoLeitura[negativo22:negativo2]][arquivoLeitura[(negativo2+1):-4]]):
                            listaPontosy[arquivoLeitura[negativo22:negativo2]][arquivoLeitura[(negativo2+1):-4]]=mediaPorcentagem
                                #listaPontosJanela[arquivoLeitura[negativo2:-4]]=algoritimo[negativo:len(algoritimo)]
                            if(arquivoEscolida==7):
                                pasta = '../resultados/resultados1/'
                                for diretorio, subpastas, arquivos in os.walk(pasta):
                                    #print(arquivos)
                                    for arquivo in arquivos:
                                        if(arquivo.find("zip")!=-1 and arquivo.find("txt")!=-1 and arquivo.find(algoritmosEscolhido)!=-1 and arquivo not in listaAquivosLista):
                                            leitura='0'
                                            a.fechar()
                                            
                                            a=manipulacao("./../resultados/resultados1/"+str(arquivo))
                                            a.nomeArquivo=(arquivo.split("-"))[0]
                                            listaAquivosLista.append(arquivo)
                                            print(str(arquivo))
                                            break
                                            break
                            elif(arquivoEscolida==6):
                                pasta = './'
                                for diretorio, subpastas, arquivos in os.walk(pasta):
                                    for arquivo in arquivos:
                                        if(arquivo.find("numeroVideos")!=-1 and arquivo.find(".txt.txt")!=-1 and arquivo.find(algoritmosEscolhido)!=-1 and arquivo not in listaAquivosLista):
                                            leitura='0'
                                            a.fechar()
                                            a=manipulacao("./"+str(arquivo))
                                            a.nomeArquivo="resultadoGraficoAlgoritmoLFU6-numeroVideos"
                                            listaAquivosLista.append(arquivo)
                                            print(str(arquivo))
                                            break
                                            break
                    else:
                        negativo=-1
                        while algoritimo[negativo]!=" ":
                            negativo=negativo-1
                        if((arquivoEscolida==1 or arquivoEscolida==2) and int(algoritimo[negativo:len(algoritimo)])>0):
                            negativo2=-4
                            while arquivoLeitura[negativo2]!="-":
                                negativo2=negativo2-1
                            memoria=int((int(memoria)*0.63)/1024)
                            if(memoria not in list(mediaDado.keys())):
                                mediaDado[memoria]={}
                            if(str(algoritimo[negativo:len(algoritimo)]) not in list(mediaDado[memoria].keys())):
                                mediaDado[memoria][str(algoritimo[negativo:len(algoritimo)])]={}
                            mediaDado[memoria][str(algoritimo[negativo:len(algoritimo)])][arquivoLeitura[(negativo2+1):-4]]=mediaPorcentagem
                            if(a.verificarFimArquivo()): 
                                pasta = '../resultados/resultados/'
                                for diretorio, subpastas, arquivos in os.walk(pasta):
                                    #print(arquivos)
                                    for arquivo in arquivos:
                                        if(arquivo.find("txt")!=-1 and arquivo.find(algoritmosEscolhido)!=-1 and arquivo not in listaAquivosLista):
                                            leitura='0'
                                            a.fechar()
                                            a=manipulacao("./../resultados/resultados/"+str(arquivo))
                                            a.nomeArquivo=(arquivo.split("-"))[0]
                                            listaAquivosLista.append(arquivo)
                                            print(str(arquivo))
                                            break
                                            break    
                                
                                
                                
                        elif((arquivoEscolida==3 or arquivoEscolida==4 ) and int(algoritimo[negativo:len(algoritimo)])>0):
                            negativo2=-4
                            while arquivoLeitura[negativo2]!="-":
                                negativo2=negativo2-1
                            permi=False
                            #int(math.ceil(((larguraBanda*1024)/0.63)/8))
                            banda=float("{:.2f}".format(float(((int(banda)*0.63)/1024)*8)))
                            if(banda not in list(mediaDado.keys())):
                                mediaDado[banda]={}
                                permi=True
                            #mediaDado[banda][algoritimo[negativo:len(algoritimo)]]=mediaPorcentagem
                            # if(permi or mediaPorcentagem>listaPontosy[banda]):
                            #     listaPontosy[banda]=mediaPorcentagem
                            #     listaPontosJanela[banda]=int(algoritimo[negativo:len(algoritimo)])
                            
                            
                            if(str(algoritimo[negativo:len(algoritimo)]) not in list(mediaDado[banda].keys())):
                                mediaDado[banda][str(algoritimo[negativo:len(algoritimo)])]={}

                            mediaDado[banda][str(algoritimo[negativo:len(algoritimo)])][arquivoLeitura[(negativo2):-4]]=mediaPorcentagem
                            if(a.verificarFimArquivo()): 
                                pasta = '../resultados/resultados14/'
                                for diretorio, subpastas, arquivos in os.walk(pasta):
                                    #print(arquivos)
                                    for arquivo in arquivos:
                                        if(arquivo.find("txt")!=-1 and arquivo.find(algoritmosEscolhido)!=-1 and arquivo not in listaAquivosLista):
                                            leitura='0'
                                            a.fechar()
                                            a=manipulacao("./../resultados/resultados14/"+str(arquivo))
                                            a.nomeArquivo=(arquivo.split("-"))[0]
                                            listaAquivosLista.append(arquivo)
                                            print(str(arquivo))
                                            break
                                            break    

                            
                                
                            
                            
                        elif((arquivoEscolida==9 ) and int(algoritimo[negativo:len(algoritimo)])>0):
                            permi=False
                            #int(math.ceil(((larguraBanda*1024)/0.63)/8))
                            banda=float("{:.2f}".format(float(((int(banda)*0.63)/1024)*8)))
                            if(algoritimo[negativo:len(algoritimo)] not in list(mediaDado.keys())):
                                mediaDado[algoritimo[negativo:len(algoritimo)]]={}
                                permi=True
                            mediaDado[algoritimo[negativo:len(algoritimo)]]=mediaPorcentagem
                            if(permi or mediaPorcentagem>listaPontosy[banda]):
                                listaPontosy[algoritimo[negativo:len(algoritimo)]]=mediaPorcentagem
                                listaPontosJanela[algoritimo[negativo:len(algoritimo)]]=int(algoritimo[negativo:len(algoritimo)])
                        elif(arquivoEscolida==5 and int(algoritimo[negativo:len(algoritimo)])>0):
                            permi=False
                            tamanhoVideo=int((int(tamanhoVideo)*0.63)/1024)
                            if(tamanhoVideo not in list(mediaDado.keys())):
                                mediaDado[tamanhoVideo]={}
                                permi=True
                            mediaDado[tamanhoVideo][algoritimo[negativo:len(algoritimo)]]=mediaPorcentagem
                            if(permi or mediaPorcentagem>listaPontosy[tamanhoVideo]):
                                listaPontosy[tamanhoVideo]=mediaPorcentagem
                                listaPontosJanela[tamanhoVideo]=int(algoritimo[negativo:len(algoritimo)])
                        elif((arquivoEscolida==6 or arquivoEscolida==7 or arquivoEscolida==8) and int(algoritimo[negativo:len(algoritimo)])>0):
                            negativo2=-4
                            #print(arquivoLeitura[negativo2:-4])
                            while arquivoLeitura[negativo2]!="-":
                                negativo2=negativo2-1
                            negativo22=negativo2-1
                             
                            while arquivoLeitura[negativo22]!="-":
                                negativo22=negativo22-1      
                            negativo22=negativo22+1
                            permi=False
                            #print(arquivoLeitura)
                            if(arquivoLeitura[negativo22:negativo2] not in list(mediaDado.keys())):
                                mediaDado[arquivoLeitura[negativo22:negativo2]]={}
                                listaPontosy[arquivoLeitura[negativo22:negativo2]]={}
                                permi=True
                            if(arquivoLeitura[(negativo2+1):-4] not in list(mediaDado[arquivoLeitura[negativo22:negativo2]].keys())):
                                mediaDado[arquivoLeitura[negativo22:negativo2]][arquivoLeitura[(negativo2+1):-4]]={}
                                listaPontosy[arquivoLeitura[negativo22:negativo2]][arquivoLeitura[(negativo2+1):-4]]={}    
                            #print(mediaPorcentagem,'-',int(algoritimo[negativo:len(algoritimo)]))
                            #print(mediaDado)
                            #print(arquivoLeitura[negativo22:negativo2])
                            #print(arquivoLeitura[(negativo2+1):-4])
                            #print(algoritimo[(negativo+1):len(algoritimo)])
                            
                            mediaDado[arquivoLeitura[negativo22:negativo2]][arquivoLeitura[(negativo2+1):-4]][algoritimo[(negativo+1):len(algoritimo)]]=mediaPorcentagem
                            #if(permi or mediaPorcentagem>listaPontosy[arquivoLeitura[negativo22:negativo2]][arquivoLeitura[negativo2:-4]]):
                            #    listaPontosy[arquivoLeitura[negativo22:negativo2]][arquivoLeitura[negativo2:-4]][algoritimo[negativo:len(algoritimo)]]=mediaPorcentagem
                            #    listaPontosJanela[arquivoLeitura[negativo2:-4]]=algoritimo[negativo:len(algoritimo)]
                            #print(len(mediaDado[arquivoLeitura[negativo22:negativo2]][arquivoLeitura[(negativo2+1):-4]]))
                            if(a.verificarFimArquivo()): 
                                if(arquivoEscolida==8):
                                    pasta = './../resultados/resultados8/'
                                    for diretorio, subpastas, arquivos in os.walk(pasta):
                                        for arquivo in arquivos:
                                            if(arquivo.find("poisson")!=-1 and arquivo.find("txt")!=-1 and arquivo.find(algoritmosEscolhido)!=-1 and arquivo not in listaAquivosLista):
                                                leitura='0'
                                                a.fechar()
                                                a=manipulacao("./../resultados/resultados8/"+str(arquivo))
                                                a.nomeArquivo=(arquivo.split("-"))[0]
                                                listaAquivosLista.append(arquivo)
                                                print(str(arquivo))
                                                break
                                                break
                                elif(arquivoEscolida==7):
                                    pasta = './../resultados/resultados3/'
                                    for diretorio, subpastas, arquivos in os.walk(pasta):
                                        for arquivo in arquivos:
                                            if(arquivo.find("zip")!=-1 and arquivo.find("txt")!=-1 and arquivo.find(algoritmosEscolhido)!=-1 and arquivo not in listaAquivosLista):
                                                leitura='0'
                                                a.fechar()
                                                a=manipulacao("./../resultados/resultados3/"+str(arquivo))
                                                a.nomeArquivo=(arquivo.split("-"))[0]
                                                listaAquivosLista.append(arquivo)
                                                print(str(arquivo))
                                                break
                                                break
                                elif(arquivoEscolida==6):
                                    pasta = './'
                                    for diretorio, subpastas, arquivos in os.walk(pasta):
                                        #print(str(arquivos))
                                        for arquivo in arquivos:
                                            #print(str(arquivo))
                                            if(arquivo.find("numeroVideos")!=-1 and arquivo.find("txt")!=-1 and arquivo.find(algoritmosEscolhido)!=-1 and arquivo not in listaAquivosLista):
                                                leitura='0'
                                                a.fechar()
                                                a=manipulacao("./"+str(arquivo))
                                                a.nomeArquivo="resultadoGrafico6-numeroVideos"
                                                listaAquivosLista.append(arquivo)
                                                print(str(arquivo))
                                                break
                                                break
if(graf==2 or graf==3):
    #print("./"+InicioCaminho+"/"+a.nomeArquivo)
    #print(a.nomeArquivo)
    os.mkdir("./"+InicioCaminho+"/"+a.nomeArquivo)
    algorimos=""
    if(arquivoEscolida==1):
        nomeGraf="Variação da memoria 1GB a 25 GB saltos de 1GB"
        eixox="Memoria(GB)"
    elif(arquivoEscolida==2):
        nomeGraf="Variação da memoria 25GB a 50 GB saltos de 1GB"
        eixox="Memoria(GB)"
    elif(arquivoEscolida==3):
        nomeGraf="Varia largura banda Gbs em saltos 0.2Gbs "
        eixox="Lagura de Banda (Blocos)"
    elif(arquivoEscolida==4):
        nomeGraf="Varia lagura banda 1000 a 25000 blocos saltos de 1000 Blocos"
        eixox="Largura de Banda (Blocos)"
    elif(arquivoEscolida==5):
        nomeGraf="Varia tamanho video 1000 a 10000 blocos saltos de 1000 Blocos"
        eixox="Largura do Video (Blocos)"
    elif(arquivoEscolida==6):
        nomeGraf="Varia numerero video 50 a 200  pulos 10 videos:"
        eixox="Numero de videos"
    elif(arquivoEscolida==7):
        nomeGraf="Varia video 0,25 a 1  pulos 0,25"
        eixox="ZIFP"
    elif(arquivoEscolida==8):
        nomeGraf="Varia intevalo de chegada 1s a 10s pulos 1s"
        eixox="intevalo de chegada dos videos (Segundos)"
        
    if(algoritimo!="LFU" and algoritimo!="LRU"  and algoritimo!="FIFO" and algoritimo!="Randon" and algoritimo!="CC com janela de 0"):
    #list(listaPontosy.keys()),list(listaPontosy.values()),list(listaPontosJanela.values())
        if(arquivoEscolida==6 or arquivoEscolida==7 or arquivoEscolida==8):
            listax=[]
            listay=[]
            listaz=[]
            for key, value in mediaDado.items():
                listazip={}
                for key2, value2 in value['0'].items():
                    contador=0
                    while(contador<3):
                        print(str(contador)+"-"+str(key2)+"--"+str(value[str(contador)]))
                        print(str(contador)+"-"+str(key2)+"--"+str(value[str(contador)][str(key2)]))
                        if(str(key2) in listazip):
                            listazip[str(key2)]+=value[str(contador)][str(key2)]
                        else:
                            listazip[str(key2)]=value[str(contador)][str(key2)]
                        contador+=1
                maior=0
                janela=0
                for key2, value2 in listazip.items():
                    listazip[key2]=(value2/3)
                    if(maior<(value2/3)):
                        maior=value2/3
                        janela=key2
                listax.append(key)
                listay.append(maior)
                listaz.append(janela)
            #listax=(list(listaPontosy.keys()))
            #listay=(list(listaPontosy.values()))
            #listaz=(list(listaPontosJanela.values()))
            exchanges = True
            passnum = len(listax)-1
            while passnum > 0 and exchanges:
                exchanges = False
                for i in range(passnum):
                    if(float(listax[i])>float(listax[i+1])):
                        print("organizar")
                        exchanges = True
                        temp = listax[i]
                        listax[i] = listax[i+1]
                        listax[i+1] = temp
                        temp = listay[i]
                        listay[i] = listay[i+1]
                        listay[i+1] = temp
                        temp = listaz[i]
                        listaz[i] = listaz[i+1]
                        listaz[i+1] = temp
                passnum = passnum-1
            arquivoEscrita = open("./"+InicioCaminho+"/"+a.nomeArquivo+nomeGraf+".txt", "w")
            arquivoEscrita.write('algoritmo.append('+str(algoritimo)+")")
            arquivoEscrita.write('\n')
            arquivoEscrita.write('listaPontosx.append('+str(listax)+")")
            arquivoEscrita.write('\n')
            arquivoEscrita.write('listaPontosy.append('+str(listay)+")")
            arquivoEscrita.write('\n')
            arquivoEscrita.write('listaPontosJanela.append('+str(listaz)+")")
            arquivoEscrita.write('\n')
            arquivoEscrita.write('listaPontosyToad.doubleclick.netdoas='+str(listaPontosy))
            arquivoEscrita.write('\n')
            arquivoEscrita.write('listaPontosJanela='+str(listaPontosJanela))
            arquivoEscrita.write('\n')
            arquivoEscrita.write('media='+str(mediaDado))
            arquivoEscrita.write('\n')
            arquivoEscrita.close()            
            #GraficoGerar=graficoConjuntoResultados("./"+InicioCaminho+"/"+a.nomeArquivo+nomeGraf,listax,listay,listaz,nomeGraf,algorimos,eixox)
        else:
            arquivoEscrita = open("./"+InicioCaminho+"/"+a.nomeArquivo+nomeGraf+".txt", "w")
            listaMedia={}
            listax=[]
            listay=[]
            listaz=[]
            # for key, value in mediaDado.items():
            #     listazip={}
            #     for key2, value2 in value.items():
            #         contador=0
            #         while(contador<3):
            #             print(str(contador)+"-"+str(key2)+"--"+str(value[str(contador)]))
            #             print(str(contador)+"-"+str(key2)+"--"+str(value[str(contador)][str(key2)]))
            #             if(str(key2) in listazip):
            #                 listazip[str(key2)]+=value[str(contador)][str(key2)]
            #             else:
            #                 listazip[str(key2)]=value[str(contador)][str(key2)]
            #             contador+=1
            #     maior=0
            #     janela=0
            #     for key2, value2 in listazip.items():
            #         listazip[key2]=(value2/3)
            #         if(maior<(value2/3)):
            #             maior=value2/3
            #             janela=key2
            #     listax.append(key)
            #     listay.append(maior)
            #     listaz.append(janela)   
            #arquivoEscrita.write('algoritmo.append('+str(algoritimo)+")")
            arquivoEscrita.write('\n')
            # arquivoEscrita.write('listaPontosx.append('+str(list(listaMedia.keys()))+")")
            # arquivoEscrita.write('\n')
            # arquivoEscrita.write('listaPontosy.append('+str(list(listaMedia.values()))+")")
            arquivoEscrita.write('\n')
            arquivoEscrita.write("listaPontosJanela.append([])")
            arquivoEscrita.write('\n')
            arquivoEscrita.write('media='+str(mediaDado))
            arquivoEscrita.write('\n')
            arquivoEscrita.close()
            #GraficoGerar=graficoConjuntoResultados("./"+InicioCaminho+"/"+a.nomeArquivo+nomeGraf,list(listaPontosy.keys()),list(listaPontosy.values()),list(listaPontosJanela.values()),nomeGraf,algorimos,eixox)
    else:
        if(arquivoEscolida==6 or arquivoEscolida==7 or arquivoEscolida==8):
            print("qqqqqqqqqqqqqqqqqqqqqqqq")
            listax=(list(listaPontosy.keys()))
            listay=(list(listaPontosy.values()))
            
            listaz=(list(listaPontosJanela.values()))
            exchanges = True
            passnum = len(listax)-1
            while passnum > 0 and exchanges:
                exchanges = False
                for i in range(passnum):
                    if(float(listax[i])>float(listax[i+1])):
                        print("organizar")
                        print(listax)
                        print("y")
                        print(listay)
                        print("z")
                        print(listaz)
                        exchanges = True
                        temp = listax[i]
                        listax[i] = listax[i+1]
                        listax[i+1] = temp
                        temp = listay[i]
                        listay[i] = listay[i+1]
                        listay[i+1] = temp
                        #temp = listaz[i]
                        #listaz[i] = listaz[i+1]
                        #listaz[i+1] = temp
                passnum = passnum-1
            arquivoEscrita = open("./"+InicioCaminho+"/"+a.nomeArquivo+nomeGraf+".txt", "w")
            #arquivoEscrita.write('listaPontosx='+str(listax))
            #arquivoEscrita.write('\n')
            #arquivoEscrita.write('listaPontosy='+str(listay))
            #arquivoEscrita.write('\n')
            listayMedia={}
            for key1,value in enumerate(listay):
                media=0
                divisor=0
                for key2 in value:
                    media+=value[key2]
                    divisor+=1
                valorMedir=(media/divisor)
                listayMedia[key1]=valorMedir
                
            arquivoEscrita.write('algoritmo.append('+str(algoritimo)+")")
            arquivoEscrita.write('\n')
            arquivoEscrita.write('listaPontosx.append('+str(listax)+")")
            arquivoEscrita.write('\n')
            arquivoEscrita.write('listaPontosy.append('+str(listayMedia)+")")
            arquivoEscrita.write('\n')
            arquivoEscrita.write('listaPontosJanela.append([])')    
            arquivoEscrita.write('listaPontosMediay='+str(listayMedia))
            arquivoEscrita.write('\n')
            arquivoEscrita.write('listaPontosJanela='+str(listaz))
            arquivoEscrita.write('\n')
            arquivoEscrita.write('listaPontosyTodoas='+str(listaPontosy))
            arquivoEscrita.write('\n')
            arquivoEscrita.write('listaPontosJanela='+str(listaPontosJanela))
            arquivoEscrita.write('\n')
            arquivoEscrita.write('media='+str(mediaDado))
            arquivoEscrita.write('\n')
            arquivoEscrita.close()            
            #GraficoGerar=graficoConjuntoDadosxy("./"+InicioCaminho+"/"+a.nomeArquivo+nomeGraf,listax,listay,nomeGraf,algorimos,eixox)
        else:
            arquivoEscrita = open("./"+InicioCaminho+"/"+a.nomeArquivo+nomeGraf+".txt", "w")
            listaMedia={}
            for key, value in mediaDado.items():
                contador=0
                total=0
                for key2, value2 in value.items():
                    contador+=1
                    total+=value2
                listaMedia[key]=(total/contador);  
            arquivoEscrita.write('algoritmo.append('+str(algoritimo)+")")
            arquivoEscrita.write('\n')
            arquivoEscrita.write('listaPontosx.append('+str(list(listaMedia.keys()))+")")
            arquivoEscrita.write('\n')
            arquivoEscrita.write('listaPontosy.append('+str(list(listaMedia.values()))+")")
            arquivoEscrita.write('\n')
            arquivoEscrita.write("listaPontosJanela.append([])")
            arquivoEscrita.write('\n')
            arquivoEscrita.write('media='+str(mediaDado))
            arquivoEscrita.write('\n')
            arquivoEscrita.close()
            #GraficoGerar=graficoConjuntoDadosxy("./"+InicioCaminho+"/"+a.nomeArquivo+nomeGraf,list(mediaDado.keys()),list(mediaDado.values()),nomeGraf,algorimos,eixox)
        
    # print("1-Varia memoria 1 a 25 GB  pulos 1GB")
    #     print("2-Varia memoria 25 a 50 GB pulos 1GB ")
    #     print("3-Varia banda 100 a 1000 blocos pulos 50 blocos")
    #     print("4-Varia banda 1000 a 25000 blocos  pulos 1000")
    #     print("5-Varia video 1000 a 10000GB  pulos 1GB  Operacao:")
    #     print("6-Varia numerero video 50 a 200  pulos 10 videos:")
    #     print("7-Varia video 0,25 a 1  pulos 0,25  :")
    #     print("8-Varia intevalo de chegada 1s a 10s pulos 1s  Operacao:")
          #self.fig, self.ax = self.plt.subplots()            
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
