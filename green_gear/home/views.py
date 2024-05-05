from django.shortcuts import render
from django.urls import reverse
from django.views.generic import FormView

from about_us.models import Feedback
from home.forms import NewPostEmailForm


def home(request):
    """Main page"""
    feedbacks = Feedback.objects.filter(is_active=True).order_by('assessment')
    # feedbacks = [i for i in range(5)]

    context = {
        'title': 'Green gear',
        'feedbacks': feedbacks,
    }
    template_name = 'home/home.html'
    return render(request, template_name, context)


class HomeView(FormView):
    template_name = 'home/home.html'
    form_class = NewPostEmailForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Green Gear'
        context['feedbacks'] = Feedback.objects.filter(
            is_active=True).order_by('assessment')
        context['email_form'] = context['form']
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        self.object = super().get_form(form_class)
        return self.object

    def get_success_url(self):
        return reverse('home:home')


def subscribe(request, email):
    return reverse('home:home')
