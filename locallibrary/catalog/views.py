from django.shortcuts import render
from catalog.models import Book, Genre, BookInstance, Author


def index(request):
    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()

    num_instance_availb = BookInstance.objects.filter(status='a').count()
    num_author = Author.objects.all().count()

    return render(request,
                  'index.html',
                  context={'num_books': num_books, 'num instance': num_instance,
                           'num_instance_availb': num_instance_availb, 'num_author': num_author})
