"""scproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
import scapp.views
import user.views
import board.views
import freeboard.views
import review.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',scapp.views.index, name="home"),
    path('blog/',scapp.views.blog, name="blog"),
    path('contact/',scapp.views.contact, name="contact"),
    path('services/',scapp.views.services, name="services"),
    path('blog-single/',scapp.views.blogsingle, name="blogsingle"),
    path('user/', include('user.urls')),
    path('board/', include('board.urls')),
    path('freeboard/', include('freeboard.urls')),
    path('review/', include('review.urls')),
    path('blog2/',scapp.views.blog2, name="blog2"),
    path('blog3/',scapp.views.blog3, name="blog3"),
    path('blog4/',scapp.views.blog4, name="blog4"),
    path('blog5/',scapp.views.blog5, name="blog5"),
    path('blog6/',scapp.views.blog6, name="blog6"),
]