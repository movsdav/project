from django.db import models
from django.contrib.auth.models import User

from patientsApp.models import Patient


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    patients = models.ManyToManyField(Patient, blank=True)
