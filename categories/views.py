from rest_framework import viewsets
from categories.serializers import CategorySerializer
from categories.models import Category


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

