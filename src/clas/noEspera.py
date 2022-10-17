class NoEspera:
    def __init__(self, key,key2,key3,pacote,dirr=None, esq=None):
        self.item =key
        self.item2=key2
        self.item3=key3
        self.blocosChave=pacote
        self.dir = dirr
        self.esq = esq
        self.pai=None
        self.filho_esq=False