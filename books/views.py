import json

from books.models import Book, BookTagRel
from books.serializers import BookSerializer
from rest_framework import viewsets, permissions, generics

from categories.models import Category
from tags.models import Tag
from utils.functions import search_books
from utils.responses import ResponseMsg


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
                return ResponseMsg.bad_request("Invalid sort key.")

        if request.user.is_authenticated:
            for book in books:
                if request.user.userprofile.favorite_books.exists(pk=book.pk):
                    book.is_favorite = True
                    book.save()

        serializer = self.get_serializer(books, many=True)
        data = {
            "bookList": serializer.data,
            "keywords": keywords,
        }
        return ResponseMsg.ok(data=data)


class BookRecommendView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        categories = self.get_queryset()
        cates = []
        fav_cates = json.loads(request.user.userprofile.favorite_categories).get('data')
        read_books = json.loads(request.user.userprofile.books_read).get('data')

        for i in range(-5, 0):
            new_cates = [1, read_books[i]]
            if i != -5:
                for j in range(-5, i):
                    if read_books[i] == cates[j + 5][1]:
                        cates[j + 5][0] += 1
                        break
                    if j == i - 1:
                        cates.append(new_cates)
            else:
                cates.append(new_cates)

        for i in fav_cates:
            for j in cates:
                if i == j[1]:
                    j[0] += 2
                    break

        cates.sort()

        book1 = categories.get(category_name=cates[-1][1]).books.order_by('rating')[0]
        book2 = categories.get(category_name=cates[-2][1]).books.order_by('rating')[0]
        result = {"result": [{"book1_id": book1.id, "book1_name": book1.book_name},
                             {"book1_id": book2.id, "book1_name": book2.book_name}]}

        return ResponseMsg.ok(data=result)
