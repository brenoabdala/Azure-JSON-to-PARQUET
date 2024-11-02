# Azure Function - Processamento e Upload de Dados em Parquet para o Azure Blob Storage

Este projeto é uma função do Azure Functions em Python que recebe dados JSON via requisição HTTP, processa esses dados, salva-os no formato Parquet e faz upload para o Azure Blob Storage.

## Estrutura do Projeto

- **main**: Ponto de entrada da função Azure Function. Recebe os dados JSON, processa-os, e faz o upload do arquivo Parquet para o Azure Blob Storage.
- **load_json_data**: Converte a string JSON recebida em um objeto Python.
- **save_to_parquet**: Salva os dados processados no formato Parquet.
- **upload_to_azure_blob**: Faz upload do arquivo Parquet para o Azure Blob Storage.

## Pré-requisitos

- Python 3.7 ou superior
- Conta no [Azure Blob Storage](https://azure.microsoft.com/pt-br/services/storage/blobs/) com o container criado
- [Azure Functions Core Tools](https://docs.microsoft.com/azure/azure-functions/functions-run-local) (para rodar a função localmente)

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Instale as dependências listadas no `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure a string de conexão do Azure Blob Storage como variável de ambiente:
    ```bash
    export AZURE_STORAGE_CONNECTION_STRING="sua-string-de-conexao"
    ```

## Configuração

No arquivo `main` da função:

- `container_name`: Nome do container do Azure Blob Storage onde o arquivo será salvo.
- `blob_name`: Caminho e nome do blob para o arquivo Parquet (exemplo: `dados/dados.parquet`).

## Executando Localmente

Para testar a função localmente, use o comando abaixo:

```bash
 func start

```

Você poderá enviar uma requisição HTTP para a função usando um cliente como o Postman ou curl. Exemplo de requisição:

```bash
curl -X POST http://localhost:7071/api/nome-da-sua-funcao \
    -H "Content-Type: application/json" \
    -d '{"chave1": "valor1", "chave2": "valor2"}'
```

Deploy no Azure
Faça login na sua conta do Azure:

```bash
az login
```
Crie o recurso do Azure Functions e faça o deploy:

``` bash
func azure functionapp publish <NOME_DA_SUA_APP_FUNCTION>
```
Exemplo de Uso
- Quando a função recebe uma requisição HTTP com um corpo JSON válido, ela:

- Carrega o JSON.
- Salva os dados no formato Parquet.
- Faz o upload para o Azure Blob Storage.
- Em caso de sucesso, a função retorna uma resposta com status 200 e a mensagem "Dados processados e enviados com sucesso!". Se houver algum erro, retorna uma mensagem de erro com o status 500.

