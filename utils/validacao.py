def ler_opcao(msg, opcoes_validas):
    while True:
        opc = input(msg).strip()
        if opc.isdigit():
            valor = int(opc)
            if valor in opcoes_validas:
                return valor
        print(f'Entrada inválida! Digite um número entre {min(opcoes_validas)} e {max(opcoes_validas)}')