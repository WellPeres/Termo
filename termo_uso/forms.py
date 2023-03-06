from django import forms

from .models import TermoDeUsoEquipamento

    
class TermoModelForm(forms.ModelForm):
    class Meta:
        model = TermoDeUsoEquipamento
        fields = ['funcionario', 'nome_pc', 'ssd', 'memoria', 'tipo', 'monitor1', 'monitor2', 'perifericos', 'arquivo', 'observacao']