from django.contrib import admin

from blog.models import Post, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    list_display_links = ('title',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'is_active')
    list_display_links = ('title',)
