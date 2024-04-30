from django.shortcuts import render

# Create your views here.
def contact(request):
    title = {
        'title': 'contact'
    }
    return render(request, 'contact/contact.html', title)