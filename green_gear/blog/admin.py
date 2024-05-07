from django.contrib import admin

from blog.models import Post, Category, NewPostEmail


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'is_active')
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(NewPostEmail)
class NewPostEmailAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active')
    list_display_links = ('email',)
