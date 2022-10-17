class Filme:
    def __init__ (self,filme,tamanhoFilme):
        self.idFilme=filme
        self.blocos={}
        self.blocoMemoria={}
        self.clientes={}
        self.numeroClientes=0
        self.endNos={}
        self.tamanhoFilme=tamanhoFilme
        self.classificacao={} 
        self.tempoClassificacao={} 
    def __repr__(self):
        #return 'Filme:'+str(self.idFilme)+" Bloco:"+str(self.blocos)+" Bloco Memoria:"+str(self.blocoMemoria)+" Numero Cliente:"+str(self.numeroClientes)+" Cliente:"+str(len(self.clientes))
        return self.clientes
        #for  cliente in self.clientes.items():
        #    print(cliente)
    def verificar(self,quantidadeNaoEncontrado,log):
        for idbloco in list(self.blocos.keys()):
            if(self.blocos.get(idbloco)==None):
                log.escreverVerificar("Bloco não lista bloc")
                log.escreverVerificar(idbloco, self.idFilme)
                #breakpoint()
            if(self.blocoMemoria.get(idbloco)==None):
                log.escreverVerificar("Bloco não lista blocos na memoria")
                log.escreverVerificar(idbloco, self.idFilme)
                #breakpoint()
            if(self.endNos.get(idbloco)==None):
                log.escreverVerificar("Bloco não na arvores")
                log.escreverVerificar(idbloco, self.idFilme)
                quantidadeNaoEncontrado+=1
                #breakpoint()
        if(len(self.blocos)!=len(self.blocoMemoria)):
            log.escreverVerificar("Tamanhos lista diferentes")
            log.escreverVerificar("Blocos",len(self.blocos))
            log.escreverVerificar("Blocos Memoria",len(self.blocoMemoria))
            log.escreverVerificar("End Nos",len(self.endNos))
            #breakpoint()
        return quantidadeNaoEncontrado
