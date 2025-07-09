from googleapiclient.discovery import build
from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd
from dotenv import load_dotenv
import os

# CARREGAR VARIÁVEIS DE AMBIENTE DO ARQUIVO .env
load_dotenv()

# CONFIGURAÇÕES
API_KEY = os.getenv('API_KEY') # A variável API_KEY está definida no arquivo .env
PLAYLIST_ID = 'PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

# CONEXÃO COM A API
def connect_youtube():
    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)

# COLETAR OS IDS DE TODOS OS VÍDEOS DA PLAYLIST
def get_video_ids(youtube, playlist_id):
    video_ids = []
    next_page_token = None

    while True:
        res = youtube.playlistItems().list(
            part = 'contentDetails',
            playlistId = playlist_id,
            maxResults = 50,
            pageToken = next_page_token
        ).execute()

        for item in res['items']:
            video_ids.append(item['contentDetails']['videoId'])

        next_page_token = res.get('nextPageToken')
        if not next_page_token:
            break

    return video_ids


# COLETAR INFORMAÇÕES DOS VÍDEOS
def get_video_details(youtube, video_ids):
    video_data = []

    for i in range(0, len(video_ids), 50):
        batch = video_ids[i:i + 50]
        res = youtube.videos().list(
            part='snippet,statistics',
            id=','.join(batch)
        ).execute()

        for item in res['items']:
            snippet = item['snippet']
            stats = item.get('statistics', {})

            video_data.append({
                'ID do video': item['id'],
                'Título': snippet.get('title'),
                'Descrição': snippet.get('description'),
                'Data de publicação': snippet.get('publishedAt'),
                'Quantidade de views': stats.get('viewCount', 0),
                'Quantidade de likes': stats.get('likeCount', 0),
                'Quantidade de comentários': stats.get('commentCount', 0),
                'URL da thumbnail': snippet['thumbnails']['high']['url']
            })

    return video_data

# SALVAR OS DADOS EM UM ARQUIVO CSV
def save_to_csv(data, file_name = 'youtube_playlist_data.csv'):
    df = pd.DataFrame(data)
    df.to_csv(file_name, index=False, encoding='utf-8-sig')
    print(f'Dados salvos em {file_name}')

# ENVIAR PARA BIGQUERY
def upload_to_bigquery(df, dataset_id, table_id, credential_path):
    credential = service_account.Credentials.from_service_account_file(credential_path)
    client = bigquery.Client(credentials=credential, project=credential.project_id)

    table_ref = f"{credential.project_id}.{dataset_id}.{table_id}"

    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        autodetect=True,
    )

    job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
    job.result()

    print(f'Dados enviados para BigQuery na tabela {table_ref}')


# FUNÇÃO MAIN
def main():
    youtube = connect_youtube()
    print("Conectado à API do YouTube com sucesso!")

    print("Coletando IDs dos vídeos da playlist...")
    video_ids = get_video_ids(youtube, PLAYLIST_ID)

    print (f"Total de vídeos encontrados: {len(video_ids)}")

    print("Coletando detalhes dos vídeos...")
    video_details = get_video_details(youtube, video_ids)

    print("Salvando dados no arquivo CSV...")
    save_to_csv(video_details)

    print("Carregando dados no BigQuery...")
    df = pd.DataFrame(video_details)
    upload_to_bigquery(
        df=df,
        dataset_id = 'youtube_dados',
        table_id = 'playlist_videos',
        credential_path = 'youtube-dados-465419-066cc76a75dd.json'
    )

if __name__ == '__main__':
    main()





