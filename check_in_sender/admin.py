from django.contrib import admin

from .models import Aircompany, Traveller, CheckIn, Email, EmailTraveller


class AircompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')


class TravellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


class CheckInAdmin(admin.ModelAdmin):
    list_display = ('aircompany', 'traveller', 'date_time', 'status')


class EmailAdmin(admin.ModelAdmin):
    list_display = ('template_path', 'content')


class EmailTravellerAdmin(admin.ModelAdmin):
    list_display = ('email', 'traveller')


admin.site.register(Aircompany, AircompanyAdmin)
admin.site.register(Traveller, TravellerAdmin)
admin.site.register(CheckIn, CheckInAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(EmailTraveller, EmailTravellerAdmin)

