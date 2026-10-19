from django.db import models

class Produto(models.Model):
    nome = models.CharField('Nome do Produto', max_length= 100)
    preco = models.DecimalField('Preço do Produto', max_digits= 8, decimal_places=2,)
    tipo = models.CharField('Tipo do Produto', max_length= 100)
    quantidade = models.IntegerField('Quantidade do Produto', default=0)

class CadastrarMoto(models.Model):
    modelo = models.CharField('Modelo da moto', max_length=100)
    quilometragem = models.IntegerField('Quilometragem da moto', max_digits=6, decimal_places=2)
    ano = models.IntegerField('Ano da moto', max_digits=4)
    problema = models.CharField('Problema(s) da moto', max_length=100)