"""
URL configuration for green_gear project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import home
from about_us.views import about_us
from service.views import service
from blog.views import list_page
from blog.views import detail_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about_us/', about_us, name='about_us'),
    path('home/', home, name='home'),
    path('service/', service, name='service'),
    path('blog/', list_page, name='list_page'),
    path('blog_post/', detail_page, name='detail_page'),
    path('', home, name='home'),
]