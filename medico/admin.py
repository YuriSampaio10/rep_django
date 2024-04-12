from django.contrib import admin
from .models import Medico, Especialidade

# Registrando os modelos para serem gerenciados pelo admin
admin.site.register(Medico)
admin.site.register(Especialidade)

