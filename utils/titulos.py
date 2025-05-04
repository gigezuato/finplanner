def linha_horizontal(simbolo, tamanho):
    print(f'\033[32m{simbolo}\033[m' * tamanho)


def titulo(msg, simb, tam):
    linha_horizontal(simb, tam)
    print(f'\033[32m{msg.center(tam * len(simb))}\033[m')
    linha_horizontal(simb, tam)


def subtitulo(msg, simb, tam):
    if simb == ' ' or '':
        print(' ' * (tam // 2), f'\033[36m{msg}\033[m', ' ' * (tam // 2))
    else:
        print(f'\033[36m{simb}\033[m' * (tam // 2), f'\033[36m{msg}\033[m', f'\033[36m{simb}\033[m' * (tam // 2))