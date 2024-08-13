# seu_app/forms.py

from django import forms

class InscricaoForm(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    telefone = forms.CharField(max_length=15)
    mensagem = forms.CharField(widget=forms.Textarea, required=False)
