def linha_horizontal(simbolo, tamanho):
    print(f'{simbolo}' * tamanho)


def titulo(msg, simb, tam):
    linha_horizontal(simb, tam)
    print(msg.center(tam * len(simb)))
    linha_horizontal(simb, tam)


def subtitulo(msg, simb, tam):
    if simb == ' ' or '':
        print(' ' * (tam // 2), msg, ' ' * (tam // 2))
    else:
        print(f'{simb}' * (tam // 2), msg, f'{simb}' * (tam // 2))