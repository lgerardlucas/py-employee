from django.contrib import admin
from .models import Register

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department')
    list_diplay_links = ('name',)
admin.site.register(Register,RegisterAdmin)
