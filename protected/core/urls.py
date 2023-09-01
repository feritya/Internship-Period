from django.urls import path,include

urlpatterns = [
    path('author_list/', views.AuthorListView.as_view(), name='author_list'),

]   