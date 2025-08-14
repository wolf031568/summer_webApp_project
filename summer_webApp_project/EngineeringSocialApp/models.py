from django.db import models

# Create your models here.
class users(models.Model):
    create_at = models.DateTimeField(auto_now_add= True) #create new user 
    first_name = models.CharField(max_length= 20)
    last_name = models.CharField(max_length=20)
    #email = models.EmailField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    major = models.CharField(max_length=30)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")