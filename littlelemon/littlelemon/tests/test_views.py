from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test instances of the Menu model
        Menu.objects.create(title="Ice Cream", price=3.99, inventory=100)
        Menu.objects.create(title="Pizza", price=9.99, inventory=50)
        Menu.objects.create(title="Burger", price=5.99, inventory=75)

    def test_get_all(self):
        client = APIClient()
        response = client.get(reverse('MenuItems'))
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
