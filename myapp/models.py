from django.db import models


# Create your models here.

class Authors(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birthdate = models.DateField(null=True)
    bio = models.TextField(null=True)

    def __str__(self):
        return self.name + " " + self.email


class Tag(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()

    def __str__(self):
        return self.name



class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_add = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Authors, on_delete=models.PROTECT, null=True)
    tags = models.ManyToManyField(Tag, related_name='articles', null=True)
