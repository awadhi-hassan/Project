from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Fingerprint)

admin.site.register(models.Reservation)
