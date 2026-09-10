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
    return render(
request, 'acervo/lista.html',
{'livros': livros}
)

def novo_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save() # grava no banco
            return redirect('lista')
        else:
            form = LivroForm()

        return render(request, 'acervo/form.html', {'form': form})

