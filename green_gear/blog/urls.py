from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogView.as_view(), name='list_page'),
    path('post/<slug:slug>/<int:pk>/', views.DetailPostView.as_view(), name='post'),
]
