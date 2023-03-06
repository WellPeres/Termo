from django.contrib import admin

from .models import TermoDeUsoEquipamento

@admin.register(TermoDeUsoEquipamento)
class TermoAdmin(admin.ModelAdmin):
    list_display = ('funcionario', 'nome_pc', 'ssd', 'memoria', 'tipo', 'monitor1', 'monitor2', 'perifericos', 'slug', 'arquivo', 'observacao',
                    'criado', 'modificado')
