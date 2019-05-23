from books.models import Book
from books.serializers import BookSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def list(self, request, *args, **kwargs):
        order_by = request.query_params.get('order_by')
        # selected = request.query_params.get('selected')
        books = self.get_queryset()

        if order_by is not None:
            if order_by in ['book_name']:
                books = books.order_by(order_by)
            else:
                return Response({"detail": "Invalid sort key."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(books, many=True)
        data = {
            "bookList": serializer.data,
            "selectedTags": ['T1', 'T2', 'T3', 'XXX'],
        }
        return Response(data, status=status.HTTP_200_OK)
