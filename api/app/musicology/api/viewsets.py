from rest_framework import viewsets
from api.app.musicology.api import serializers
from api.app.musicology import models

class notas_piano_frequencia_ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.notas_piano_frequencia_Serializer
    queryset = models.notas_piano_frequencia.objects.all()