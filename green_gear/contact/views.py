from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, FormView
from django.core.mail import send_mail

from contact.forms import CommunicationServiceForm


def contact(request):
    template_name = 'contact/contact.html'
    form = CommunicationServiceForm()
    if request.method == "POST":
        form = CommunicationServiceForm(request.POST)

    return render(request, template_name)


class CommunicationServiceView(FormView):
    template_name = 'contact/contact.html'
    form_class = CommunicationServiceForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_form'] = context['form']
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        self.object = super().get_form(form_class)
        return self.object

    def get_success_url(self):
        return reverse('home:home')
