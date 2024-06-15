# RamenGO

## Tecnologias Utilizadas

![Python Version](https://img.shields.io/badge/python-3.12-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16.0-blue)
![Docker](https://img.shields.io/badge/Docker-25.0-blue)

---

## Objetivo do Projeto

O objetivo deste projeto é desenvolver a API RamenGO, uma plataforma que permite aos usuários montar um pedido de ramen, escolhendo entre diversos tipos de caldo e proteínas.

## Como Executar

### Configuração do Arquivo .env

Para iniciar, é necessário ter Python 3.12 e PostgreSQL 16 instalados no ambiente de desenvolvimento. Após a instalação, preencha o arquivo `.env` com as seguintes informações para conectar ao banco de dados:

```env
POSTGRES_USER=seu_usuario
POSTGRES_PASSWORD=sua_senha
POSTGRES_DB=nome_do_banco
POSTGRES_SCHEMA=nome_do_esquema
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
PATH_LOGGER=../loggers/log.log
X_API_KEY=sua_api_key
```

### Execução Manual

1. **Criação do Ambiente Virtual**  
   Crie um ambiente virtual para instalar as dependências do projeto:

   ```sh
   python3.12 -m venv .venv
   ```

2. **Instalação das Dependências**  
   Ative o ambiente virtual e instale as dependências:

   ```sh
   source .venv/bin/activate  # Para Linux/MacOS
   .venv\Scripts\activate  # Para Windows
   pip install -r requirements.txt
   ```

3. **Migração do Banco de Dados**  
   Gere e aplique as migrações do banco de dados:

   ```sh
   alembic revision --autogenerate -m "Criação da migração"
   alembic upgrade head
   ```

4. **Inserção de Dados Iniciais**  
   Insira os dados iniciais na base de dados:

   ```sh
   export PYTHONPATH=$(pwd)
   python src/database/inserts.py
   ```

5. **Iniciar o FastAPI**  
   Inicie a aplicação FastAPI:

   ```sh
   uvicorn src.main:app --reload
   ```

   A API estará disponível na porta 8000:

   ```sh
   http://localhost:8000/docs/
   ```

### Execução com Docker

1. **Build da Imagem Docker**  
   Certifique-se de ter Docker e docker-compose instalados. Construa a imagem:

   ```sh
   docker-compose build
   ```

2. **Subir Contêineres**  
   Inicie os contêineres:

   ```sh
   docker-compose up
   ```

   A aplicação estará disponível na porta 8000 do seu computador:

   ```sh
   http://localhost:8000/docs/
   ```
