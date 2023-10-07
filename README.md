# VoDProS-Video-on-demand-proxy-Simulator

VoDProS consegue simular o fluxo do funcionamento  de servidor proxy VoD e atraves do simulação conseguindo extrair informações como a taxa de acerto do proxy, para diferentes cerarios e argortimos.

##Primeiros Execução

### Antes criar ambiente virtual, para depos proseguir para os proximos passos

Criar Ambienste virtual
`python3 -m  venv ./env`

Ativa ambiente virtual
`source ./env/bin/activate`

### Instalar os seguintes pacotes:

OS-sys
`pip install os-sys `

Python-time
`pip install python-time`

Python-math
`pip install python-math`

Multiprocess
`pip install multiprocess`

### Para executar o código no pode executar:
#### PYTHON 3

    cd ./src/

    python3 main.py

##Depois da primeira vez Execução



ou

    cd ./src/

    python3 main.py 1 1 1

1º argumento é numero do diretorio de leitura
2º argumento é numero da varição dos parametros
3º argumento é numero do algortimo que deseja executar

### OBS
  Altere a variale `numeorThreadMax` que é quantidade de thread que o simulador podera usar.

##### *OBS:* utilise o pypy3 como compilador por executar o codigo em menor tempo.


###### Matheus Koch-
