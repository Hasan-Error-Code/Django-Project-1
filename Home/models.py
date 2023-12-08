from django.db import models

# Create your models here.
class teacher(models.Model):
    T_name = models.IntegerField()
    T_Age = models.CharField(max_length=50)
    T_Class = models.CharField(max_length=50)


    