from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='custom_user')
    created_at = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    major = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"