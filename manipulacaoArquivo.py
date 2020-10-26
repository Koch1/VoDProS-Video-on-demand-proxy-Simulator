from cliente import Cliente

class ManipulacaoArquivo:
    def __init__(self,arquivoLeitura):
        self.nomeArquivoLer=open (arquivoLeitura, 'r')
        
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
        return self.nomeArquivoLer.readline()

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



    