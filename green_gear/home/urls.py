from django.urls import path

from home import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # path('subscribe/<email:email>/', views.subscribe, name='subscribe'),
]
