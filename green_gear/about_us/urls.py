from django.urls import path

from about_us import views

app_name = 'about_us'

urlpatterns = [
    path('', views.about_us, name='about_us'),
]
