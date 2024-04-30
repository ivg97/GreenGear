from django.shortcuts import render

# Create your views here.
def list_page(request):
    return render(request, 'blog/list_page.html')