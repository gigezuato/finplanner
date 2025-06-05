from datetime import datetime


def ler_opcao(msg, opcoes_validas):
    """
        -> Verifica se a opção digitada pelo usuário é um número e se está no intervalo de números de opções válidas.
    :param msg: mensagem exibida para o usuário
    :param opcoes_validas: intervalo (range) de números correspondentes às opções válidas
    :return: o valor númerico da opção escolhida e validada
    """
    while True:
        opc = input(msg).strip()
        if opc.isdigit():
            valor = int(opc)
            if valor in opcoes_validas:
                return valor
        print(f'\033[31mEntrada inválida! Digite um número entre {min(opcoes_validas)} e {max(opcoes_validas)}\033[m')


def ler_tipo(msg):
    """
        -> Verifica se o tipo digitado pelo usuário corresponde à "fixa" ou "váriável".
    :param msg: mensagem exibida para o usuário
    :return: retorna o tipo validado
    """
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
    """
        -> Verifica se o valor digitado é um número. Obs: o número irá ser lido e retornado no formato float.
    :param msg: mensagem exibida para o usuário
    :return: o valor validado
    """
    while True:
        try:
            valor = float(input(msg))
            return valor
        except ValueError:
            print('\033[31mValor inválido! Por favor, digite números.\033[m')


def ler_data(msg):
    """
        -> Verifica se a data digitada está no formato: dd/mm/aa (Ex: 10/05/25)
    :param msg: mensagem exibida para o usuário
    :return: a data validada
    """
    while True:
        data = str(input(msg))
        try:
            data_validada = datetime.strptime(data, '%d/%m/%y')
            return data_validada
        except ValueError:
            print('\033[31mFormato inválido! Use dd/mm/aa.\033[m')


def ler_resposta_sim_nao(msg):
    """
        -> Lê e verifica uma resposta do tipo "sim" ou "não", sendo sim = 's' e não = 'n'.
    :param msg: mensagem exibida para o usuário
    :return: a resposta validada
    """
    while True:
        resp = str(input(msg)).lower().strip()
        if resp in 'sn':
            break
        else:
            print('\033[31mResposta inválida! Digite "s" para sim ou "n" para não.\033[m')
    return resp


def ler_ano_mes():
    """
        -> Lê e verifica o ano e o mês, ou seja, se o ano é um valor núméico e se o mês está entre 1 e 12.
    :return: o ano e o mês validados
    """
    while True:
        try:
            ano = int(input('Ano (ex: 2025): '))
            break
        except ValueError:
            print('\033[31mAno inválido!\033[m')
    mes = ler_opcao('Digite o número do mês (1 - 12): ', range(1, 13))
    return ano, mes