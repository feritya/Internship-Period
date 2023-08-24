from django.shortcuts import render,get_object_or_404,redirect
from django.db.models.deletion import ProtectedError
from .models import Author, Book,AuthorNotes
from django.contrib.admin.utils import get_deleted_objects
from django.http import HttpResponseForbidden


"""
def delete_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    
    if request.method == 'POST':
        try:
            author.delete()
            return redirect('author_list')
        except ProtectedError as e:
            # protected_books = e.protected_objects.filter(book=book)
            # protected_books = [obj for obj in e.protected_objects if obj._meta.model_name == 'book']
            # protected_notes= [obj for obj in e.protected_objects if obj._meta.model_name == 'note']

            protected_books = [obj for obj in e.protected_objects if obj._meta.model_name == 'Book']
            protected_notes = [obj for obj in e.protected_objects if obj._meta.model_name == 'AuthorNotes']


            return render(request, 'protected_author.html', {'author': author, 'protected_books': protected_books, 'protected_notes': protected_notes})
        
    return render(request, 'delete_author.html', {'author': author})




def delete_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    
    if request.method == 'POST':
        #  deleted_objects, model_count, perms_needed, 
        protected = get_deleted_objects(
            [author], request.user, Author._meta
        )
        protected_books = []
        protected_notes = []

        for obj in protected:
            if obj._meta.model_name == 'book':
                protected_books.append(obj)
            elif obj._meta.model_name == 'note':
                protected_notes.append(obj)

        if protected_books or protected_notes:
            return render(request, 'protected_author.html', {'author': author, 'protected_books': protected_books, 'protected_notes': protected_notes})
        else:
            author.delete()
            return redirect('author_list')
        
    return render(request, 'delete_author.html', {'author': author})

"""
from django.db.models import ProtectedError
def delete_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    
    if request.method == 'POST':
        try:
            author.delete()
            return redirect('author_list')
        except ProtectedError:
            protected_books = Book.objects.filter(author=author)
            protected_notes = AuthorNotes.objects.filter(author=author)

            return render(request, 'protected_author.html', {'author': author, 'protected_books': protected_books, 'protected_notes': protected_notes})
        
    return render(request, 'delete_author.html', {'author': author})


def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    
    if request.method == 'POST':
        book.delete()
        return redirect('delete_author', author_id=book.author.id) 
        
    return render(request, 'delete_book.html', {'book': book})

def delete_note(request, note_id):
    note = get_object_or_404(AuthorNotes, pk=note_id)
    
    if request.method == 'POST':
        note.delete()
        return redirect('delete_author', author_id=note.author.id)
        
    return render(request, 'delete_note.html', {'note': note})


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_listt.html', {'authors': authors})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def note_list(request):
    notes = AuthorNotes.objects.all()
    return render(request, 'note_list.html', {'notes': notes})