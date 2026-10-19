from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm

def inicial(request):
    return render(request, 'index.html')

def produtos(request):
    Produtos = Produto.objects.all()
    context = {
        'todos_produtos': Produtos
    }
    return render(request, 'produtos.html', context)

def cadastrar_produtos(request):
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('produtos')

    context = {
        'form_produto': form
    }
    return render(request, 'cadastrar_produtos.html', context)
