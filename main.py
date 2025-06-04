from utils.titulos import *
from utils.validacao import *
from gerenciadores.gerenciador_receita import GerenciadorReceita
from gerenciadores.gerenciador_despesa import GerenciadorDespesa
from gerenciadores.gerenciador_resumo_mensal import GerenciadorResumoMensal
from arquivos.exporta_excel import ExportaExcel

gerenciador_rec = GerenciadorReceita()
gerenciador_desp = GerenciadorDespesa()
gerenciador_resumo = GerenciadorResumoMensal()
exportador = ExportaExcel(gerenciador_rec, gerenciador_desp, gerenciador_resumo.resumos)

titulo('FinPlanner', '*=', 40)
while True:
    titulo('MENU', '-', 30)
    print('Opções:')
    print('1 - Receita\n2 - Despesa\n3 - Resumo Mensal\n4 - Exportar arquivos\n0 - Sair')  # Menu principal
    opc = ler_opcao('>> Sua escolha: ', range(5))
    match opc:
        case 1:
            while True:
                subtitulo('RECEITA', '-', 30)
                print('1 - Cadastrar\n2 - Listar\n3 - Relatório\n0 - Voltar')  # Menu Receita
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
                print('1 - Cadastrar\n2 - Listar\n3 - Relatório\n0 - Voltar')  # Menu Despesa
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
            ano, mes = ler_ano_mes()

            receitas_do_mes = gerenciador_rec.filtrar_por_mes(ano, mes)
            despesas_do_mes = gerenciador_desp.filtrar_por_mes(ano, mes)

            if not receitas_do_mes and not despesas_do_mes:
                print(f'Ainda não foram cadastadas nem receitas nem despesas de {mes}/{ano} !')
            else:
                gerenciador_resumo.atualizar_resumo(ano, mes, receitas_do_mes, despesas_do_mes)
                gerenciador_resumo.exibir_resumo(ano, mes)

        case 4:
            while True:
                subtitulo('EXPORTAR', '-', 30)  # Menu Exportar
                print('O que deseja salvar?')
                print('1 - Todas as receitas (arquivo .xlsx com apenas as receitas)\n2 - Todas as despesas ('
                      'arquivo .xlsx com apenas as despesas)\n3 - Receitas de um período (arquivo .xlsx com apenas '
                      'receitas do mês e ano escolhidos)\n4 - Despesas de um período (arquivo .xlsx com apenas '
                      'despesas do mês e ano escolhidos)\n5 - Resumo Mensal (arquivo .xlsx com RECEITAS, '
                      'DESPESAS e RESUMO juntos)\n0 - Voltar')
                opc_salvar = ler_opcao('>> Sua escolha: ', range(6))
                linha_horizontal('-', 30)

                match opc_salvar:
                    case 1:
                        print('\033[33mEssa opção irá exportar um arquivo .xlsx contendo uma planilha com todas as '
                              'receitas cadastradas.\033[m')
                        resp = ler_resposta_sim_nao('>> Deseja continuar? [s - sim / n - não]: ')
                        if resp == 's':
                            exportador.exportar_receitas(gerenciador_rec.receitas)
                        else:
                            print('\033[31mOperação cancelada!\033[m')

                    case 2:
                        print('\033[33mEssa opção irá exportar um arquivo .xlsx contendo uma planilha com todas as '
                              'despesas cadastradas.\033[m')
                        resp = ler_resposta_sim_nao('>> Deseja continuar? [s - sim / n - não]: ')
                        if resp == 's':
                            exportador.exportar_despesas(gerenciador_desp.despesas)
                        else:
                            print('\033[31mOperação cancelada!\033[m')

                    case 3:
                        print('\033[33mEssa opção irá exportar um arquivo .xlsx contendo uma planilha com todas as '
                              'receitas do mês e ano escolhidos.\033[m')
                        resp = ler_resposta_sim_nao('>> Deseja continuar? [s - sim / n - não]: ')
                        if resp == 's':
                            ano, mes = ler_ano_mes()
                            exportador.exportar_receitas_periodo(ano, mes)
                        else:
                            print('\033[31mOperação cancelada!\033[m')

                    case 4:
                        print('\033[33mEssa opção irá exportar um arquivo .xlsx contendo uma planilha com todas as '
                              'depesas do mês e ano escolhidos.\033[m')
                        resp = ler_resposta_sim_nao('>> Deseja continuar? [s - sim / n - não]: ')
                        if resp == 's':
                            ano, mes = ler_ano_mes()
                            exportador.exportar_despesas_periodo(ano, mes)
                        else:
                            print('\033[31mOperação cancelada!\033[m')

                    case 5:
                        print('\033[33mEssa opção irá exportar um arquivo .xlsx contendo 3 planilhas:')
                        print('- Receitas do mês')
                        print('- Despesas do mês')
                        print('- Resumo mensal\033[m')
                        resp = ler_resposta_sim_nao('>> Deseja continuar? [s - sim / n - não]: ')
                        if resp == 's':
                            ano, mes = ler_ano_mes()
                            exportador.exportar_resumo_mensal(ano, mes)
                        else:
                            print('\033[31mOperação cancelada!\033[m')
                    case 0:
                        break
        case 0:
            break
subtitulo('Programa Finalizado!', '*=', 30)