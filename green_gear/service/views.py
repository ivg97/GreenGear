from django.shortcuts import render


def service(request):
    context = {
        'title': 'Services'
    }
    template_name = 'service/service.html'
    return render(request, template_name, context)
