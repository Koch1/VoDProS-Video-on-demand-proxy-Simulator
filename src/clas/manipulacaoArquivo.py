from clas.cliente import Cliente
import pickle
import os
class ManipulacaoArquivo:
    def __init__(self,arquivoLeitura,grafico,alg):
        print(arquivoLeitura)
        self.nomeArquivoLer=open(arquivoLeitura,'r')
        self.ponteiro=0
        self.caminho="./RAM/"+str(alg)+"/"+str(grafico.arquivoLeitura)+"/"+str(grafico.memoria)+"/"+str(grafico.banda)+"/"+str(grafico.tamanhovideo)
        
    def escritaResult(self,resultado):
        nomeArquivo=open ('resultado', 'a')
        nomeArquivo.write('Algoritimo:'+(str(resultado.nomeAlgoritimo)))
        nomeArquivo.write('\n')
        nomeArquivo.write('Arquivo Leitura: '+(str(resultado.arquivoLeitura)))
        nomeArquivo.write('\n')
        nomeArquivo.write('Arquivo Acertos: '+(str(resultado.acertos)))
        nomeArquivo.write('\n')
        nomeArquivo.write('Arquivo Erros: '+(str(resultado.erros)))
        nomeArquivo.write('\n')
        nomeArquivo.write('Total Clientes: '+(str(resultado.totalClientes)))
        nomeArquivo.write('\n')
        nomeArquivo.write('Total Pacotes Reais: '+(str(resultado.totalPacotesEntregues)))
        nomeArquivo.write('\n')
        nomeArquivo.write('\n')
        arquiv.close()
    
    def leituraLinha(self):
        leitura=self.nomeArquivoLer.readline()
        self.ponteiro=self.nomeArquivoLer.tell()
        return leitura
    
    def carregarMemoria(self):
        arquivo = open(self.caminho+'/memoria', "rb")
        memoria= pickle.load(arquivo)
        arquivo.close()
        return memoria
    def carregarInstanteTempo(self):
        arquivo = open(self.caminho+'/instanteTempo', "rb")
        instanteTempo= pickle.load(arquivo)
        arquivo.close()
        arquivo = open(self.caminho+'/ponteiroLeitura', "rb")
        self.ponteiro= pickle.load(arquivo)
        self.nomeArquivoLer.seek(self.ponteiro)
        arquivo.close()
        return instanteTempo
    def carregarNovoCliente(self):
        arquivo = open(self.caminho+'/novoCliente', "rb")
        novoCliente= pickle.load(arquivo)
        arquivo.close()
        return novoCliente
    def carregarListaClientes(self):
        arquivo = open(self.caminho+'/listaClientes', "rb")
        instanteTempo= pickle.load(arquivo)
        arquivo.close()
        return instanteTempo
    def carregarListaFilmes(self):
        arquivo = open(self.caminho+'/listaFilmes', "rb")
        listaFilmes= pickle.load(arquivo)
        arquivo.close()
        return listaFilmes
    def carregarResult(self):
        arquivo = open(self.caminho+'/result', "rb")
        result= pickle.load(arquivo)
        arquivo.close()
        return result
    def carregarInicio(self):
        arquivo = open(self.caminho+'/inicio', "rb")
        inicio= pickle.load(arquivo)
        arquivo.close()
        return inicio
    def carregarGrafico(self):
        arquivo = open(self.caminho+'/grafico', "rb")
        grafico= pickle.load(arquivo)
        arquivo.close()
        return grafico
        
    def salvarLocal(self,memoria,instanteTempo,novoCliente,listaClientes,listaFilmes,result,inicio,grafico):
        os.makedirs(self.caminho,exist_ok=True)
        nomeArquivo=open (self.caminho+'/memoria','wb')
        pickle.dump(memoria, nomeArquivo)
        nomeArquivo.close()
        nomeArquivo=open (self.caminho+'/instanteTempo','wb')
        pickle.dump(instanteTempo, nomeArquivo)
        nomeArquivo.close()
        nomeArquivo=open (self.caminho+'/ponteiroLeitura','wb')
        pickle.dump(self.ponteiro, nomeArquivo)
        nomeArquivo.close()
        nomeArquivo=open (self.caminho+'/novoCliente','wb')
        pickle.dump(novoCliente, nomeArquivo)
        nomeArquivo.close()
        nomeArquivo=open (self.caminho+'/listaClientes','wb')
        pickle.dump(listaClientes, nomeArquivo)
        nomeArquivo.close()
        nomeArquivo=open (self.caminho+'/listaFilmes','wb')
        pickle.dump(listaFilmes, nomeArquivo)
        nomeArquivo.close()
        nomeArquivo=open (self.caminho+'/result','wb')
        pickle.dump(result, nomeArquivo)
        nomeArquivo.close()
        nomeArquivo=open (self.caminho+'/inicio','wb')
        pickle.dump(inicio, nomeArquivo)
        nomeArquivo.close()
        nomeArquivo=open (self.caminho+'/grafico','wb')
        pickle.dump(grafico, nomeArquivo)
        nomeArquivo.close()
    


    def novoClienteLido(self,tamanhoVideo):
        cli=self.leituraLinha()
        novoCliente=cli.replace('\n', '').split(' ')
        if(len(novoCliente)>1):
            return Cliente(novoCliente[0],novoCliente[2],novoCliente[1],-1,tamanhoVideo)
        else:
            return 0;

    def escritaResultadoContineo(self,resultado):
        nomeArquivo=open ('resultado'+resultado.nomeAlgoritimo+resultado.arquivoLeitura, 'a')
        nomeArquivo.write((str(resultado.acertos)))
        nomeArquivo.write(',')
        nomeArquivo.write((str(resultado.erros)))
        nomeArquivo.write(',')
        nomeArquivo.write((str(resultado.totalClientes)))
        nomeArquivo.write(',')
        nomeArquivo.write((str(resultado.totalPacotesEntregues)))
        nomeArquivo.write(',')
        nomeArquivo.write((str(resultado.totalClientesAtivos)))
        nomeArquivo.write('\n')
        
        
        
    def abrindoSalvamentoMemoria(self):
        os.makedirs(self.caminho,exist_ok=True)
        self.memoriaSalva=open (self.caminho+'/memoriaSalvaPorInstante','w')
    def salvandoMemoria(self,memoria):
        self.memoriaSalva.write((str(memoria)))
        self.memoriaSalva.write('\n')
    def FechandoAbrindoSalvamentoMemoria(self):
        self.memoriaSalva.close()