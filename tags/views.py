from rest_framework import viewsets
from tags.serializers import TagSerializer
from tags.models import Tag


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

