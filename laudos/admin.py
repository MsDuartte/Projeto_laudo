from django.contrib import admin
from .models import Laudo

@admin.register(Laudo)
class LaudoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'user', 'data_criacao')
    search_fields = ('titulo', 'user__username')
    list_filter = ('data_criacao', 'user')

# Se você ainda não tiver registrado o modelo LaudoTemplate, você pode fazer isso também:
from .models import LaudoTemplate

@admin.register(LaudoTemplate)
class LaudoTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    search_fields = ('name', 'user__username')
    list_filter = ('user',)
