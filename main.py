from manipulacaoArquivo import ManipulacaoArquivo
from algoritmoAleatorio import AlgortimoAleatorio
from algoritmoCARTE import AlgortimoCARTE
from algoritmoCC import AlgortimoCC
from resultado import Resultado
from cliente import Cliente
from filme import Filme
from printDados import PrintDados
from planilhaODS import PlaniliaOBS
#Menu  de arquivo fazer


#arquivo contem 4 colunas. (idCleintes,  numero do filme q vai assistir,  tempo de chagada , parte do  video q assistir)
if __name__ == "__main__":
    arq='1t.txt'
    #alg="algorimo=AlgortimoAleatorio()"
    alg="algorimo=AlgortimoCARTE(3)"
    #alg="algorimo=AlgortimoCC()"
    leitura=ManipulacaoArquivo('./baseLeitura/'+str(arq))
    #algorimo=AlgortimoAleatorio()
    print(alg)
    exec(alg)
    memoriaTotal=10
    memoria=[]
    larguraBanda=100
    filaEspera=[]
    instanteTempo=0
    novoCliente=leitura.novoClienteLido()
    listaClientes=[]
    listaFilmes={}
    result=Resultado(arq,alg)
    #pri=PlaniliaOBS()
    #pri.iniciarPlanilha()
    printDados=PrintDados()
    while True:
        #Leitura de novo  cliente e veirificação  de colocar na lista
        while (novoCliente!=0 and novoCliente.tempoInicio==instanteTempo):
            result.novoCliente()
            listaClientes.append(novoCliente)
            novoCliente=leitura.novoClienteLido()
        #pri.AdicionarDadosPlanilha(memoria,listaClientes,instanteTempo,result.acertos,result.erros,listaFilmes,memoriaTotal)
        printDados.intefase3(instanteTempo,result,memoria,memoriaTotal,listaClientes,listaFilmes,algorimo.classificacao)
        #Substituição da parte dos cliente atendendo
        for cliente in (listaClientes[:]):
            if(cliente.idBloco==cliente.tamanhoBloco):
                result.terminouCliente()
                listaClientes.remove(cliente)
            else:
                result.entreguePacote()
                if(cliente.idFilme in listaFilmes):
                    if((cliente.idBloco+1) in listaFilmes[cliente.idFilme].blocos):
                        cliente.trocaBloco(listaFilmes)
                        memoria[listaFilmes[cliente.idFilme].blocoMemoria[cliente.idBloco]]=([cliente.idFilme,cliente.idBloco,listaFilmes[cliente.idFilme].blocos[cliente.idBloco]])
                        result.acerto()
                    else:
                        result.erro()
                        if(memoriaTotal>len(memoria)):
                            cliente.trocaBloco(listaFilmes)
                            listaFilmes[cliente.idFilme].blocoMemoria[cliente.idBloco]=len(memoria)
                            memoria.append([cliente.idFilme,cliente.idBloco,listaFilmes[cliente.idFilme].blocos[cliente.idBloco]])
                        else:
                            algorimo.substituicaoBlocos(listaFilmes,cliente,memoria,listaClientes)
                else:
                    result.erro()
                    listaFilmes[cliente.idFilme]=Filme(cliente.idFilme)
                    if(memoriaTotal>len(memoria)):
                        cliente.trocaBloco(listaFilmes)
                        listaFilmes[cliente.idFilme].blocoMemoria[cliente.idBloco]=len(memoria)
                        memoria.append([cliente.idFilme,cliente.idBloco,listaFilmes[cliente.idFilme].blocos[cliente.idBloco]])
                    else:
                        algorimo.substituicaoBlocos(listaFilmes,cliente,memoria,listaClientes)
                #pri.AdicionarDadosPlanilha(memoria,listaClientes,instanteTempo,result.acertos,result.erros,listaFilmes,memoriaTotal)
                printDados.intefase3(instanteTempo,result,memoria,memoriaTotal,listaClientes,listaFilmes,algorimo.classificacao)

        #Verficação final para ver se acabou  a distribuição ou  vai ter q contabilidar mais uma tempo
        if(novoCliente==0 and len(listaClientes)==0):
            #print(novoCliente)
            leitura.escritaResult(result)
            break
        else:
            instanteTempo=instanteTempo+1
            #print("Tempo %i" %instanteTempo)
    # pri.salvarArquivo()

#Menu  de dos codicos
