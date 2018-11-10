from copy import copy
import json
from operator import attrgetter, itemgetter


class Book:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return self.title

    def __repr__(self):
        return str(self)


def get_books(filename, raw=False):
    try:
        data = json.load(open(filename))
    except FileNotFoundError:
        return []
    else:
        if raw:
            return data['books']
        return [Book(**book) for book in data['books']]


BOOKS = get_books('books.json')
RAW_BOOKS = get_books('books.json', raw=True)

# pub_sort = sorted(RAW_BOOKS, key=itemgetter('publish_date'))
# print(pub_sort[0]['publish_date'], pub_sort[-1]['publish_date'])


# pages_sort = sorted(BOOKS, key=attrgetter('number_of_pages'))
# print(pages_sort[0].number_of_pages,
#      pages_sort[-1].number_of_pages)


# a = [1, 2, 3, 4]
# def double(n):
#    return n * 2
# print(list(map(double, a)))


def sales_price(book):
    """Apply a 20% discount to the book's price"""
    book = copy(book)
    book.price = round(book.price - book.price*.2, 2)
    return book


# sales_books = list(map(sales_price, BOOKS))

""" Implementation of the map() function as a list comprehension. Only use list comprehensions for tasks that don't need a lot of lines of code; for more complex functions, use map()"""
sales_books2 = [sales_price(book) for book in BOOKS]
print(BOOKS[0].price)
print(sales_books2[0].price)
