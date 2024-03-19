from django.contrib import admin
from django.urls import path
from myFirstProject import views

urlpatterns = [
    path('', views.index),
    path('second/', views.Second_page),
    path('page1/', views.page1),
    path('page2/', views.page2),
    path('page3/', views.page3),
    path('page4/', views.page4)
]
