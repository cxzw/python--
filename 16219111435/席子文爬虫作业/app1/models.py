from django.db import models

# Create your models here.
class app1(models.Model):
    title=models.CharField(max_length=250)