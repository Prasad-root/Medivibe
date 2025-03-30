from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255,null=True)
    home_address = models.CharField(max_length=500,null=True)
    contact_number = models.CharField(max_length=10,null=True)
    location = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.user.username
