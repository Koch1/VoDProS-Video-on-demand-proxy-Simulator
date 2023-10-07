from classes.cliente import Cliente

class ManipulacaoArquivo:
    def __init__(self,arquivoLeitura,grafico,alg):
        print(arquivoLeitura)
        self.nomeArquivoLer=open(arquivoLeitura,'r')
        self.ponteiro=0
        
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
        nomeArquivo.close()
    
    def leituraLinha(self):
        leitura=self.nomeArquivoLer.readline()
        self.ponteiro=self.nomeArquivoLer.tell()
        return leitura

    def novoClienteLido(self,tamanhoVideo):
        cli=self.leituraLinha()
        novoCliente=cli.replace('\n', '').split(' ')
        if(len(novoCliente)>1):
            return Cliente(novoCliente[0],novoCliente[2],novoCliente[1],-1,tamanhoVideo)
        else:
            return 0;


        
        

