from utils.titulos import *
from utils.validacao import *
from gerenciadores.gerenciador_receita import GerenciadorReceita
from gerenciadores.gerenciador_despesa import GerenciadorDespesa
from gerenciadores.gerenciador_resumo_mensal import GerenciadorResumoMensal


gerenciador_rec = GerenciadorReceita()
gerenciador_desp = GerenciadorDespesa()
gerenciador_resumo = GerenciadorResumoMensal()

titulo('FinPlanner', '*=', 40)
while True:
    titulo('MENU', '-', 30)
    print('Opções:')
    print('1 - Receita\n2 - Despesa\n3 - Resumo Mensal\n4 - Salvar Arquivo\n0 - Sair')
    opc = ler_opcao('>> Sua escolha: ', range(5))
    match opc:
        case 1:
            while True:
                subtitulo('RECEITA', '-', 30)
                print('1 - Cadastrar\n2 - Listar\n3 - Relatório\n0 - Voltar')
                opc_receita = ler_opcao('>> Sua escolha: ', range(4))
                match opc_receita:
                    case 1:
                        subtitulo('CADASTRO', '-', 20)
                        nome_receita = str(input('Nome da Receita: ')).capitalize()
                        tipo_receita = ler_tipo('Tipo da Receita ["fixa"/"variável"]: ')
                        valor_receita = ler_valor('Valor da Receita: R$ ')
                        categoria_receita = str(input('Categoria da Receita: ')).capitalize()
                        data_receita = ler_data('Data da Receita [dd/mm/aa]: ')

                        gerenciador_rec.cadastrar_receita(nome_receita, tipo_receita, valor_receita,
                                                          categoria_receita, data_receita)
                    case 2:
                        subtitulo('RECEITAS', '-', 20)
                        if gerenciador_rec.qtde_receitas() == 0:
                            print('Ainda não há receitas cadastradas!')
                        else:
                            gerenciador_rec.listar_receitas()
                    case 3:
                        subtitulo('RELATÓRIO', '-', 20)
                        if gerenciador_rec.qtde_receitas() == 0:
                            print('Ainda não há receitas cadastradas!')
                        else:
                            gerenciador_rec.relatorio_receitas()
                            print(f'Total: R${gerenciador_rec.total_receitas():.2f}')
                            print(f'Quantidade de receitas cadastradas: {gerenciador_rec.qtde_receitas()}')
                    case 0:
                        break
        case 2:
            while True:
                subtitulo('DESPESA', '-', 30)
                print('1 - Cadastrar\n2 - Listar\n3 - Relatório\n0 - Voltar')
                opc_despesa = ler_opcao('>> Sua escolha: ', range(4))
                match opc_despesa:
                    case 1:
                        subtitulo('CADASTRO', '-', 20)
                        nome_despesa = str(input('Nome da Despesa: ')).capitalize()
                        tipo_despesa = ler_tipo('Tipo da Despesa ["fixa"/"variável"]: ')
                        valor_despesa = ler_valor('Valor da Despesa: R$ ')
                        categoria_despesa = str(input('Categoria da Despesa: ')).capitalize()
                        data_despesa = ler_data('Data da Despesa [dd/mm/aa]: ')

                        gerenciador_desp.cadastrar_despesa(nome_despesa, tipo_despesa, valor_despesa,
                                                           categoria_despesa, data_despesa)
                    case 2:
                        subtitulo('DESPESAS', '-', 20)
                        if gerenciador_desp.qtde_despesas() == 0:
                            print('Ainda não há despesas cadastradas!')
                        else:
                            gerenciador_desp.listar_despesas()
                    case 3:
                        subtitulo('RELATÓRIO', '-', 20)
                        if gerenciador_desp.qtde_despesas() == 0:
                            print('Ainda não há despesas cadastradas!')
                        else:
                            gerenciador_desp.relatorio_despesas()
                            print(f'Total: R${gerenciador_desp.total_despesas():.2f}')
                            print(f'Quantidade de despesas cadastradas: {gerenciador_desp.qtde_despesas()}')
                    case 0:
                        break
        case 3:
            subtitulo('RESUMO MENSAL', '-', 30)
            if gerenciador_rec.qtde_receitas() == 0 or gerenciador_desp.qtde_despesas() == 0:
                print('Ainda não é possível gerar o resumo mensal!')
            else:
                while True:
                    try:
                        ano = int(input('Ano (ex: 2025): '))
                        mes = ler_opcao('Digite o número do mês (1 - 12): ', range(1, 13))
                        break
                    except ValueError:
                        print('Ano ou mês inválido!')
                receitas_do_mes = gerenciador_rec.filtrar_por_mes(ano, mes)
                despesas_do_mes = gerenciador_desp.filtrar_por_mes(ano, mes)

                gerenciador_resumo.obter_ou_criar_resumo(ano, mes, receitas_do_mes, despesas_do_mes)

                gerenciador_resumo.exibir_resumo(ano, mes)
        case 4:
            subtitulo('SALVAR', '-', 30)
        case 0:
            break
subtitulo('Programa Finalizado!', '*=', 30)