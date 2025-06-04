from datetime import datetime


def ler_opcao(msg, opcoes_validas):
    while True:
        opc = input(msg).strip()
        if opc.isdigit():
            valor = int(opc)
            if valor in opcoes_validas:
                return valor
        print(f'\033[31mEntrada inválida! Digite um número entre {min(opcoes_validas)} e {max(opcoes_validas)}\033[m')


def ler_tipo(msg):
    while True:
        tipo = str(input(msg)).strip().lower()
        if tipo == 'fixa' or tipo == 'variável':
            return tipo
        elif tipo == 'variavel':
            tipo = 'variável'
            return tipo
        else:
            print('\033[31mTipo inválido! As opções são: fixa ou variável.\033[m')


def ler_valor(msg):
    while True:
        try:
            valor = float(input(msg))
            return valor
        except ValueError:
            print('\033[31mValor inválido! Por favor, digite números.\033[m')


def ler_data(msg):
    while True:
        data = str(input(msg))
        try:
            data_validada = datetime.strptime(data, '%d/%m/%y')
            return data_validada
        except ValueError:
            print('\033[31mFormato inválido! Use dd/mm/aa.\033[m')


def ler_resposta_sim_nao(msg):
    while True:
        resp = str(input(msg)).lower().strip()
        if resp in 'sn':
            break
        else:
            print('\033[31mResposta inválida! Digite "s" para sim ou "n" para não.\033[m')
    return resp


def ler_ano_mes():
    while True:
        try:
            ano = int(input('Ano (ex: 2025): '))
            mes = ler_opcao('Digite o número do mês (1 - 12): ', range(1, 13))
            return ano, mes
        except ValueError:
            print('\033[31mAno ou mês inválido!\033[m')