from utils.titulos import *
from utils.validacao import *

titulo('FinPlanner', '*=', 40)
while True:
    print('Opções:')
    print('''
    1 - Cadastrar
    2 - Visualizar
    3 - Resumo Mensal
    4 - Salvar Arquivo
    0 - Sair''')
    opc = ler_opcao('>> Sua escolha: ', range(5))
    match opc:
        case 1:
            subtitulo('CADASTRAR', '-', 30)
            while True:
                print('''
                1 - Receitas
                2 - Despesas
                0 - Voltar
                ''')
                opc_cadastro = ler_opcao('>> Sua escolha: ', range(3))
                match opc_cadastro:
                    case 1:
                        subtitulo('RECEITAS', '-', 20)
                    case 2:
                        subtitulo('DESPESAS', '-', 20)
                    case 0:
                        break
        case 2:
            subtitulo('VISUALIZAR', '-', 30)
            while True:
                print('''
                1 - Receitas
                2 - Despesas
                0 - Voltar
                ''')
                opc_visualizar = ler_opcao('>> Sua escolha: ', range(3))
                match opc_visualizar:
                    case 1:
                        subtitulo('RECEITAS', '-', 20)
                    case 2:
                        subtitulo('DESPESAS', '-', 20)
                    case 0:
                        break
        case 3:
            subtitulo('RESUMO MENSAL', '-', 30)
        case 4:
            subtitulo('SALVAR', '-', 30)
        case 0:
            break
subtitulo('Programa Finalizado!', '*=', 30)