from rest_framework import serializers
from api.app.musicology import models

class notas_piano_frequencia_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.notas_piano_frequencia
        fields = ('id', 'notas_nome', 'notas_numero_tecla', 'notas_frequencia', 'notas_data_insere',)