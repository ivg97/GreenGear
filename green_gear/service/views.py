from django.shortcuts import render

# Create your views here.
def service(request):
    title = {
        'title': 'services'
    }
    return render(request, 'service/service.html', title)