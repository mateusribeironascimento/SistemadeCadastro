from EX115.lib.interface import *
from EX115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    sleep(2)
    cabeçalho()
    resposta = leiaInt('Digite sua opção: ')
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho2('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do sistema... Até logo!')
        sleep(1)
        break
    else:
        print('\033[1:31mERRO! Digite uma opção válida.\033[m')