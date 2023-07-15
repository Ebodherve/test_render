from django.db import models

# Create your models here.

class AnythingModel(models.Model):
    att1 = models.CharField(max_length=255)
    att2 = models.CharField(max_length=255)

