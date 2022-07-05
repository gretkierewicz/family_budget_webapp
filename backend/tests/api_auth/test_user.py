from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


def create_valid_register_data(suffix: int = 1) -> dict[str, str]:
    return {
        "username": f"user{suffix}",
        "password": "user1234",
        "password2": "user1234",
        "email": f"user{suffix}@mail.com",
    }


class AccountTests(APITestCase):
    def test_create_user_with_register_endpoint(self):
        """
        Ensure we can create a new user object.
        """
        user_data = create_valid_register_data()
        url = reverse("register-list")
        response = self.client.post(url, user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(
            User.objects.get().username, user_data.get("username"),
        )

    def test_user_list_endpoint(self):
        user_data = create_valid_register_data()
        user = User.objects.create_user(user_data)
        self.client.force_login(user)
        url = reverse("user-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertEqual(len(response.data), 1, response.data)
