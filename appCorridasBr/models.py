from django.db import models

# Create your models here.
class Usuario(models.Model):
    cpf = models.CharField(max_length=11,primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    senha = models.IntegerField()