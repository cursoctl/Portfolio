
from django.shortcuts import render, get_object_or_404
from .models import Projeto, Experiencia, Categoria

def index(request):
    projetos = Projeto.objects.all()
    return render(request, 'portfolio_app/index.html', {'projetos': projetos})

def home(request):
    categorias = Categoria.objects.all()
    projetos = Projeto.objects.all()
    experiencias = Experiencia.objects.all()
    return render(request, 'portfolio_app/home.html', {  # Verifique o caminho
        'projetos': projetos,
        'categorias': categorias,
        'experiencias': experiencias,
    })
def filtro_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    projetos = Projeto.objects.filter(categoria=categoria)
    return render(request, 'portfolio_app/filtro_categoria.html', {  # Verifique o caminho
        'projetos': projetos,
        'categoria': categoria,
    })
def portfolio(request):
    return render(request, 'portfolio_app/portfolio.html')

def contato(request):
    return render(request, 'portfolio_app/contato.html')