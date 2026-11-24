import os
from django.conf import settings
from django.db import models
from django.templatetags.static import static
from PIL import Image


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class ItemCardapio(models.Model):
    categoria = models.ForeignKey(
        "Categoria",
        on_delete=models.CASCADE,
        related_name="itens",
    )
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to="cardapio/", blank=True, null=True)

    def __str__(self):
        return self.nome

    @property
    def imagem_segura_url(self):
        """
        Retorna a URL da imagem em media/ se existir fisicamente.
        Caso contrário, busca em static/images/ ou usa o logo da cantina.
        """
        if self.imagem:
            try:
                if os.path.exists(self.imagem.path):
                    return self.imagem.url
            except ValueError:
                pass

            # Fallback: verifica se existe arquivo com mesmo nome em static/images/
            nome_arquivo = os.path.basename(self.imagem.name)
            caminho_static = settings.BASE_DIR / "static" / "images" / nome_arquivo
            if os.path.exists(caminho_static):
                return static(f"images/{nome_arquivo}")

        return static("images/amaral-cantina-logo.jpeg")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.imagem:
            try:
                caminho = self.imagem.path
                if os.path.exists(caminho):
                    with Image.open(caminho) as img:
                        if img.height > 500 or img.width > 500:
                            img.thumbnail((500, 500), Image.Resampling.LANCZOS)
                            img.save(caminho)
            except Exception:
                # Impede que falhas de arquivo quebrem o salvamento no Admin
                pass