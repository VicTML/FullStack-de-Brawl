from django.shortcuts import redirect, render

# Create your views here.
from django.http import HttpResponse, request

from acervo.forms import LivroForm
def inicio(request):
    return HttpResponse(
    'Acervo do Brawl Ainda Ativo!'
    )

from .models import Livro

def lista_livros(request):
    livros = Livro.objects.all()

    nome_query = request.GET.get('nome')
    tipo_query = request.GET.get('tipo')
    categoria_query = request.GET.get('categoria')

    if nome_query:
        livros = livros.filter(titulo__icontains=nome_query)
    if tipo_query:
        livros = livros.filter(tipo_acervo=tipo_query)
    if categoria_query:
        livros = livros.filter(categoria=categoria_query)

    return render(request, 'acervo/lista.html', {'livros': livros})

def novo_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('novo_livro')
    else:
        form = LivroForm()

    return render(request, 'acervo/form.html', {'form': form})