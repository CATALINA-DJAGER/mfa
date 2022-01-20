from django.contrib import admin

from .models import Aircompany


class AircompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')


admin.site.register(Aircompany, AircompanyAdmin)
