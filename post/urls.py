"""
URL configuration for post project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

#앱이 추가될 때 기본 path경로와 각 앱 폴더 안쪽의 url.py를 아래와 같이 등록
urlpatterns = [
  path('posts', views.posts, name='posts'),
  path('posts/<slug:slug>/', views.posts_detail, name='post-detail')
]
