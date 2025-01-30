from django import forms
from .models import LaudoTemplate, Laudo

class LaudoForm(forms.ModelForm):
    class Meta:
        model = Laudo
        fields = ['titulo', 'conteudo']
        

class LaudoTemplateForm(forms.ModelForm):
    class Meta:
        model = LaudoTemplate
        fields = ['name', 'content']