import json
import logging
import os
import pandas as pd
from azure.storage.blob import BlobServiceClient
import azure.functions as func

# Função para carregar dados do JSON
def load_json_data(json_str):
    return json.loads(json_str)

# Função para salvar dados em Parquet
def save_to_parquet(data, parquet_file):
    df = pd.DataFrame(data)
    df.to_parquet(parquet_file, index=False)

# Função para fazer upload do arquivo Parquet para Azure Blob Storage
def upload_to_azure_blob(parquet_file, container_name, blob_name, connection_string):

    parquet_file =''
    container_name = ''
    blob_name =''
    connection_string =''

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    with open(parquet_file, "rb") as data:
        blob_client.upload_blob(data)

# Função principal
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processando requisição...')

    # Obter dados do JSON do corpo da requisição
    json_data = req.get_body().decode('utf-8')
    
    # Parâmetros de configuração
    parquet_file = '/tmp/dados.parquet'                            # Usando /tmp para armazenamento temporário
    container_name = 'seu-container'                               # Nome do seu container
    blob_name = 'dados/dados.parquet'                              # Nome do blob no Azure
    connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')  # String de conexão do Azure Blob Storage

    try:
        # Processar dados
        data = load_json_data(json_data)                                                  # Carrega o JSON
        save_to_parquet(data, parquet_file)                                                   # Salva como Parquet
        upload_to_azure_blob(parquet_file, container_name, blob_name, connection_string)  # Faz upload para o Azure

        return func.HttpResponse("Dados processados e enviados com sucesso!", status_code=200)

    except Exception as e:
        logging.error(f'Erro: {str(e)}')
        return func.HttpResponse("Erro ao processar os dados.", status_code=500)
