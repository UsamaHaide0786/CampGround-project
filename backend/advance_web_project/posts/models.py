from django.db import models


# Create your models here.
class Post(models.Model):
    name = models.TextField(null=False)
    url = models.TextField()
    description = models.TextField()
