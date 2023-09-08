from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User
from .serializers import UserSerializer


class UserListViewTestCase(APITestCase):

    def setUp(self):
        # Create some example users for testing
        User.objects.create(username="user1", email="user1@example.com",
                            first_name='user1fn', last_name="user1ln")
        User.objects.create(username="user2", email="user2@example.com",
                            first_name='user1fn', last_name="user1ln")

    def test_get_user_list(self):
        # Define the URL for your view
        # Assuming you've set the name in your app's urls.py
        url = reverse('users')

        # Make an HTTP GET request to the URL
        response = self.client.get(url)

        # Check if the response status code is HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Get the expected serialized data
        users = User.objects.all()
        expected_data = UserSerializer(users, many=True).data

        # Check if the response data matches the expected data
        self.assertEqual(response.data, expected_data)
