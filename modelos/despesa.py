from datetime import datetime


class Despesa:
    def __init__(self, nome, tipo, valor, categoria, data):
        self.nome = nome
        self.tipo = tipo
        self.valor = valor
        self.categoria = categoria
        self.data = datetime.strftime(data, '%d/%m/%y')

    def dados_relatorio(self):
        return [self.nome, self.tipo, self.valor, self.categoria, self.data]