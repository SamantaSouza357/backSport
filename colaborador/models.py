from django.db import models

# Create your models here.



class Colaborador(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    idade = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)

    def __str__(self):
        return self.nome




