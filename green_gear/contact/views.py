from django.shortcuts import render


def contact(request):
    template_name = 'contact/contact.html'
    return render(request, template_name)

