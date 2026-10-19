from django.forms import ModelForm
from .models import Produto, CadastrarMoto

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'tipo', 'quantidade']

class CadastrarMotoForm(ModelForm):
    class Meta:
        model = CadastrarMoto
        fields = ['modelo', 'quilometragem', 'ano', 'problema']
