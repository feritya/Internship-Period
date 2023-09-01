# from django.shortcuts import render, redirect
# from django.views import View
# from django.db.models import ProtectedError
# from .models import Author, Article, Book

# class AuthorListView(View):
#     template_name = 'author_list.html'
    
#     def get(self, request):
#         authors = Author.objects.all()
#         return render(request, self.template_name, {'authors': authors})
    
#     def post(self, request):
#         authors = Author.objects.all()
#         protected_books = []
#         protected_articles = []

#         for author in authors:
#             try:
#                 author.delete()
#             except ProtectedError:
#                 protected_books.extend(Book.objects.filter(author=author))
#                 protected_articles.extend(Article.objects.filter(author=author))

#         return render(request, self.template_name, {'authors': authors, 'protected_books': protected_books, 'protected_articles': protected_articles})

# def delete_author(request, author_id):
#     author = Author.objects.get(pk=author_id)
    
#     # Korunan kitapları ve makaleleri bul
#     protected_books = Book.objects.filter(author=author)
#     protected_articles = Article.objects.filter(author=author)
    
#     # Korunan kitapları ve makaleleri sil
#     protected_books.delete()
#     protected_articles.delete()
    
#     # Yazarı sil
#     author.delete()
    
#     return redirect('author_list')


from django.shortcuts import render, redirect
from django.views import View
from django.db.models import ProtectedError
from .models import ModelA, ModelB, ModelC

class ModelAListView(View):
    template_name = 'model_a_list.html'
    
    def get(self, request):
        model_a_objects = ModelA.objects.all()
        return render(request, self.template_name, {'model_a_objects': model_a_objects})

    def post(self, request):
        if 'delete' in request.POST:
            model_a_id = int(request.POST.get('delete'))
            model_a = ModelA.objects.get(pk=model_a_id)
            
            # Korunan B ve C nesnelerini bul
            protected_b_objects = ModelB.objects.filter(model_a=model_a)
            protected_c_objects = ModelC.objects.filter(model_a=model_a)
            
            if protected_b_objects or protected_c_objects:
                return render(request, 'model_a_list.html', {'model_a_objects': ModelA.objects.all(), 'protected_b_objects': protected_b_objects, 'protected_c_objects': protected_c_objects, 'selected_model_a': model_a})
            else:
                # Silebilir, herhangi bir bağlı nesne yok
                model_a.delete()
                return redirect('model_a_list')

