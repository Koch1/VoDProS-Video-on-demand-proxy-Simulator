class Arvore:
    def __init__(self,log):
        #self.root = No(None,None,None,None,None,None)
        self.root = None
        self.log=log

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
                    for ids in novo.blocosChave:
                        atual.blocosChave[ids]=novo.blocosChave[ids];
                    #atual.blocosChave.update(novo.blocosChave);
                    #atual.blocosChave.update(novo.blocosChave)
                    return atual
                elif novo.item < atual.item: # ir para esquerda
                    atual = atual.esq
                    if atual == None:
                        novo.pai=anterior
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

    def buscar(self, chave):
        if self.root == None:
            return None # se arvore vazia
        atual = self.root # começa a procurar desde raiz
        while atual.item != chave: # enquanto nao encontrou
            if chave < atual.item:
                atual = atual.esq # caminha para esquerda
            else:
                atual = atual.dir # caminha para direita
            if atual == None:
                return None # encontrou uma folha -> sai
        return atual  # terminou o laço while e chegou aqui é pq encontrou item    

    # O sucessor é o Nó mais a esquerda da subarvore a direita do No que foi passado como parametro do metodo
    def nosucessor(self, apaga): # O parametro é a referencia para o No que deseja-se apagar
        paidosucessor=apaga
        sucessor=apaga
        atual = apaga.dir # vai para a subarvore a direita
        while atual != None: # enquanto nao chegar no Nó mais a esquerda
            paidosucessor = sucessor
            sucessor = atual
            atual = atual.esq # caminha para a esquerda
        # *********************************************************************************
        # quando sair do while "sucessor" será o Nó mais a esquerda da subarvore a direita
        # "paidosucessor" será o o pai de sucessor e "apaga" o Nó que deverá ser eliminado
        # *********************************************************************************
        if sucessor != apaga.dir: # se sucessor nao é o filho a direita do Nó que deverá ser eliminado
            paidosucessor.esq = sucessor.dir # pai herda os filhos do sucessor que sempre serão a direita
            if(sucessor.dir!=None):
                sucessor.dir.pai=paidosucessor
            # lembrando que o sucessor nunca poderá ter filhos a esquerda, pois, ele sempre será o
            # Nó mais a esquerda da subarvore a direita do Nó apaga.
            # lembrando também que sucessor sempre será o filho a esquerda do pai
            sucessor.dir = apaga.dir # guardando a referencia a direita do sucessor para 
            apaga.dir.pai=sucessor
            # quando ele assumir a posição correta na arvore
        return sucessor

    def remover(self, v):
        if self.root == None:
            return False # se arvore vazia
        atual = self.root
        pai = self.root
        filho_esq = True
         # ****** Buscando o valor **********
        while atual.item != v: # enquanto nao encontrou
            pai = atual
            if v < atual.item: # caminha para esquerda
                atual = atual.esq
                filho_esq = True # é filho a esquerda? sim
            else: # caminha para direita
                atual = atual.dir 
                filho_esq = False # é filho a esquerda? NAO
            if atual == None:
                return False # encontrou uma folha -> sai
        # fim laço while de busca do valor

         # **************************************************************
        # se chegou aqui quer dizer que encontrou o valor (v)
        # "atual": contem a referencia ao No a ser eliminado
        # "pai": contem a referencia para o pai do No a ser eliminado
        # "filho_esq": é verdadeiro se atual é filho a esquerda do pai
         # **************************************************************

        # Se nao possui nenhum filho (é uma folha), elimine-o
        if atual.esq == None and atual.dir == None:
            if atual == self.root:
                self.root = None # se raiz
            else:
                if filho_esq:
                    pai.esq =  None # se for filho a esquerda do pai
                else:
                    pai.dir = None # se for filho a direita do pai

        # Se é pai e nao possui um filho a direita, substitui pela subarvore a direita
        elif atual.dir == None:
            if atual == self.root:
                self.root = atual.esq # se raiz
            else:
                if filho_esq:
                    pai.esq = atual.esq # se for filho a esquerda do pai
                else:
                    pai.dir = atual.esq # se for filho a direita do pai
        # Se é pai e nao possui um filho a esquerda, substitui pela subarvore a esquerda
        elif atual.esq == None:
            if atual == self.root:
                self.root = atual.dir # se raiz
            else:
                if filho_esq:
                    pai.esq = atual.dir # se for filho a esquerda do pai
                else:
                    pai.dir = atual.dir # se for  filho a direita do pai

        # Se possui mais de um filho, se for um avô ou outro grau maior de parentesco
        else:
            sucessor = self.nosucessor(atual)
            # Usando sucessor que seria o Nó mais a esquerda da subarvore a direita do No que deseja-se remover
            if atual == self.root:
                self.root = sucessor # se raiz
            else:
                if filho_esq:
                    pai.esq = sucessor # se for filho a esquerda do pai
                else:
                    pai.dir = sucessor # se for filho a direita do pai
            sucessor.esq = atual.esq # acertando o ponteiro a esquerda do sucessor agora que ele assumiu 
                                        # a posição correta na arvore   
        return True

    def removeNos(self, atual):
        if self.root == None:
            return False # se arvore vazia
        pai = atual.pai
        # Se nao possui nenhum filho (é uma folha), elimine-o
        if atual.esq == None and atual.dir == None:
            #print("Arvores 01")
            if atual == self.root:
                self.root = None # se raiz
                #print("Arvores 02")
            else:
                if pai.esq==atual:
                    #print(pai,pai.esq,atual)
                    #print("Arvores 03")
                    pai.esq =  None # se for filho a esquerda do pai
                else:
                    pai.dir = None # se for filho a direita do pai
                    #print("Arvores 04")

        # Se é pai e nao possui um filho a direita, substitui pela subarvore a direita
        elif atual.dir == None:
            #print("Arvores 05")
            if atual == self.root:
                self.root = atual.esq # se raiz
                atual.esq.pai=None
                #print("Arvores 06")
            else:
                if pai.esq==atual:
                    pai.esq = atual.esq # se for filho a esquerda do pai
                    atual.esq.pai=pai
                    #print("Arvores 07")
                else:
                    pai.dir = atual.esq # se for filho a direita do pai
                    atual.esq.pai=pai
                    #print("Arvores 08")
        # Se é pai e nao possui um filho a esquerda, substitui pela subarvore a esquerda
        elif atual.esq == None:
            #print("Arvores 09")
            if atual == self.root:
                #print("Arvores 10")
                self.root = atual.dir # se raiz
                atual.dir.pai=None
            else:
                if pai.esq==atual:
                    pai.esq = atual.dir # se for filho a esquerda do pai
                    atual.dir.pai=pai
                    #print("Arvores 11")
                else:
                    pai.dir = atual.dir # se for  filho a direita do pai
                    atual.dir.pai=pai
                    #print("Arvores 12")

        # Se possui mais de um filho, se for um avô ou outro grau maior de parentesco
        else:
            #breakpoint();
            sucessor = self.nosucessor(atual)
            #print("Arvores 13")
            # Usando sucessor que seria o Nó mais a esquerda da subarvore a direita do No que deseja-se remover
            if atual == self.root:
                self.root = sucessor # se raiz
                sucessor.pai=None
                #print("Arvores 14")
            else:
                if pai.esq==atual:
                    pai.esq = sucessor # se for filho a esquerda do pai
                    sucessor.pai=pai
                    #print("Arvores 15")
                else:
                    pai.dir = sucessor # se for filho a direita do pai
                    sucessor.pai=pai
                    #if(atual.dir!=sucessor):
                    #    atual.dir.pai=sucessor
                    #print("Arvores 16")
            sucessor.esq = atual.esq # acertando o ponteiro a esquerda do sucessor agora que ele assumiu 
            atual.esq.pai=sucessor
            # a posição correta na arvore   
        return True
    
    def quatidadeItems(self,atual,quantidade):
        if atual != None:
            self.quatidadeItems(atual.esq,quantidade)
            quantidade['quantidade']+=len(atual.blocosChave)
            #log.escrever(atual.item)
            self.quatidadeItems(atual.dir,quantidade)
    
    def removerQuantidade(self,atual,lista,quantidade,listaFilmes,log):
        if atual != None and quantidade>len(lista) :
            self.removerQuantidade(atual.esq,lista,quantidade,listaFilmes,log)
            if(len(atual.blocosChave)<=(quantidade-len(lista))):
                for dados in atual.blocosChave.values():
                    del(listaFilmes[dados['idFilme']].endNos[dados['idBloco']])
                #lista.extend(atual.blocos)
                lista.update(atual.blocosChave)
                atual.blocosChave={}
                #del atual.item
            elif((quantidade-len(lista))>0):
                valorQuantidade=(quantidade-len(lista))
                contador=0
                for key in list(atual.blocosChave)[:]:
                    lista[key]=atual.blocosChave[key].copy();
                    del(listaFilmes[atual.blocosChave[key]['idFilme']].endNos[atual.blocosChave[key]['idBloco']])
                    del(atual.blocosChave[key])
                    contador+=1
                    if(contador==valorQuantidade):
                        break;  
                return 0
            self.removerQuantidade(atual.dir,lista,quantidade,listaFilmes,log)
            if(len(atual.blocosChave)==0):
                #self.inOrderLog(self.root,log)
                if atual.esq == None and atual.dir == None:
                    #log.escrever("if 1")
                    #print("if 1")
                    if atual == self.root:
                        self.root = None # se raiz
                        atual.pai=None
                    else:
                        if atual.pai.esq==atual:
                            atual.pai.esq =  None # se for filho a esquerda do pai
                        else:
                            atual.pai.dir = None # se for filho a direita do pai
                # Se é pai e nao possui um filho a esquerda, substitui pela subarvore a esquerda
                elif atual.esq == None:
                    #log.escrever("if 3")
                    #print("if 3")
                    if atual == self.root:
                        self.root = atual.dir # se raiz
                        atual.dir.pai=None
                    else:
                        if atual.pai.esq==atual:
                            atual.pai.esq = atual.dir # se for filho a esquerda do pai
                            atual.dir.pai=atual.pai
                        else:
                            atual.pai.dir = atual.dir # se for  filho a direita do pai
                            atual.dir.pai=atual.pai
                # Se é pai e nao possui um filho a direita, substitui pela subarvore a direita
                elif atual.dir == None:
                    #breakpoint();
                    #log.escrever("if 2")
                    #print("if 2")
                    if atual == self.root:
                        self.root = atual.esq # se raiz
                        atual.esq.pai=None
                    else:
                        if atual.pai.esq==atual:
                            atual.pai.esq = atual.esq # se for filho a esquerda do pai
                            atual.esq.pai=pai
                        else:
                            atual.pai.dir = atual.esq # se for filho a direita do pai
                            atual.esq.pai=pai
                # Se possui mais de um filho, se for um avô ou outro grau maior de parentesco
                else:
                    #log.escrever("if 4")
                    #print("if 4")
                    #breakpoint();
                    sucessor = self.nosucessor(atual)
                    # Usando sucessor que seria o Nó mais a esquerda da subarvore a direita do No que deseja-se remover
                    if atual == self.root:
                        self.root = sucessor # se raiz
                        sucessor.pai=None
                    else:
                        if atual.pai.esq==atual:
                            atual.pai.esq=sucessor # se for filho a esquerda do pai
                            sucessor.pai=atual.pai 
                        else:
                            atual.pai.dir=sucessor # se for filho a direita do pai
                            sucessor.pai=atual.pai
                            #if(atual.dir!=sucessor):
                            #    atual.dir.pai=sucessor
                    sucessor.esq = atual.esq
                    atual.esq.pai=sucessor
            
                    
    
    def mostrarClassificacao(self,pai,filho_esq, atual,lista):
        if atual != None:
            self.mostrarClassificacao(atual,True,atual.esq,lista)
            for key in atual.blocosChave.keys():
                print(key)
                lista.append({'memoria':atual.blocosChave[key]['memoria'],'pontuacao':atual.item ,'idFilme':atual.blocosChave[key]['idFilme'] ,'idBloco':atual.blocosChave[key]['idBloco']})
            #lista.update(atual.blocosChave)
            self.mostrarClassificacao(atual,False,atual.dir,lista)
    
    def verificarLoopNos(self,atual):
        if((atual==atual.esq and atual!=None) or (atual==atual.dir and atual!=None) or (atual==atual.pai and atual!=None) or (atual.pai==atual.esq and atual.pai!=None) or (atual.pai==atual.dir and atual.pai!=None) or (atual.dir==atual.esq and atual.esq!=None)):
            breakpoint();
            
        
    
    
    def inOrder(self, atual):
        if atual != None:
            self.inOrder(atual.esq)
            # log.escrever(atual)
            print(atual,end=" ")
            # if(atual.item<0):
            #     breakpoint()
            self.inOrder(atual.dir)
    def inOrderLog(self, atual,log):
        if atual != None:
            self.inOrderLog(atual.esq,log)
            # log.escrever(atual)
            log.escrever("("+str(atual.esq)+"-"+str(atual)+"["+str(atual.pai)+"]-"+str(atual.dir)+")")
            # if(atual.item<0):
            #     breakpoint()
            self.inOrderLog(atual.dir,log)
    def inOrderPrint(self, atual):
        if atual != None:
            self.inOrderPrint(atual.esq)
            # log.escrever(atual)
            print("("+str(atual.esq)+"-"+str(atual)+"["+str(atual.pai)+"]-"+str(atual.dir)+")")
            # if(atual.item<0):
            #     breakpoint()
            self.inOrderPrint(atual.dir)
            
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
        print("Exibindo em ordem: ",end="")
        self.inOrder(self.root)
        print("\n Exibindo em pos-ordem: ",end="")
        self.posOrder(self.root)
        print("\n Exibindo em pre-ordem: ",end="")
        self.preOrder(self.root)
        print("\n Altura da arvore: %d" %(self.altura(self.root)))
        print("Quantidade de folhas: %d"  %(self.folhas(self.root)))
        print("Quantidade de Nós: %d" %(self.contarNos(self.root)))
        if self.root != None: # se arvore nao esta vazia
            print("Valor minimo: %d" %(self.minn().item))
            print("Valor maximo: %d" %(self.maxx().item))
