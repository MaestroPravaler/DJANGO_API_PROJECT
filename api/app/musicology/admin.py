from django.contrib import admin
from .models import * # IMPORTAR MINHAS APPS

class notas_piano_frequencia_admin(admin.ModelAdmin):
    # LISTAR O QUE APARECE
    list_display = ('notas_nome', 'notas_numero_tecla', 'notas_frequencia')
    # FILTROS
    list_filter = ('notas_nome', 'notas_numero_tecla', 'notas_frequencia')
    # SOMENTE LEITURA
    readonly_fields = ('notas_data_insere',)
    fieldsets = (
        (u"NOTAS / CARACTERISTICAS", {'fields' : ('notas_nome', 'notas_numero_tecla', 'notas_frequencia', 'notas_data_insere')}),
    )
# ==================== REGISTRO MODELS ==================
admin.site.register (notas_piano_frequencia, notas_piano_frequencia_admin)
# =======================================================   


