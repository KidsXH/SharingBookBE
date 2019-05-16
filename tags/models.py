from django.db import models


class Tag(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    tag_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['created', ]
