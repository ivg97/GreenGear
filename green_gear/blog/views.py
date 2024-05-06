from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from blog.models import Category, Post


def list_page(request):
    title = {
        'title': 'blog'
    }
    return render(request, 'blog/list_page.html', title)


def detail_page(request):
    title = {
        'title': 'blog post'
    }
    return render(request, 'blog/detail_page.html', title)


class BlogView(TemplateView):
    template_name = 'blog/list_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Green gear - Blog'
        context['categories'] = Category.objects.all()
        posts = Post.objects.filter(is_active=True)
        top = posts[0] if len(posts) > 0 else None
        context['posts'] = posts
        context['top_post'] = top
        return context


class DetailPostView(DetailView):
    model = Post

    def get_template_names(self):
        return f'blog/detail_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Green gear - {self.object.title}'
        return context
