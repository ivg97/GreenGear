from django.shortcuts import render

# Create your views here.
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