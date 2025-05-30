from modelos.resumo_mensal import ResumoMensal
from utils.titulos import linha_horizontal


class GerenciadorResumoMensal:
    def __init__(self):
        self.resumos = {}

    def obter_ou_criar_resumo(self, ano, mes, receitas, despesas):
        """
            -> Se o resumo já existir, ele é retornado, senão, cria-se o resumo daquele mês e ano.
        :param ano: ano do resumo
        :param mes: mês do resumo
        :param receitas: receitas daquele período (ano, mês)
        :param despesas: despesas daquele período (ano, mês)
        :return: o resumo do mês e ano que foram fornecidos
        """
        chave = (ano, mes)
        if chave not in self.resumos:
            self.resumos[chave] = ResumoMensal(ano, mes, receitas, despesas)
        return self.resumos[chave]

    def atualizar_resumo(self, ano, mes, receitas, despesas):
        """
            -> Atualiza os dados do resumo mensal se ele ja existir, senão o método obter_ou_criar_resumo é chamado
            para criar o resumo.
        :param ano: ano do resumo
        :param mes: mês do resumo
        :param receitas: receitas daquele período
        :param despesas: despesas daquele período
        """
        chave = (ano, mes)
        if chave in self.resumos:
            self.resumos[chave].receitas = receitas
            self.resumos[chave].despesas = despesas
            self.resumos[chave].porcentagens = {}
        else:
            self.obter_ou_criar_resumo(ano, mes, receitas, despesas)

    def exibir_resumo(self, ano, mes):
        """
            -> Exibe o resumo mensal do período que o usuário digitou.
        :param ano: ano do resumo
        :param mes: mês do resumo
        """
        meses = [' ', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
                 'Outubro', 'Novembro', 'Dezembro']
        nome_mes = meses[mes]
        chave = (ano, mes)

        if chave in self.resumos.keys():
            resumo = self.resumos[chave]
            print(f'\033[32m{nome_mes.upper().center(30, '.')}\033[m')
            print(f'Total de Receitas: R$ {resumo.total_receitas():.2f}')
            print(f'Total de Despesas: R$ {resumo.total_despesas():.2f}')
            print(f'Saldo Mensal: R$ {resumo.saldo_mensal():.2f}')

            linha_horizontal('.', 30 + len(nome_mes))

            if resumo.despesas:
                print('Porcentagens por Categoria de Despesas: ')
                if not resumo.porcentagens:
                    resumo.porc_categoria()
                for cat, porc in resumo.porcentagens.items():
                    print(cat, ' = ', round(porc, 2), '%')

                linha_horizontal('.', 30 + len(nome_mes))

                menor_categoria, menor_porc = resumo.menor_categoria_despesa()
                maior_categoria, maior_porc = resumo.maior_categoria_despesa()
                menor_despesa, menor_valor = resumo.menor_gasto()
                maior_despesa, maior_valor = resumo.maior_gasto()

                print(f'Menor porcentagem por categoria de Despesa: {menor_categoria} - {menor_porc:.2f}%')
                print(f'Maior porcentagem por categoria de Despesa: {maior_categoria} - {maior_porc:.2f}%')
                print(f'Menor Despesa: {menor_despesa} - R$ {menor_valor:.2f}')
                print(f'Maior Despesa: {maior_despesa} - R$ {maior_valor:.2f}')
            else:
                print('Não há despesas cadastradas para esse mês!')
        else:
            print(f'\033[31mResumo do mês {nome_mes} de {ano} não encontrado!\033[m')