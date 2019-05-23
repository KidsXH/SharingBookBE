from django.db import models
from authors.models import Author
from categories.models import Category
from tags.models import Tag


class Book(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    book_name = models.CharField(blank=False, max_length=100)
    book_credit = models.PositiveIntegerField(default=0)
    introduction = models.TextField()
    trending = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    quantity = models.PositiveIntegerField(default=0)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True)
    rating_amount = models.PositiveIntegerField(default=0)

    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='books', through='BookTagRel')
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)


class BookTagRel(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

