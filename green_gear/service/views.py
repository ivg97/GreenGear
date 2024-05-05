from django.shortcuts import render
from django.views.generic import TemplateView

from service.models import Service

def service(request):
    context = {
        'title': 'Green gear - Services'
    }
    template_name = 'service/service.html'
    return render(request, template_name, context)


class ServiceView(TemplateView):
    template_name = 'service/service.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Services'
        context['services'] = Service.objects.filter(is_active=True)
        return context
