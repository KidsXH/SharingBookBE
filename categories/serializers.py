from rest_framework import serializers
from categories.models import Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.HyperlinkedRelatedField(many=True, view_name='book-detail', read_only=True)

    class Meta:
        model = Category
        fields = ('url', 'id', 'category_name', 'books')
