from django.db import models


class Category(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    category_name = models.CharField(max_length=20)

    class Meta:
        ordering = ['created', ]
