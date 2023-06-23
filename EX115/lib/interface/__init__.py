def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1:31mERRO! Digite uma opção válida.\033[m')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n


def cabeçalho():
    print('=' * 40)
    print(f'\033[7m{"MENU PRINCIPAL":^40}\033[m')
    print('=' * 40)
    print('\033[1:31m1\033[m', ' - ', '\033[1:34mVer Pessoas Cadastradas')
    print('\033[1:31m2\033[m', ' - ', '\033[1:34mCadastrar Nova Pessoa')
    print('\033[1:31m3\033[m', ' - ', '\033[1:34mSair do Sistema\033[m')
    print('=' * 40)


def cabeçalho2(txt):
    print('=' * 40)
    print(f'\033[7m{txt:^40}\033[m')
    print('=' * 40)