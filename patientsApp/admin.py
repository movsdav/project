from django.contrib import admin

from .models import Patient

# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = list(field.name for field in Patient._meta.get_fields())