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
