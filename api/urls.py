from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.app.musicology.api import viewsets as notasviewsets

route = routers.DefaultRouter()
route.register(r'notas', notasviewsets.notas_piano_frequencia_ViewSet, basename ="Notas")



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
