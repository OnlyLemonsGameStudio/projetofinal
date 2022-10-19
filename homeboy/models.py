from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Produto(models.Model):
    produto_nome = models.CharField(max_length=200)
    produto_preco = models.DecimalField(max_digits=6, decimal_places=2)