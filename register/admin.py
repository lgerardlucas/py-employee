from django.contrib import admin
from .models import Register
from django.contrib.auth.models import Group, User

admin.site.site_header = 'Área Administrativa'
admin.site.index_title = 'Sistema para Controle de Funcionários'

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_diplay_links = ('name',)

admin.site.register(Register,RegisterAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)
