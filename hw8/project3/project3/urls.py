"""project3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from app3 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_func, name="index_in_html"),
    path('new', views.new_func, name="new_in_html"),
    path('detail/<int:pk_of_article>', views.detail_func, name="detail_in_html"),
    path('movie',views.movie_func, name="movie_in_html"),
    path('drama', views.drama_func, name="drama_in_html"),
    path('entertain', views.entertain_func, name="entertain_in_html"),
]