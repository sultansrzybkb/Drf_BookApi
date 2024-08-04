from django.shortcuts import render
from django.http import JsonResponse

from book_api.models import Book
def book_list(request):
    books=Book.objects.all()
    books_list = list(books.values())
    return JsonResponse({
        "books": books_list
    })
def create(request):
    pass

#serilize