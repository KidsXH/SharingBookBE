from rest_framework import serializers

from authors.models import Author
from books.models import Book
from categories.models import Category
from tags.models import Tag
from tags.serializers import TagSerializer
from authors.serializers import AuthorSerializer
from categories.serializers import CategorySerializer


class BookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='author_name', queryset=Author.objects.all())
    category = serializers.SlugRelatedField(slug_field='category_name', queryset=Category.objects.all())
    tags = serializers.SlugRelatedField(many=True, slug_field='tag_name', queryset=Tag.objects.all())

    class Meta:
        model = Book
        fields = ('id', 'book_name', 'author', 'introduction', 'category', 'tags',
                  'book_credit', 'trending', 'quantity', 'rating', 'rating_amount')
