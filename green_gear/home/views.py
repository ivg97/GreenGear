from django.shortcuts import render

# Create your views here.
def home(request):
    title = {
        'title': 'Green gear'
    }
    return render(request, 'home/home.html', title)