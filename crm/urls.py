from django.contrib import admin
from django.urls import include, path

from crm import views

urlpatterns = [
    path('', views.first_page),
    path('thanks', views.thanks_page, name='thanks_page'),
]

