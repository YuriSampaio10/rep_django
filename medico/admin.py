from django.contrib import admin
from .models import Person, Medico

# Registrando os modelos para serem gerenciados pelo admin
admin.site.register(Person)
admin.site.register(Medico)

