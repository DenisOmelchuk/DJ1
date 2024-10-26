from django.http import JsonResponse
from django.shortcuts import render
from bookstore.models import Book


def list_books(request):
    books = Book.objects.all()
    books_data = list()
    for book in books:
        book_data = {
            'name': book.name,
            'year': book.year,
            'author': book.author.name,
            'author_age': book.author.age,
            'publisher': book.publisher.name,
        }
        books_data.append(book_data)

    return JsonResponse({
        'books': books_data
    })
