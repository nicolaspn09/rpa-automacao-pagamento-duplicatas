import re
import pandas as pd
from consultaOracle import ConsultaOracle
from consultaPG import ConsultaPG
import gspread


class AnalisaDadosPlanilha:
    def __init__(self, caminho_planilha, credenciais_google=None):
        pass # Logica de negocio removida por seguranca corporativa



    def _detectar_tipo_arquivo(self):
        pass # Logica de negocio removida por seguranca corporativa



    def _limpar_moeda(self, valor):
        pass # Logica de negocio removida por seguranca corporativa

        

    def _limpar_cnpj(self, cnpj):
        pass # Logica de negocio removida por seguranca corporativa



    def _ler_dados(self, sheet_name, cols_indices, col_names):
        pass # Logica de negocio removida por seguranca corporativa



    def obter_lista_tarefas(self):
        pass # Logica de negocio removida por seguranca corporativa



    def processar_abatimentos_e_gerar_guia(self):
        pass # Logica de negocio removida por seguranca corporativa



    def _formatar_linha(self, dup, valor, cnpj, id_cli, nome):
        pass # Logica de negocio removida por seguranca corporativa

    

    def _salvar_resultado(self, df_base):
        pass # Logica de negocio removida por seguranca corporativa
