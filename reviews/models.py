from django.db import models
from django.db import connections

# Create your models here.
class Review(models.Model):
    
    title = models.TextField()
    content = models.TextField()
    