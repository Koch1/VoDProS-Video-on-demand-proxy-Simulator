class No:
    def __init__(self,key,idBloco,idFilme,idM, dirr=None, esq=None):
        self.item = key
        #self.blocos=[]
        #self.blocos.append({'idFilme':idFilme,'idBloco':idBloco, 'memoria':idM})
        self.blocosChave={}
        self.blocosChave[str(idFilme)+'-'+str(idBloco)]={'idFilme':idFilme,'idBloco':idBloco, 'memoria':idM}
        self.dir = dirr
        self.esq = esq
        self.pai=None
        self.filho_esq=False
        
    def __repr__(self):
        return (str(self.item)+("("+str(len(self.blocosChave))+")"))