from googleapiclient.discovery import build
import pandas as pd
from dotenv import load_dotenv
import os

# CARREGAR VARIÁVEIS DE AMBIENTE DO ARQUIVO .env
load_dotenv()

# CONFIGURAÇÕES
API_KEY = os.getenv('API_KEY') # Certifique-se de que a variável API_KEY está definida no arquivo .env
PLAYLIST_ID = 'PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

# CONEXÃO COM A API
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)
