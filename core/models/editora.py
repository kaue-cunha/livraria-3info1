from django.db import models

class Editora(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)  # Campo adicionado
    cidade = models.CharField(max_length=255, blank=True, null=True)  # Opcional, caso queira cidade

    def __str__(self):
        return self.nome