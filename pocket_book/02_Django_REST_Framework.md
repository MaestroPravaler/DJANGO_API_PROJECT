## DJANGO REST FRAMEWORK

#### 00 - Git Flow - Criar a Feature 
```
git flow feature start "nomedafeature"
```
#### 01 - Criar o app
Criar uma pasta de nome app no diretorio do projeto.
```
django-admin startapp "nomedoapp"
```
#### 02 - Arquivo (settings.py) 
Instalar os apps
```
apps.musicology,
rest_framework,
```
#### 03 - Configurar (models.py)
```
from django.db import models

class notas_piano_frequencia(models.Model):
    notas_nome = models.CharField(max_length=255)
    notas_numero_tecla = models.IntegerField()
    notas_frequencia = models.IntegerField()
    notas_data_insere = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = u"Notas Musicais e as Teclas do Piano"
        ordering = ('notas_nome',)
    def __str__(self):
        return self.notas_nome
```  
#### 04 - Registrar os Models (admin.py)
```
from django.contrib import admin
from .models import * # IMPORTAR MINHAS APPS

class notas_piano_frequencia_admin(admin.ModelAdmin):
    # LISTA QUE VAI APARECER NO ADMIN
    list_display = ('notas_nome', 'notas_numero_tecla', 'notas_frequencia')
    # LISTA LATERAL QUE FILTRA POR CAMPO
    list_filter = ('notas_nome', 'notas_numero_tecla', 'notas_frequencia')
    # LISTA DE CAMPOS SOMENTE LEITURA
    readonly_fields = ('notas_data_insere',)
    fieldsets = (
        (u'NOTAS MUSICAIS - CARACTERÍSTICAS', {'fields' : ('notas_nome', 'notas_numero_tecla', 'notas_frequencia', 'notas_data_insere')}),
    )

#  ==================== REGISTRO DOS MODELS ==============================================
admin.site.register (notas_piano_frequencia, notas_piano_frequencia_admin)
# ===================================================================================
```
#### 05 - Na pasta da aplicação criar a pasta (api)
criar os arquivos (serializers.py) e (viewsets.py)
#### 06 - Arquivo (serializers.py)
```
from rest_framework import serializers
from api.app.musicology import models

class notas_piano_frequencia_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.notas_piano_frequencia
        fields = ('id', 'notas_nome', 'notas_numero_tecla', 'notas_frequencia', 'notas_data_insere',)
```     
#### 07 - Arquivo (viewsets.py)
```
from rest_framework import viewsets
from api.app.musicology.api import serializers
from api.app.musicology import models

class notas_piano_frequencia_ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.notas_piano_frequencia_Serializer
    queryset = models.notas_piano_frequencia.objects.all()
```
#### 08 - CONFIGURAR MINHAS ROTAS (urls.py)
```
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from api.app.musicology.api import viewsets as notasviewsets

route = routers.DefaultRouter()

route.register(r'notas', notasviewsets.notas_piano_frequencia_ViewSet, basename="Notas")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
```
#### 09 - Git Flow (merge até a master)
