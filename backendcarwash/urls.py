"""backendcarwash URL Configuration

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
from backendapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/', views.CustomerList.as_view()),
    path('washer/', views.WasherList.as_view()),
    path('service/', views.ServiceList.as_view()),
    path('package/', views.PackageList.as_view()),
    path('order/', views.OrderList.as_view()),
    path('rating/', views.RatingList.as_view()),
    path('buku/', views.bukuList.as_view()),
    path('bantuan/', views.bantuanList.as_view()),
    path('nilai/', views.nilaiList.as_view()),
    path('berita/', views.beritaList.as_view()),
]
