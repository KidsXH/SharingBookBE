from numpy import unique


def intersection(list_a, list_b):
    """
    calculate intersection of two list
    :param list_a: list
    :param list_b: list
    :return: list
    """
    new_list = []
    list_a = unique(sorted(list_a))
    list_b = unique(sorted(list_b))
    n, m, i, j = len(list_a), len(list_b), 0, 0
    while i < n and j < m:
        if list_a[i] == list_b[j]:
            new_list.append(list_a[i])
            i += 1
            j += 1
        elif list_a[i] < list_b[j]:
            i += 1
        else:
            j += 1
    return new_list


def search_books(books, search_text):
    """
    get searched books by search text
    :param books: queryset
    :param search_text: string
    :return: queryset
    """
    result = books.none()
    if search_text:
        keywords = search_text.split()
        for keyword in keywords:
            result = result.union(books.filter(book_name=keyword))
            result = result.union(books.filter(author__author_name=keyword))
            result = result.union(books.filter(category__category_name=keyword))
    return result
