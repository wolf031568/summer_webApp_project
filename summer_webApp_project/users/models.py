from django.db import models

# Create your models here.
class users(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30, unique=True)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=128)  # store hashed passwords ideally

    def __str__(self):
        return f"{self.first_name} {self.last_name}"