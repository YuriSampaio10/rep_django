from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    
class Medico(models.Model):
    id_medico = models.IntegerField()  # Campo inteiro para o ID do médico
    dados = models.TextField()  # Campo de texto para os dados do médico