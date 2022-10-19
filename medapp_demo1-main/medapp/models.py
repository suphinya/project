import email
from email.policy import default
from enum import unique
from pyexpat import model
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Elder(models.Model):
    first_name = models.CharField(max_length=30)
    sure_name = models.CharField(max_length=30)
    birthday = models.DateField()
    hospital_number = models.CharField(max_length=30)
    hospital_name = models.CharField(max_length=50)
    hospital_phone = models.CharField(max_length=10)
    relative_firstname = models.CharField(max_length=30)
    relative_surename = models.CharField(max_length=30)
    relative_relation = models.CharField(max_length=30)
    relative_phone = models.CharField(max_length=10)
    disease = models.JSONField()
    physical = models.JSONField()
    memory = models.CharField(max_length=30)

    image = models.ImageField(upload_to='images/', blank=True)
    # face = models.JSONField()
