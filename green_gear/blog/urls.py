from django.contrib import admin
from django.urls import path

from blog.views import list_page, detail_page

urlpatterns = [
    path('', list_page, name='list_page'),
    path('blog_post/', detail_page, name='detail_page'),
]
