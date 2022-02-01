from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('mfa_site.urls')),
    path('check_in_sender/', include('check_in_sender.urls')),
    path('admin/', admin.site.urls),
]
