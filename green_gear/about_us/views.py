from django.shortcuts import render

from about_us.models import Team, Feedback


def about_us(request):
    members = Team.objects.filter(is_active=True)
    # members = [i for i in range(17)]

    context = {
        'title': 'Green gear - About us',
        'members': members,
    }
    template_name = 'about_us/about_us.html'
    return render(request, template_name, context)

