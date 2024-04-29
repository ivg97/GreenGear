from django.shortcuts import render


def service(request):
    template_name = 'service/service.html'
    return render(request, template_name)
