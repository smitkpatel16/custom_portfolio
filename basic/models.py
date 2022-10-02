from django.db import models

# Create your models here.


class Image(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    hashtags = models.TextField()
    category = models.CharField(max_length=50)
    associates = models.TextField()
