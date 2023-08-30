from django.contrib import admin
from .models import Post
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','created_at']
    list_filter = ("title",)
    search_fields = ['title', 'content']
    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)

