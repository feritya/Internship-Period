from django.shortcuts import render,get_object_or_404,redirect
from django.db.models.deletion import ProtectedError
from .models import Author, Book


def delete_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    
    if request.method == 'POST':
        try:
            author.delete()
            return redirect('author_list')
        except ProtectedError as e:
            # protected_books = e.protected_objects.filter(book=book)
            protected_books = [obj for obj in e.protected_objects if obj._meta.model_name == 'book']
            protected_notes= [obj for obj in e.protected_objects if obj._meta.model_name == 'note']

            return render(request, 'protected_author.html', {'author': author, 'protected_books': protected_books, 'protected_notes': protected_notes})
        
    return render(request, 'delete_author.html', {'author': author})


def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  
        
    return render(request, 'delete_book.html', {'book': book})


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})