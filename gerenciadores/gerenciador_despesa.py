from modelos.despesa import Despesa
from tabulate import tabulate


class GerenciadorDespesa:
    def __init__(self):
        self.despesas = []

    def cadastrar_despesa(self, nome, tipo, valor, categoria, data):
        """
            -> Realiza o cadastro de despesas.
        :param nome: nome da despesa
        :param tipo: tipo da despesa (fixa/variável)
        :param valor: valor da despesa
        :param categoria: categoria da despesa
        :param data: data da despesa
        """
        despesa = Despesa(nome, tipo, valor, categoria, data)
        self.despesas.append(despesa)
        print(f'\033[32mDespesa {despesa.nome} cadastrada com sucesso!\033[m')

    def listar_despesas(self):
        """
            -> Lista todas as depesas cadastradas, mostrando seu nome, valor e data.
        """
        for d in self.despesas:
            print(f'{d.nome} - R$ {d.valor:.2f} - {d.data.strftime("%d/%m/%Y")}')

    def relatorio_despesas(self):
        """
            -> Faz um relatório, em formato de tabela, com todas as despesas.
        """
        dados_tabela = []
        for d in self.despesas:
            dados_tabela.append(d.dados_relatorio())
        tabela = tabulate(dados_tabela, headers=['Nome', 'Tipo', 'Valor', 'Categoria', 'Data'], tablefmt='rst')
        print(tabela)

    def total_despesas(self):
        """
            -> Faz a soma dos valores de cada despesa, retornando o valor total de despesas.
        :return: soma dos valores das despesas (total)
        """
        return sum(d.valor for d in self.despesas)

    def qtde_despesas(self):
        """
            -> Retorna a quantidade de despesas cadastradas.
        :return: tamanho da lista de despesas (quantidade de despesas cadastradas)
        """
        return len(self.despesas)

    def filtrar_por_mes(self, ano, mes):
        """
            -> Filtra as despesas, retornando aquelas em que a data inclui o mês e ano que foram passados.
        :param ano: ano das despesas
        :param mes: mês das despesas
        :return: uma lista com as despesas do período passado de parâmetro
        """
        return [despesa for despesa in self.despesas if despesa.ano == ano and despesa.mes == mes]