from django.contrib import admin

# Register your models here.
from.models import Dados_c
class dadosAdmin(admin.ModelAdmin):
    list_display = ['nome','cpf']


admin.site.register(Dados_c)