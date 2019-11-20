from django.contrib import admin

# Register your models here.
from .models import Campionati,Squadre,Calendario

class CampionatiAdmin(admin.ModelAdmin):
    fields = ['nome']


class SquadreAdmin(admin.ModelAdmin):
    fields = ['nome']


class CalendarioAdmin(admin.ModelAdmin):
    fields = ['giornata','ar','data','locali','ospiti']



admin.site.register(Campionati,CampionatiAdmin)
admin.site.register(Squadre,SquadreAdmin)
admin.site.register(Calendario,CalendarioAdmin)
