class Receita:
    def __init__(self, nome, tipo, valor, categoria, data):
        self.nome = nome
        self.tipo = tipo
        self.valor = valor
        self.categoria = categoria
        self.data = data
        self.ano = data.year
        self.mes = data.month

    def dados_relatorio(self):
        return [self.nome, self.tipo, self.valor, self.categoria, self.data.strftime('%d/%m/%Y')]