from django.db import models
from django.contrib.auth.models import User

class Reservation(models.Model):
    computer_number = models.IntegerField()
    duration_time = models.CharField(max_length=30)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name

class Files(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files')

    def __str__(self):
        return f'{self.user.first_name} Files'