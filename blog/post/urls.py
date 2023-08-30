from  . import views
from django.urls import path

urlpatterns = [

    path('create/', views.post_create, name='create'),
    path('index/', views.post_index, name='index'),
    path('update/', views.post_update, name='update'),
    path('detail/<int:post_id>/', views.post_detail, name='detail'),
    
    path('delete/', views.post_delete, name='delete'),
    # path('list/', views.post_list, name='list'),
]




