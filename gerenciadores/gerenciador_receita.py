from modelos.receita import Receita
from tabulate import tabulate


class GerenciadorReceita:
    def __init__(self):
        self.receitas = []

    def cadastrar_receita(self, nome, tipo, valor, categoria, data):
        receita = Receita(nome, tipo, valor, categoria, data)
        self.receitas.append(receita)
        print(f'\033[32mReceita {receita.nome} cadastrada com sucesso!\033[m')

    def listar_receitas(self):
        for r in self.receitas:
            print(f'{r.nome} - R$ {r.valor:.2f} - {r.data}')

    def relatorio_receitas(self):
        dados_tabela = []
        for r in self.receitas:
            dados_tabela.append(r.dados_relatorio())
        tabela = tabulate(dados_tabela, headers=['Nome', 'Tipo', 'Valor', 'Categoria', 'Data'], tablefmt='rst')
        print(tabela)

    def total_receitas(self):
        return sum(r.valor for r in self.receitas)

    def qtde_receitas(self):
        return len(self.receitas)
