## Depoly no Heroku

### Configurações iniciais
1. Criar uma conta no Heroku (https://www.heroku.com/)
2. Instalar a CLI do Heroku (https://devcenter.heroku.com/articles/heroku-cli)
3. Verificar a Instalação
```
heroku --version
```
4. Abrir o seu projeto e ativar o ambiente virutal.
```
source venv/bin/activate
```
5. Instalar a biblioteca  Django-environ
```
pip install django-environ
```
6. Instalar o whitenoise
```
pip install whitenoise
```


### Modificação dos arquivos do Projeto

#### 01 - Personalizar o settings
> Para a melhor compreensão dos modelos adotados nesta prática sugerimos a leitura:
(https://12factor.net/pt_br/)
1. Criar a pasta settings no  diretório do projeto
2. Criar o arquivo producao.py
``` python
import environ # Carrega a Biblioteca Django-environ
# importar o arquivo settings original
from api.settings.dev import *

#Criar uma instancia da classe Env
env = environ.Env()

#Suscrever as variáveis de ambiente

# OBS: são Strings e DEBUG espera um boleano
# Já passo um parâmetro default False
DEBUG = env.bool("DEBUG", False) 

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

DATABASES = {
    "defaut": env.db()
}

```
3. Mover o arquivo settings.py para esta pasta e renomear para dev.py
Atualizar a localização do dev.py
``` python
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
```
Configuração do whitenoise (Servir arquivos estáticos). [Documentação](http://whitenoise.evans.io/en/stable/)
``` python 
import os

MIDDLEWARE = [
  # 'django.middleware.security.SecurityMiddleware',
  'whitenoise.middleware.WhiteNoiseMiddleware',
  # ...
  # Acrescentar ao final do arquivo
  STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
  STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
]
```

#### 02 - Reconhecer os Ambientes

1. Configurar o arquivo wsgi.py
```python
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings.dev')

application = get_wsgi_application()
```
2. Alterar o arquivo manage.py
``` python
 """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings.dev')
```

#### 03 - Especificidadas do Heroku
1. Criar o arquivo requeriments.txt
```
pip freeze > requirements.txt
```
Adicionar ao arquivo as dependencias necessarias para produção:
``` python 
# Servidor wsgi recomendado pelo Heroku (Não copiar esta linha)
gunicorn==20.0.4
# Adaptador de Postgres para o Python (Não copiar esta linha)
psycopg2==2.8.5 

```
2. Criar o arquivo runtime.txt
```
python-3.8.6
```
3. Criar o arquivo Procfile
```
release: python3 manage.py migrate
web: gunicorn api.wsgi --preload --log-file -
```
#### 04 - Comandos Necessarios para o Deploy
1. Fazer login no Heroku
```
heroku login
```
2. Criar um app 
```
heroku create "nomedoapp"
```
3. Configurar as variáveis de ambiente
```
heroku config:set DEBUG=False
heroku config:set DJANGO_SETTINGS_MODULES=api.settings.producao
heroku config:set ALLOWED_HOSTS=nomegeradopeloheroku
heroku config:set SECRET_KEY=suakey

```
4. Criar o banco de dados
```
heroku addons:create heroku-postgresql:hobby-dev
```
5. Colocar a aplicação no ar
```
git push heroku master
```
6. Abrir a aplicação
```
heroku open
```
7. Entrar no bash remoto
```
heroku run bash
```