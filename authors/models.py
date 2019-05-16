from django.db import models

# Create your models here.


class Author(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    author_name = models.CharField(max_length=100)
    introduction = models.TextField()

    class Meta:
        ordering = ['created', ]
