from dataclasses import field
from django import forms
from controle.models import Dados_c

class DadosForm(forms.ModelForm):
    class Meta:
        model = Dados_c
        fields = '__all__'