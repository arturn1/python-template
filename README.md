# Python API

## Dependências

```
aniso8601==9.0.1
blinker==1.7.0
certifi==2023.11.17
charset-normalizer==3.3.2
click==8.1.7
colorama==0.4.6
dynaconf==3.2.4
Flask==3.0.1
Flask-Cors==4.0.0
Flask-RESTful==0.3.10
idna==3.6
itsdangerous==2.1.2
Jinja2==3.1.3
MarkupSafe==2.1.4
python-dotenv==1.0.0
pytz==2023.3.post1
requests==2.31.0
schedule==1.2.1
six==1.16.0
urllib3==2.1.0
Werkzeug==3.0.1
```

## Instalação

### Ambiente Virtual Python (venv)

Primeiramente, é necessário criar um ambiente virtual Python (venv). Caso não tenha o pacote `venv` instalado, use o comando `sudo apt install python3-venv`.

Para criar o ambiente virtual, execute o comando abaixo no diretório do projeto:

```python -m venv system-env```

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