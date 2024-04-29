from django.shortcuts import render


def home(request):
    """Main page"""
    template_name = 'home/home.html'
    return render(request, template_name)
