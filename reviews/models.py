from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.TextField()
    content = models.TextField()
    