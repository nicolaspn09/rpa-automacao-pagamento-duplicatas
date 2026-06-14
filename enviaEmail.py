import os
import sys
import gspread
import requests
import pandas as pd
from datetime import datetime
from google.oauth2.service_account import Credentials
from google.auth.transport.requests import Request as AuthRequest

sys.path.append(r"c:\rpa\Python")

from Classes.ZimbraMailer.ZimbraMailer.Zimbra import ZimbraMailer


class EnviaEmail:
    def __init__(self, credenciais_json):
        pass # Logica de negocio removida por seguranca corporativa



    def _gerar_tabela_html(self, dados):
        pass # Logica de negocio removida por seguranca corporativa

    

    def processar_e_enviar(self, alvo, destinatarios, destinatarios_copia, eh_gsheet=False):
        pass # Logica de negocio removida por seguranca corporativa
