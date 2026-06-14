import os
import sys
import json
from dotenv import load_dotenv, find_dotenv
from analisaDadosPlanilha import AnalisaDadosPlanilha
from enviaEmail import EnviaEmail
from verificaArquivosDiretorio import VerificarArquivosDiretorio


sys.path.append(r"c:\rpa\Python")

from Classes.Hangouts.Hangouts.Hangouts import Hangouts
from Classes.ZimbraMailer.ZimbraMailer.Zimbra import ZimbraMailer


# Obtém o caminho do diretório onde o script está localizado
script_dir = os.path.dirname(os.path.abspath(__file__))
# Procura o .env a partir do diretório do script
dotenv_path = find_dotenv(os.path.join(script_dir, '.env'))
load_dotenv(dotenv_path)
  

def verificar_arquivos_validos(verificador):
    pass # Logica de negocio removida por seguranca corporativa



def processar_envio_email(verificador):
    pass # Logica de negocio removida por seguranca corporativa



def analisa_arquivos():
    pass # Logica de negocio removida por seguranca corporativa
