class ArvoreEspera:
    def __init__(self):
        #self.root = No(None,None,None,None,None,None)
        self.root = None

    def inserir(self, novo):
        #novo = No(v,idFilme,idBloco,idM,None,None) # cria um novo Nó
        if self.root == None:
            self.root = novo
            return novo
        else: # se nao for a raiz
            atual = self.root
            while True:
                anterior = atual
                if(novo.item==atual.item):
                    if(novo.item2==atual.item2):
                        if(novo.item3==atual.item3):
                            atual = atual.dir
                            if atual == None:
                                novo.pai=anterior
                                anterior.esq = novo
                                return novo
                        elif novo.item3 <= atual.item3: # ir para esquerda
                            atual = atual.esq
                            if atual == None:
                                novo.pai=anterior
                                novo.filho_esq=True
                                anterior.esq = novo
                                return novo
                            # fim da condição ir a esquerda
                        else: # ir para direita
                            atual = atual.dir
                            if atual == None:
                                novo.pai=anterior
                                anterior.dir = novo
                                return novo
                        # fim da condição ir a direita
                
                    elif novo.item2 <= atual.item2: # ir para esquerda
                        atual = atual.esq
                        if atual == None:
                            novo.pai=anterior
                            novo.filho_esq=True
                            anterior.esq = novo
                            return novo
                        # fim da condição ir a esquerda
                    else: # ir para direita
                        atual = atual.dir
                        if atual == None:
                            novo.pai=anterior
                            anterior.dir = novo
                            return novo
                        # fim da condição ir a direita
                
                elif novo.item <= atual.item: # ir para esquerda
                    atual = atual.esq
                    if atual == None:
                        novo.pai=anterior
                        novo.filho_esq=True
                        anterior.esq = novo
                        return novo
                    # fim da condição ir a esquerda
                else: # ir para direita
                    atual = atual.dir
                    if atual == None:
                        novo.pai=anterior
                        anterior.dir = novo
                        return novo
                    # fim da condição ir a direita

    

    
    
    def ordenadoValore(self,pai,filho_esq, atual,lista,quantidade):
        if atual != None and quantidade>len(lista):
            self.ordenadoValore(atual,False ,atual.dir,lista,quantidade)
            if(len(atual.blocosChave)<=(quantidade-len(lista))):
                #print("Atualizar")
                #print(atual.blocosChave)
                #lista.extend(atual.blocosChave)
                
                lista.update(atual.blocosChave)
            else:
                return 0
            self.ordenadoValore(atual,True ,atual.esq,lista,quantidade)

    def inOrder(self, atual):
        if atual != None:
            self.inOrder(atual.esq)
            # log.escrever(atual)
            print(atual,end=" ")
            # if(atual.item<0):
            #     breakpoint()
            self.inOrder(atual.dir)
            
    def preOrder(self, atual):
        if atual != None:
            print(atual.item,end=" ")
            self.preOrder(atual.esq)
            self.preOrder(atual.dir)
    
    def posOrder(self, atual):
        if atual != None:
            self.posOrder(atual.esq)
            self.posOrder(atual.dir)
            print(atual.item,end=" ")

    def altura(self, atual):
        if atual == None or atual.esq == None and atual.dir == None:
            return 0
        else:
            if self.altura(atual.esq) > self.altura(atual.dir):
                return  1 + self.altura(atual.esq) 
            else:
                return  1 + self.altura(atual.dir) 
    def folhas(self, atual):
        if atual == None:
            return 0
        if atual.esq == None and atual.dir == None:
            return 1
        return self.folhas(atual.esq) + self.folhas(atual.dir)

    def contarNos(self, atual):
        if atual == None:
            return 0
        else:
            return  1 + self.contarNos(atual.esq) + self.contarNos(atual.dir)

    def minn(self):
        atual = self.root
        anterior = None
        while atual != None:
            anterior = atual
            atual = atual.esq
        return anterior

    def maxx(self):
        atual = self.root
        anterior = None
        while atual != None:
            anterior = atual
            atual = atual.dir
        return anterior

    def caminhar(self):
        print(" Exibindo em ordem: ",end="")
        self.inOrder(self.root)
        print("\n Exibindo em pos-ordem: ",end="")
        self.posOrder(self.root)
        print("\n Exibindo em pre-ordem: ",end="")
        self.preOrder(self.root)
        print("\n Altura da arvore: %d" %(self.altura(self.root)))
        print(" Quantidade de folhas: %d"  %(self.folhas(self.root)))
        print(" Quantidade de Nós: %d" %(self.contarNos(self.root)))
        if self.root != None: # se arvore nao esta vazia
            print(" Valor minimo: %d" %(self.minn().item))
            print(" Valor maximo: %d" %(self.maxx().item))