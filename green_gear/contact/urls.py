from django.urls import path

from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.CommunicationServiceView.as_view(), name='contact'),

]
