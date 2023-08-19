from django.urls import path
from . import views

urlpatterns = [
    # Diğer url pattern'ları...
    path('delete_author/<int:author_id>/', views.delete_author, name='delete_author'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('author_list/', views.author_list, name='author_list'),
    path('book_list/', views.book_list, name='book_list'),
]
