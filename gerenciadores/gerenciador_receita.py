from modelos.receita import Receita
from tabulate import tabulate


class GerenciadorReceita:
    def __init__(self):
        self.receitas = []

    def cadastrar_receita(self, nome, tipo, valor, categoria, data):
        """
            -> Realiza o cadastro de receitas.
        :param nome: nome da receita
        :param tipo: tipo da receita (fixa/variável)
        :param valor: valor da receita
        :param categoria: categoria da receita
        :param data: data da receita
        """
        receita = Receita(nome, tipo, valor, categoria, data)
        self.receitas.append(receita)
        print(f'\033[32mReceita {receita.nome} cadastrada com sucesso!\033[m')

    def listar_receitas(self):
        """
            -> Lista todas as receitas cadastradas, mostrando seu nome, valor e data.
        """
        for r in self.receitas:
            print(f'{r.nome} - R$ {r.valor:.2f} - {r.data.strftime("%d/%m/%Y")}')

    def relatorio_receitas(self):
        """
            -> Faz um relatório, em formato de tabela, com todas as receitas.
        """
        dados_tabela = []
        for r in self.receitas:
            dados_tabela.append(r.dados_relatorio())
        tabela = tabulate(dados_tabela, headers=['Nome', 'Tipo', 'Valor', 'Categoria', 'Data'], tablefmt='rst')
        print(tabela)

    def total_receitas(self):
        """
            -> Faz a soma dos valores de cada receita, retornando o valor total de receitas.
        :return: soma dos valores das receitas (total)
        """
        return sum(r.valor for r in self.receitas)

    def qtde_receitas(self):
        """
            -> Retorna a quantidade de receitas cadastradas.
        :return: tamanho da lista de receitas (quantidade de receitas cadastradas)
        """
        return len(self.receitas)

    def filtrar_por_mes(self, ano, mes):
        """
            -> Filtra as receitas, retornando aquelas em que a data inclui o mês e ano que foram passados.
        :param ano: ano das receitas
        :param mes: mês das receitas
        :return: uma lista com as receitas do período passado de parâmetro
        """
        return [receita for receita in self.receitas if receita.ano == ano and receita.mes == mes]