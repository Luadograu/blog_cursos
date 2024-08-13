from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'cursos/index.html')

def cursos(request):
    return render(request, 'cursos/cursos.html')

def alimentos(request):
    return render(request, 'cursos/alimentos.html')

def quimica(request):
    return render(request, 'cursos/quimica.html')

def ads(request):
    return render(request, 'cursos/ads.html')

def inscricoes(request):
    return render(request, 'cursos/inscricao.html')

# seu_app/views.py

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import InscricaoForm  # Assumindo que você tenha um formulário Django Forms

def inscricao(request):
    if request.method == 'POST':
        form = InscricaoForm(request.POST)
        if form.is_valid():
            # Processar os dados do formulário
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            telefone = form.cleaned_data['telefone']
            mensagem = form.cleaned_data['mensagem']
            
            # Exemplo: Enviar um e-mail
            send_mail(
                'Nova Inscrição no Curso de Química',
                f'Nome: {nome}\nE-mail: {email}\nTelefone: {telefone}\nMensagem: {mensagem}',
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            
            # Redirecionar para uma página de sucesso ou confirmação
            return redirect('inscricao_sucesso')
    else:
        form = InscricaoForm()
    
    return render(request, 'inscricao.html', {'form': form})
