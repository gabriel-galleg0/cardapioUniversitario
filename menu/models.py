from django.db import models
from PIL import Image

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class ItemCardapio(models.Model):
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, related_name="itens")
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to="cardapio/", blank=True, null=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.imagem:
            img = Image.open(self.imagem.path)
            max_size = (500, 500)
            img.thumbnail(max_size, Image.Resampling.LANCZOS)
            img.save(self.imagem.path)
            