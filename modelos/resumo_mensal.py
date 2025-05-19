class ResumoMensal:
    def __init__(self, ano, mes, receitas, despesas):
        self.ano = ano
        self.mes = mes
        self.receitas = receitas
        self.despesas = despesas
        self.porcentagens = {}

    def total_receitas(self):
        """
            -> Soma todas as receitas
        :return: a soma dos valores da receita
        """
        return sum(r.valor for r in self.receitas)

    def total_despesas(self):
        """
            -> Soma todas as despesas
        :return: a soma dos valores da despesa
        """
        return sum(d.valor for d in self.despesas)

    def saldo_mensal(self):
        """
            -> Saldo = Total de Receitas - Total de Despesas
        :return: o saldo mensal
        """
        return self.total_receitas() - self.total_despesas()

    def porc_categoria(self):
        """
            -> Calcula a porcentagem de despesa por categoria.
            -> Armazena a porcentagem como valor no dicionário porcentagens (atributo dessa classe),
            tendo como chave o nome de cada categoria.
        """
        total = self.total_despesas()
        categorias = {}

        for d in self.despesas:
            if d.categoria in categorias:
                categorias[d.categoria] += d.valor
            else:
                categorias[d.categoria] = d.valor

        for categoria, valor in categorias.items():
            self.porcentagens[categoria] = (valor / total) * 100

    def menor_categoria_despesa(self):
        """
            -> Verifica qual foi a categoria com menor gasto e a sua porcentagem em relação ao total de despesas.
        :return: o nome da categoria de menor gasto e a porcentagem
        """
        if not self.porcentagens:  # verifica se as porcentagens ainda não foram calculadas
            self.porc_categoria()  # calcula as porcentagens
        menor_categoria = min(self.porcentagens, key=self.porcentagens.get)  # armazena o nome da categoria
        menor_porcentagem = self.porcentagens[menor_categoria]  # armazena a menor porcentagem

        return menor_categoria, menor_porcentagem

    def maior_categoria_despesa(self):
        """
            -> Verifica qual foi a categoria com maior gasto e a sua porcentagem em relação ao total de despesas.
        :return: o nome da categoria de maior gasto e a porcentagem
        """
        if not self.porcentagens:  # verifica se as porcentagens ainda não foram calculadas
            self.porc_categoria()  # calcula as porcentagens
        maior_categoria = max(self.porcentagens, key=self.porcentagens.get)  # armazena o nome da categoria
        maior_porcentagem = self.porcentagens[maior_categoria]  # armazena a maior porcentagem

        return maior_categoria, maior_porcentagem

    def menor_gasto(self):
        """
            -> Verifica qual objeto de Despesa possui o menor valor (menor gasto)
        :return: o nome da despesa e o seu valor
        """
        if not self.despesas:  # verifica se ainda não há despesas cadastradas
            return None  # retorna none
        else:
            menor_despesa = min(self.despesas, key=lambda d: d.valor)  # armazena o objeto despesa com menor valor
            return menor_despesa.nome, menor_despesa.valor  # retorna nome da despesa e valor da despesa

    def maior_gasto(self):
        """
            -> Verifica qual objeto de Despesa possui o maior valor (maior gasto)
        :return: o nome da despesa e o seu valor
        """
        if not self.despesas:  # verifica se ainda não há despesas cadastradas
            return None  # retorna none
        else:
            maior_despesa = max(self.despesas, key=lambda d: d.valor)  # armazena o objeto despesa com maior valor
            return maior_despesa.nome, maior_despesa.valor  # retorna nome da despesa e valor da despesa