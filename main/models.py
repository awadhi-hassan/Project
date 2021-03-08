from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Fingerprint(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
       return self.first_name

class Reservation(models.Model):
    computer_number = models.IntegerField()
    duration_time = models.CharField(max_length=30)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name