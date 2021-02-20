from django.db import models

# Create your models here.
class plantPromModel(models.Model):
    Sentence = models.CharField(max_length=1000)
    
