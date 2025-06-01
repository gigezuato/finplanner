import os
import pandas as pd


class ExportaExcel:
    def __init__(self, gerenciador_rec, gerenciador_desp, gerenciador_resumo_mensal, caminho_base='./exportados'):
        self.gerenciador_rec = gerenciador_rec
        self.gerenciador_desp = gerenciador_desp
        self.gerenciador_resumo_mensal = gerenciador_resumo_mensal
        self.caminho_base = caminho_base
        os.makedirs(self.caminho_base, exist_ok=True)

    @staticmethod
    def converter_para_dataframe(objetos):
        return pd.DataFrame([{
            'Nome': obj.nome,
            'Tipo': obj.tipo,
            'Valor': obj.valor,
            'Categoria': obj.categoria,
            'Data': obj.data.strftime('%d/%m/%Y')
        } for obj in objetos])

    def exportar_receitas(self, receitas):
        if not receitas:
            print('Não há receitas para exportar!')
            return

        df_receitas = self.converter_para_dataframe(receitas)

        nome_arquivo = 'todas_receitas.xlsx'
        caminho_completo = os.path.join(self.caminho_base, nome_arquivo)

        df_receitas.to_excel(caminho_completo, index=False)
        print(f'Receitas exportadas para "{caminho_completo}" com sucesso!')

    def exportar_despesas(self, despesas):
        if not despesas:
            print('Não há despesas para exportar!')
            return

        df_despesas = self.converter_para_dataframe(despesas)

        nome_arquivo = 'todas_despesas.xlsx'
        caminho_completo = os.path.join(self.caminho_base, nome_arquivo)

        df_despesas.to_excel(caminho_completo, index=False)
        print(f'Despesas exportadas para "{caminho_completo}" com sucesso!')

    def exportar_receitas_periodo(self, ano, mes):
        receitas_mes = self.gerenciador_rec.filtrar_por_mes(ano, mes)

        if not receitas_mes:
            print(f'Não há receitas de {mes:02d}/{ano} para exportar!')
            return

        df_receitas_mes = self.converter_para_dataframe(receitas_mes)

        nome_arquivo = f'receitas_{ano}_{mes:02d}.xlsx'
        caminho_completo = os.path.join(self.caminho_base, nome_arquivo)

        df_receitas_mes.to_excel(caminho_completo, index=False)
        print(f'Receitas exportadas para "{caminho_completo}" com sucesso!')

    def exportar_despesas_periodo(self, ano, mes):
        despesas_mes = self.gerenciador_desp.filtrar_por_mes(ano, mes)

        if not despesas_mes:
            print(f'Não há despesas de {mes:02d}/{ano} para exportar!')
            return

        df_depesas_mes = self.converter_para_dataframe(despesas_mes)

        nome_arquivo = f'depesas_{ano}_{mes:02d}.xlsx'
        caminho_completo = os.path.join(self.caminho_base, nome_arquivo)

        df_depesas_mes.to_excel(caminho_completo, index=False)
        print(f'Despesas exportadas para "{caminho_completo}" com sucesso!')