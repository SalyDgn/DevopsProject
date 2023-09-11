from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import User, Visit
from .serializers import UserSerializer, VisitSerializer


class UserListViewTestCase(APITestCase):

    def setUp(self):
        User.objects.create(username="user1", email="user1@example.com",
                            first_name='user1fn', last_name="user1ln")
        User.objects.create(username="user2", email="user2@example.com",
                            first_name='user1fn', last_name="user1ln")

    def test_get_user_list(self):

        url = reverse('users')

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        users = User.objects.all()
        expected_data = UserSerializer(users, many=True).data

        self.assertEqual(response.data, expected_data)


class VisitTests(APITestCase):

    def test_get_visits_count(self):

        response = self.client.get(reverse('visit-count'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        visits = Visit.objects.all()
        expected_data = UserSerializer(visits, many=True).data

        self.assertEqual(response.data, expected_data)

    def test_first_visit(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

        visit = Visit.objects.first()
        self.assertEqual(visit.count, 1)

    def test_increment_visit_count(self):
        visit = Visit.objects.create(count=5)

        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

        visit.refresh_from_db()
        self.assertEqual(visit.count, 6)

    def test_db_number_of_rows(self):
        visit = Visit.objects.create(count=5)

        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

        visit.refresh_from_db()
        visits = Visit.objects.all()
        self.assertEqual(len(visits), 1)
