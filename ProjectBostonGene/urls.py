from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='home'),
    path('patients/', include('patientsApp.urls')),
    path('admin/', admin.site.urls),
    path('auth/',include('authApp.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
