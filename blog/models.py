from django.db import models


class Post1(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author=models.CharField(max_length=200)
    date=models.DateField()
    thumbnail=models.CharField(max_length=200)
    

    def __str__(self):
        return self.title
