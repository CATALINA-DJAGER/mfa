from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('check_in_sender/', include('check_in_sender.urls')),
    path('admin/', admin.site.urls),
]