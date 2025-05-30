def linha_horizontal(simbolo, tamanho):
    """
        -> Imprime uma linha horizontal verde com os símbolo(s) passado(s) e o tamanho especificado.
    :param simbolo: caracter que irá compor a linha (pode ser mais de um)
    :param tamanho: tamanho que a linha terá
    """
    print(f'\033[32m{simbolo}\033[m' * tamanho)


def titulo(msg, simb, tam):
    """
        -> Imprime um título verde com linhas superiores e inferiores (com o simbolo e tamanho passados) e a mensagem no
        centro.
    :param msg: mensagem
    :param simb: simbolo que irá compor as linhas (pode ser mais de um)
    :param tam: tamanho do título
    """
    linha_horizontal(simb, tam)
    print(f'\033[32m{msg.center(tam * len(simb))}\033[m')
    linha_horizontal(simb, tam)


def subtitulo(msg, simb, tam):
    """
        -> Imprime um subtítulo ciano que inclui a mensagem envolta do simbolo escolhido (ex: -----Python-----)
    :param msg: mensagem
    :param simb: simbolo que irá compor o subtítulo (pode ser mais de um)
    :param tam:tamanho do subtítulo
    """
    if simb == ' ' or '':
        print(' ' * (tam // 2), f'\033[36m{msg}\033[m', ' ' * (tam // 2))
    else:
        print(f'\033[36m{simb}\033[m' * (tam // 2), f'\033[36m{msg}\033[m', f'\033[36m{simb}\033[m' * (tam // 2))