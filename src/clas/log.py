from datetime import datetime
class Log:
    def __init__(self,inputEntrada,*debug):
        #now = str(datetime.now()).replace(":","")
        #self.arquivo=open('../resultados/logs/nome-do-arquivo'+str(inputEntrada)+str(now)+'.txt', 'a')
        #self.arquivoTempo=open('../resultados/logs/tempoExecucao'+str(inputEntrada)+str(now)+'.txt', 'a')
        #self.arquivoTempoSimulacao=open('../resultados/logs/tempoDasSimulacoes'+str(inputEntrada)+str(now)+'.txt', 'a')
        #self.logs=open('../resultados/logs/'+str(inputEntrada)+str(now)+'.txt', 'w')
        self.debug=debug
        self.verificar=[False,False,False,False,False,False,False]
        self.printTela=False
        self.tempo=0
        
    def setTempo(self,tempo):
        self.tempo=tempo
    #tem todos log 
    def escreverVerificar(self,*escrita):
        #self.arquivo.write(str(escrita)+"\n");
        if(self.printTela):
            print(escrita)
    def escreverVerificarTempo(self,tempo,*escrita):
        if(self.tempo==tempo):
            aaaa=0
            #self.arquivo.write(str(escrita)+"\n");
            #print(escrita)        
            
    def escreverVerificarSimulacao(self,*escrita):
        #self.arquivoTempoSimulacao.write(str(escrita)+"\n");
        aaaa=0
        #print(escrita)
    #escrve em todos os arquivos de logs
    def escreverTodos(self,*escrita):
        self.escreverVerificar(escrita)
        self.escreverTempo(escrita)
        self.escrever(escrita)
        self.escreverVerificarSimulacao(escrita)
        
    #log mais filtrados
    def escrever(self,*escrita):
        self.escreverVerificar(escrita)
        #self.logs.write(str(escrita)+"\n");
        
    #salva o tempo da simulação    
    def escreverTempo(self,*escrita):
        #self.arquivoTempo.write(str(escrita)+"\n");
        aaaa=0

    def fechar(self):
        aaaa=0
        #self.arquivo.close()
       # self.logs.close()
       # self.arquivoTempo.close()
       # self.arquivoTempoSimulacao.close()
    def debugPersoanalizado(self,listaFilmes,arvore,memoria,veificacao,local):
        if(self.verificar[veificacao]):
            self.escreverVerificar(self.tempo)
            if(self.tempo>0):
                quant=0
                quantidadeNaoEncontrado=0
                self.escreverVerificar("Verificação 2-2")
                for idFilme in listaFilmes:
                    quantidadeNaoEncontrado=listaFilmes[idFilme].verificar(quantidadeNaoEncontrado,self)
                    quant+=len(listaFilmes[idFilme].blocos)
                quantidade={}
                quantidade['quantidade']=0
                arvore.quatidadeItems(arvore.root,quantidade)
                self.escreverVerificar([veificacao,"Local:",local,"Diferentes ",quantidade['quantidade'],len(memoria),quantidadeNaoEncontrado])
                arvore.inOrderLog(arvore.root,self)
                self.escreverVerificar(arvore.root)
                #if((quantidade['quantidade'])!=len(memoria) or quant!=len(memoria)):        

                if((quantidade['quantidade'])!=len(memoria)):        
                    print([veificacao,"Local:",local,"Diferentes ",quantidade['quantidade'],len(memoria),quantidadeNaoEncontrado])
                    breakpoint()
