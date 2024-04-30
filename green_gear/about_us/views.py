from django.shortcuts import render


def about_us(request):
    template_name = 'about_us/about_us.html'
    return render(request, template_name)
