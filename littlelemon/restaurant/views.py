from django.shortcuts import render
from .models import Menu
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .serializers import MenuSerializer
# Create your views here.

def index(request):
    return render(request, "index.html", {})


class MenuItemsView(ListCreateAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer



class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer
