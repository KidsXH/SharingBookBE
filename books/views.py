from books.models import Book, BookTagRel
from books.serializers import BookSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status

from categories.models import Category
from tags.models import Tag
from utils.functions import search_books


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def list(self, request, *args, **kwargs):
        params = request.query_params
        # Text from search input
        search_text = params.get('searchText')
        # selected categories
        category = params.get('category')
        # selected tags
        tags = params.getlist('tags[]')
        # sort params: key in ['book_name', 'trending', 'rating', 'book_credit'], order in ['ASC', 'DESC']
        sort_key = params.get('sortKey')
        sort_order = params.get('sortOrder')
        # union of all keywords
        keywords = []
        books = self.get_queryset()

        if search_text:
            keywords += [search_text]
            books = search_books(books, search_text)

        if category:
            keywords += [category]
            books = books.filter(category=Category.objects.get(category_name=category))

        if tags and len(tags) > 0:
            keywords += tags
            # Relations between books and tags
            rel = BookTagRel.objects.all()
            relations = rel.none()
            results = books.none()
            for tag_name in tags:
                tag = Tag.objects.all().get(tag_name=tag_name)
                relations = relations.union(rel.filter(tag=tag))
            for r in relations:
                results = results.union(books.filter(id=r.book.id))
            books = results

        # sort books
        if sort_key is not None:
            if sort_key in ['book_name', 'trending', 'rating', 'book_credit']:
                books = books.order_by(sort_key)
                if sort_order == 'DESC':
                    books = reversed(books)
            else:
                return Response({"detail": "Invalid sort key."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(books, many=True)
        data = {
            "bookList": serializer.data,
            "keywords": keywords,
        }
        return Response(data, status=status.HTTP_200_OK)






