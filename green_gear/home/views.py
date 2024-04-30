from django.shortcuts import render


def home(request):
    """Main page"""
    context = {
        'title': 'Green gear',
    }
    template_name = 'home/home.html'
    return render(request, template_name, context)
