# VoDProS-Video-on-demand-proxy-Simulator

VoDProS consegue simular o fluxo do funcionamento  de servidor proxy VoD e atraves do simulação conseguindo extrair informações como a taxa de acerto do proxy, para diferentes cerarios e argortimos.


###Para executar tem ter alguns pacotes instalado: 

OS-sys
`pip install os-sys `

Python-time 
`pip install python-time`

Python-math
`pip install python-math`

Multiprocess
`pip install multiprocess`

###Para executar o código no pode executar: 
####PYTHON 3 

    cd ./src/
    
    python3 main.py

ou

    cd ./src/

    python3 main.py 1 1 1

1º argumento é numero do diretorio de leitura  
2º argumento é numero da varição dos parametros
3º argumento é numero do algortimo que deseja executar

###OBS
  Altere a variale `numeorThreadMax` que é quantidade de thread que o simulador podera usar.

#####*OBS:* utilise o pypy3 como compilador por executar o codigo em menor tempo.


###### Matheus Koch-