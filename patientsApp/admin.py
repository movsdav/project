from django.contrib import admin

from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = list(field.name for field in Patient._meta.get_fields() if field.name != 'doctor')