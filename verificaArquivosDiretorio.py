import os
import sys
import json
import random
from dotenv import load_dotenv, find_dotenv
from consultaPG import ConsultaPG

sys.path.append(r"c:\rpa\Python")

from Classes.Hangouts.Hangouts.Hangouts import Hangouts
from Classes.MoverArquivos.MoverArquivos.HubArquivos import HubArquivos
from Classes.ZimbraMailer.ZimbraMailer.Zimbra import ZimbraMailer


class VerificarArquivosDiretorio:
    # Obtém o caminho do diretório onde o script está localizado
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Procura o .env a partir do diretório do script
    dotenv_path = find_dotenv(os.path.join(script_dir, '.env'))
    load_dotenv(dotenv_path)

    def __init__(self):
        pass # Logica de negocio removida por seguranca corporativa



    def verificar_arquivos_representantes(self):
        pass # Logica de negocio removida por seguranca corporativa

            
        
    def verificar_arquivos_validar(self):
        pass # Logica de negocio removida por seguranca corporativa

            

    def mover_arquivo_processado_com_sucesso(self, nome_arquivo_original, caminho_origem_completo, saldo_total):
            pass # Logica de negocio removida por seguranca corporativa


    
    def verificar_arquivos_email_enviado(self):
        pass # Logica de negocio removida por seguranca corporativa

            

if __name__ == "__main__":
    print("a")