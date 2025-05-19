from modelos.despesa import Despesa
from tabulate import tabulate


class GerenciadorDespesa:
    def __init__(self):
        self.despesas = []

    def cadastrar_despesa(self, nome, tipo, valor, categoria, data):
        despesa = Despesa(nome, tipo, valor, categoria, data)
        self.despesas.append(despesa)
        print(f'\033[32mDespesa {despesa.nome} cadastrada com sucesso!\033[m')

    def listar_despesas(self):
        for d in self.despesas:
            print(f'{d.nome} - R$ {d.valor:.2f} - {d.data}')

    def relatorio_despesas(self):
        dados_tabela = []
        for d in self.despesas:
            dados_tabela.append(d.dados_relatorio())
        tabela = tabulate(dados_tabela, headers=['Nome', 'Tipo', 'Valor', 'Categoria', 'Data'], tablefmt='rst')
        print(tabela)

    def total_despesas(self):
        total = sum(d.valor for d in self.despesas)
        return total

    def qtde_despesas(self):
        return len(self.despesas)