from rest_framework import viewsets
from authors.serializers import AuthorSerializer
from authors.models import Author


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

