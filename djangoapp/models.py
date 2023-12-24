from django.db import models

# Create your models here.
class Comment(models.Model):
    author = models.CharField(max_length=500)
    text = models.TextField(max_length=5000)
    date = models.DateTimeField(max_length=500)
    likes = models.IntegerField()
    image = models.TextField(max_length=500)

