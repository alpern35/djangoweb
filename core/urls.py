"""
URL configuration for site79084 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_post, name='add_post'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile_detail, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),
    # (optional) path('<int:pk>/edit/', views.post_update, name='post_update'),
]

    

