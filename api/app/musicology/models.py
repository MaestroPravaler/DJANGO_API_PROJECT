from django.db import models

class notas_piano_frequencia(models.Model):
    notas_nome = models.CharField(max_length=255)
    notas_numero_tecla = models.IntegerField()
    notas_frequencia = models.IntegerField()
    notas_data_insere = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name = u"Notas X Piano X Frequencia"
        ordering = ('notas_nome',)
    def __str__(self):
        return self.notas_nome
