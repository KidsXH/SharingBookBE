from rest_framework import serializers
from authors.models import Author


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.HyperlinkedRelatedField(many=True, view_name='book-detail', read_only=True)

    class Meta:
        model = Author
        fields = ('url', 'id', 'author_name', 'introduction', 'books', )
