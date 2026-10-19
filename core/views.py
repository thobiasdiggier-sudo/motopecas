from django.shortcuts import render, redirect
from .models import Produto, CadastrarMoto
from .forms import ProdutoForm, CadastrarMotoForm

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


def cadastrar_motos(request):
    form = CadastrarMotoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('consertos')

    context = {
        'form_cadastrarMotos': form
    }
    return render(request, 'cadastrar_motos.html', context)