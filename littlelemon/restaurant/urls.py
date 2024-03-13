from django.urls import path
from django.contrib import admin
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view(), name="MenuItems"),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name="SingleMenuItem"),
]