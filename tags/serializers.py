from rest_framework import serializers
from tags.models import Tag


class TagSerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.HyperlinkedRelatedField(many=True, view_name='book-detail', read_only=True)

    class Meta:
        model = Tag
        fields = ('url', 'id', 'tag_name', 'books', )
