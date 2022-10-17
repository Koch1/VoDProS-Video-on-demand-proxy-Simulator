
import os
from clas.resultado import Resultado

class PrintDados:
    def memoriaRAM(self,memoria,clientes,tempo):
        print(tempo)
        posicao=""
        blocos=""
        filme=""
        for id,bloco in enumerate(memoria):
            if(id<10):
                posicao+=str(" "+str(id)+"|")
            else:
                posicao+=str(""+str(id)+"|")
            if(bloco[0]<10):
                filme+=str(" "+str(bloco[0])+"|")
            else:
                filme+=str(""+str(bloco[0])+"|")
            if(bloco[1]<10):
                blocos+=str(" "+str(bloco[1])+"|")
            else:
                blocos+=str(""+str(bloco[1])+"|")
        posicao+=str('C|')
        blocos+=str('C|')
        filme+=str('C|')
        for id,cli in enumerate(clientes):
            if(id<10):
                posicao+=str(" "+str(id)+"|")
            else:
                posicao+=str(""+str(id)+"|")
            if(cli.idBloco<10):
                blocos+=str(" "+str(cli.idBloco)+"|")
            else:
                blocos+=str(""+str(cli.idBloco)+"|")
            if(cli.idFilme<10):
                filme+=str(" "+str(cli.idFilme)+"|")
            else:
                filme+=str(""+str(cli.idFilme)+"|")
        print("|",posicao)
        print("|",blocos)
        print("|",filme)



    def intefase3 (self,tempo,result,memoria,tamanhoMemoria,clientes,filmess,classifisao):
        print("\n" * os.get_terminal_size().lines)
        print('Tempo: %i             Acertos:%i       Erros: %i    Erros(LimiteBanda): %i         Algorimo: %s'%(tempo,result.acertos,result.erros,result.erroBandas,result.nomeAlgoritimo))
        print('Memoria -----------------------------------------------------------------------------------------------------')
        posicao=""
        filme=""
        blocos=""
        parmetro=""
        argumento=""
        for id,bloco in enumerate(memoria):
            if(id<10):
                posicao+=str(" "+str(id)+"|")
            else:
                posicao+=str(str(id)+"|")
            if(bloco[0]<10):
                filme+=str(" "+str(bloco[0])+"|")
            else:
                filme+=str(""+str(bloco[0])+"|")
            if(bloco[1]<10):
                blocos+=str(" "+str(bloco[1])+"|")
            else:
                blocos+=str(""+str(bloco[1])+"|")
            if(bloco[2]<10):
                parmetro+=str(" "+str(bloco[2])+"|")
            else:
                parmetro+=str(""+str(bloco[2])+"|")
            if(bloco[3]<10):
                argumento+=str(" "+str(bloco[3])+"|")
            else:
                argumento+=str(""+str(bloco[3])+"|")
        memoriaEmBRanco=len(memoria)
        while(memoriaEmBRanco<tamanhoMemoria):
            if(memoriaEmBRanco<10):
                posicao+=(" "+str(memoriaEmBRanco)+"|")
            else:
                posicao+=(""+str(memoriaEmBRanco)+"|")
            filme+=('  |')
            blocos+=('  |')
            parmetro+=('  |')
            argumento+=('  |')
            memoriaEmBRanco+=1
        print("|",posicao, 'Posicao da memoria')
        print("|",filme,'Filme')
        print("|",blocos, 'Bloco')
        print("|",parmetro,'Parametro')
        print("|",argumento, 'Argumento Generico')

        print('Subtituição -----------------------------------------------------------------------------------------------------')
        posicaoMemoria=''
        pontuacao=''
        filme=''
        blocos=''
        proximoFinal=''

        for id,classif in enumerate(classifisao):
            if(id<10):
                posicaoMemoria+=str(" "+str(classif['memoria'])+"|")
            else:
                posicaoMemoria+=str(""+str(classif['memoria'])+"|")
            if(classif['pontuacao']<10):
                pontuacao+=str(" "+str(classif['pontuacao'])+"|")
            else:
                pontuacao+=str(""+str(classif['pontuacao'])+"|")
            if(classif['idFilme']<10):
                filme+=str(" "+str(classif['idFilme'])+"|")
            else:
                filme+=str(""+str(classif['idFilme'])+"|")
            if(classif['idBloco']<10):
                blocos+=str(" "+str(classif['idBloco'])+"|")
            else:
                blocos+=str(""+str(classif['idBloco'])+"|")
            if('proximoFinal' in classif):
                if(classif['proximoFinal']>-10):
                    proximoFinal+=str(" "+str(classif['proximoFinal'])+"|")
                else:
                    proximoFinal+=str(""+str(classif['proximoFinal'])+"|")
        print("|",posicaoMemoria, 'Posicao Mememoria')
        print("|",pontuacao, 'Pontuacao')
        print("|",filme,'Filme')
        print("|",blocos,'Bloco')
        if(proximoFinal!=""):
            print("|",proximoFinal,'Proximo Final')
        print('Clientes -----------------------------------------------------------------------------------------------------')
        posicao=''
        tempoInicio=''
        blocos=''
        filme=''
        for id,clien in enumerate(clientes):
            if(clien.idCliente<10):
                posicao+=str(" "+str(id)+"|")
            else:
                posicao+=str(""+str(id)+"|")
            if(clien.tempoInicio<10):
                tempoInicio+=str(" "+str(clien.tempoInicio)+"|")
            else:
                tempoInicio+=str(""+str(clien.tempoInicio)+"|")
            if(clien.idFilme<10):
                filme+=str(" "+str(clien.idFilme)+"|")
            else:
                filme+=str(""+str(clien.idFilme)+"|")
            if(clien.idBloco<10):
                blocos+=str(" "+str(clien.idBloco)+"|")
            else:
                blocos+=str(""+str(clien.idBloco)+"|")
        print("|",posicao,'Cliente')
        print("|",tempoInicio,'Tempo Inicio')
        print("|",filme,'Filme')
        print("|",blocos,'Bloco')
        self.filmePrint(filmess)

    def filmePrint(self,filmess):
        print('Filmes -----------------------------------------------------------------------------------------------------')
        tabelaCab="ID|NC|Bloco: Numero de cliente"
        print(tabelaCab)
        tabelaCab="ID|NC|Blocos:  Possicao da memoria"
        print(tabelaCab)
        for fil in filmess:
            textoPrint=""
            if(filmess[fil].idFilme<10):
                 textoPrint+=str(" "+str(filmess[fil].idFilme)+"|")
            else:
                 textoPrint+=str(""+str(filmess[fil].idFilme)+"|")
            if(filmess[fil].numeroClientes<10):
                 textoPrint+=str(" "+str(filmess[fil].numeroClientes)+"|")
            else:
                 textoPrint+=str(""+str(filmess[fil].numeroClientes)+"|")
            print(textoPrint,filmess[fil].blocos)
            print(textoPrint,filmess[fil].blocoMemoria)
            print(textoPrint,filmess[fil].clientes)
            # for ids,blos in enumerate(filmess[fil].blocos):
            #     if(ids<10):
            #          textoPrint+=str(" "+str(ids)+"->")
            #     else:
            #         textoPrint+=str(""+str(ids)+"->")
            #     if(blos<10):
            #         textoPrint+=str(" "+str(blos)+"("+str(len(filmess[fil].blocos))+")-<>")
            #     else:
            #         textoPrint+=str(""+str(blos)+"("+str(len(filmess[fil].blocos))+")-<>")
            #     if(ids in filmess[fil].blocoMemoria):
            #         if(filmess[fil].blocoMemoria[ids]<10):
            #             textoPrint+=str(" "+str(filmess[fil].blocoMemoria[ids])+"("+str(len(filmess[fil].blocoMemoria))+")!")
            #         else:
            #             textoPrint+=str(""+str(filmess[fil].blocoMemoria[ids])+"("+str(len(filmess[fil].blocoMemoria))+")!")
            #print(textoPrint)
        prox=input("Enter para proximo passo:")

