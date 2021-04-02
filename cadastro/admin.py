from django.contrib import admin
from .models import Usuario, Segmento, Competencia



# Register your models here.

# Usuários
admin.site.register(Usuario)

# Segmento
admin.site.register(Segmento)

# Competências
admin.site.register(Competencia)