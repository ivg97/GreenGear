from django.shortcuts import render

# Create your views here.
def about_us(request):
    title = {
        'title': 'About us'
    }
    return render(request, 'about_us/about_us.html', title)