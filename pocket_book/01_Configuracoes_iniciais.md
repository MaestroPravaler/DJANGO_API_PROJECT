
## ORGANIZANDO O ESPAÇO DE TRABALHO

### Requisitos

#### 01 - Verificar a Instalação do Python
```
python3 --version
sudo apt install python3
```
#### 02 - veirficar a instalação do pip
```
pip --version
sudo apt-get install python3-pip
```

#### 03 - Verificar a instalação do Virtualenv
```
sudo apt install python3-virtualenv
```

## Preparando o Ambiente

#### 00 - Inicializar o Diretòrio com o Git Flow
```
git flow init
criar o arquivo .gitignore
```

#### 01 - Criar uma VirtualEnv
```
python3 -m venv "nomedavenv"
```

#### 02 - Ativar o Ambiente Virtual
```
source nomedavenv/bin/activate
```

#### 03 - Instalar as Dependencias
```
pip install django
pip install djangorestframework
```

#### 04 - Criar o Projeto
```
django-admin startproject "nomedoseuprojeto" .
```

#### 05 - Criar a área de administração e as tabelas iniciais
```
python3 manage.py migrate
```

#### 06 - Criar o Super Usuário
```
python3 manage.py createsuperuser
```

#### 07 - Rodar a aplicação
```
python3 manage.py runserver
```

## Finalizando o Projeto

#### 01 - Finalizar a Feature
```
git flow feature finish "nomedafeature"
```

#### 02 - Criar a Release
```
git flow release start "numerodarelease"
```
#### 03 - Finalizar a Release
```
git flow release finish "numerodarelease"
```
#### 04 - Subir para o Github (caso exista)
