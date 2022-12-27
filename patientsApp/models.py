from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

import uuid


class Patient(models.Model):
    uuid = models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    diagnosis = models.TextField()
    age = models.IntegerField(validators=(
        MinValueValidator(0),
        MaxValueValidator(110),
    ))
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.age}'
