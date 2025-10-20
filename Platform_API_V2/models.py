from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

def __str__(self):
    return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    commenter = models.TextField(max_length=20)

    def __str__(self):
        return self.commenter


