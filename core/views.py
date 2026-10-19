from django.shortcuts import render
from .models import Produto

def inicial(request):
    return render(request, 'index.html')

def produtos(request):
    Produtos = Produto.objects.all()
    context = {
        'todos_produtos': Produtos
    }
    return render(request, 'produtos.html', context)

def conserto(request):
    return render(request, 'conserto.html')
