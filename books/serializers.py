from rest_framework import serializers
from authors.models import Author
from books.models import Book
from categories.models import Category
from tags.models import Tag


class BookSerializer(serializers.HyperlinkedModelSerializer):
    # author = serializers.CharField(source='author.author_name')
    # category = serializers.CharField(source='category.category_name')
    author = serializers.HyperlinkedRelatedField(view_name='author-detail', queryset=Author.objects.all())
    category = serializers.HyperlinkedRelatedField(view_name='category-detail', queryset=Category.objects.all())
    tags = serializers.HyperlinkedRelatedField(many=True, view_name='tag-detail', queryset=Tag.objects.all())

    class Meta:
        model = Book
        fields = ('url', 'id', 'book_name', 'author', 'introduction', 'category', 'tags',
                  'book_credit', 'trending', 'quantity', 'rating', 'rating_amount')
