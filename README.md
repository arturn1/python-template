# Python API

## Instalação

### Ambiente Virtual Python (venv)

Primeiramente, é necessário criar um ambiente virtual Python (venv). Caso não tenha o pacote `venv` instalado, use o comando `sudo apt install python3-venv`.

Para criar o ambiente virtual, execute o comando abaixo no diretório do projeto:

```python3 -m venv system-env```

Ative o ambiente virtual com:

```source ./system-env/Scripts/activate```

Instale as dependências necessárias para o projeto usando o arquivo `requirements.txt`:

```pip install -r requirements.txt```

### Docker

Caso prefira usar o Docker, é possível construir uma imagem a partir do Dockerfile fornecido e rodar o container.

Para construir a imagem do Docker, navegue até o diretório do projeto e execute:

```docker build -t datatrade-python .```

Para rodar o container, use o comando:
```docker run -p 8000:8000 datatrade-python```

Este comando irá executar a aplicação no container, mapeando a porta 8000 do host para a porta 8000 do container.

## Execução

Para iniciar a aplicação, você pode usar um dos seguintes comandos:

Se você estiver usando o ambiente virtual:

```flask run```

Se você estiver usando Docker:

```docker run -p 8000:8000 datatrade-python```

Estes comandos irão iniciar a aplicação e ela estará acessível no endereço http://`localhost:8000`.

## Configuração

A configuração do projeto é feita por meio de variáveis de ambiente, que podem ser configuradas no arquivo `.env` ou diretamente no seu ambiente. Essas variáveis incluem:

- `FLASK_APP`: O ponto de entrada da aplicação Flask.
- `FLASK_RUN_PORT`: A porta na qual a aplicação será executada.
- `FLASK_ENV`: O ambiente no qual a aplicação está sendo executada.
- `USE_CACHE`: Uma flag para indicar se a aplicação deve usar cache ou não.
- `PYTHONDONTWRITEBYCODE`: Uma flag usada pelo Python.

## Licença

Este projeto está sob a licença ISC. Veja o arquivo LICENSE para mais detalhes.