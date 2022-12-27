from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('patients/'),
    path('admin/', admin.site.urls),
]
