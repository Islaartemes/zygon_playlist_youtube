# 🎥 Coleta e Armazenamento de Dados de uma Playlist do YouTube

Este projeto foi desenvolvido como parte de um desafio técnico com o objetivo de demonstrar habilidades práticas em Python, integração com APIs, tratamento de dados, exportação em CSV e criação de dashboards. O projeto também realiza a integração com o BigQuery.

---

## 🎯 Objetivo

Avaliar habilidades de:

- Codificação e boas práticas
- Organização e clareza do código
- Uso de APIs reais
- Estrutura de uma solução funcional e escalável
- Criação de visualizações a partir dos dados coletados

---

## 📝 Descrição do Desafio

Desenvolver uma solução em Python que:

- Consuma dados da playlist pública abaixo utilizando a YouTube Data API:  
  🎵 [YouTube Playlist](https://www.youtube.com/playlist?list=PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj)

- Faça o tratamento dos dados (quando necessário)
- Exporte os dados para um arquivo `.csv`
- Produza um **dashboard** (Power BI ou Looker Studio)
- Envie os dados para o **BigQuery**

---

## 📌 Dados obrigatórios coletados

- ID do vídeo  
- Título  
- Descrição  
- Data de publicação  
- Quantidade de likes  
- Quantidade de views  
- Quantidade de comentários  
- URL da thumbnail  

---

## 💡 Tecnologias utilizadas

- Python 3
- YouTube Data API v3
- Google Cloud BigQuery
- Pandas
- Dotenv
- Power BI 
- Google Cloud Platform

---

## 🧰 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/Islaartemes/zygon_playlist_youtube
cd zygon_playlist_youtube
```
### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Adicione a API Key ao .env
```bash
API_KEY=sua_chave_da_api_aqui
```

### 4. Adicione o arquivo de credenciais do BigQuery
```bash
Gere uma Service Account Key em JSON com acesso ao BigQuery
```

## ▶️ Execução
Rode o script principal:
python youtube.py

O script irá:

Conectar à API do YouTube

Coletar e tratar os dados da playlist

Salvar os dados em youtube_playlist_data.csv

Enviar os dados para o BigQuery

## 👩‍💻 Autora
Isla Artemes
