from django.db import models
from django.contrib.auth.models import User

class LaudoTemplate(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'user')  # Garante que a combinação de nome e usuário seja única

    def save(self, *args, **kwargs):
        # Converte o nome para minúsculas antes de salvar
        self.name = self.name.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Laudo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo