import json
from pyexcel_ods import get_data
from pyexcel_ods import save_data

class PlaniliaOBS:
    def __init__(self):
        self.arquivo="executando.ods"
        self.data=0
        self.ultimaLinha=0

    def leitura(self):
        self.data = get_data(self.arquivo)
        self.ultimaLinha=len(self.data.values()[0])
    def print(self):
        print(json.dumps(self.data))
    
    def salvarLinha(self):
         save_data(self.arquivo, self.data,start_row=self.ultimaLinha)

    def salvarArquivo(self):
        save_data(self.arquivo, self.data)
    def iniciarPlanilha(self):
        self.data={'tab1':[]}


    def AdicionarDadosPlanilha(self,memoria,clientes,tempo,acertos,erros,listaFilmes,tamanhoMemoria):
        linha=[[],[],[],[]]
        linha[0].append('Tempo')
        linha[1].append('Acertos')
        linha[2].append('Erros')
        linha[0].append(str(tempo))
        linha[1].append(str(acertos))
        linha[2].append(str(erros))
        linha[0].append('')
        linha[1].append('')
        linha[2].append('')
        linha[0].append('Posicao')
        linha[1].append('Blocos')
        linha[2].append('Filme')
        for id,bloco in enumerate(memoria):
                linha[0].append(str(id))
                linha[1].append(str(bloco[1]))
                linha[2].append(str(bloco[0]))
        memoriaEmBRanco=len(memoria)
        while(memoriaEmBRanco<tamanhoMemoria):
            linha[0].append(str(memoriaEmBRanco))
            linha[1].append('')
            linha[2].append('')
            memoriaEmBRanco+=1
        linha[0].append('')
        linha[1].append('')
        linha[2].append('')
        for id,cli in enumerate(clientes):
                linha[0].append(str(cli.idCliente))
                linha[1].append(str(cli.idBloco))
                linha[2].append(str(cli.idFilme))
        self.data['tab1']+=linha


        