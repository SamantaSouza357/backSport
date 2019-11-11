from django.db import models

# Create your models here.
from eventos.models import Eventos


class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    genero = models.CharField(max_length=255)
    esporte = models.ForeignKey(
        Eventos,
        on_delete=models.SET_NULL,
        null=True
    )

