from django.db import models

# Create your models here.

from django.db import models

class Medico(models.Model):
    id_medico = models.AutoField(primary_key=True)  # Chave primária inteira autoincrementada
    nome = models.CharField(max_length=100)  # Campo de texto para o nome do médico
    endereco = models.TextField()  # Campo de texto para o endereço do médico
    telefone = models.CharField(max_length=20)  # Campo de texto para o telefone do médico
    email = models.EmailField()  # Campo de e-mail para o e-mail do médico
    data_nascimento = models.DateField()  # Campo de data para a data de nascimento do médico
    crm = models.CharField(max_length=20)  # Campo de texto para o CRM do médico
    especialidade = models.ForeignKey('Especialidade', on_delete=models.CASCADE)  # Chave estrangeira para a especialidade do médico

    def __str__(self):
        return self.nome
    
    
class Especialidade(models.Model):
    id_especialidade = models.AutoField(primary_key=True)  # Chave primária inteira autoincrementada
    nome = models.CharField(max_length=100)  # Campo de texto para o nome da especialidade
    descricao = models.TextField()  # Campo de texto para a descrição da especialidade

    def __str__(self):
        return self.nome


