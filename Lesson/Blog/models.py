from django.db import models


class Post(models.Model): 
    title = models.CharField(max_length=25)
    likes = models.IntegerField()
    body = models.TextField()
    