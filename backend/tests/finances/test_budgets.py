from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from backend.finances.models import Budget


def create_user(name="user1"):
    return User.objects.create_user(name, email=f"{name}@mail.com", password="Secret#1")


class BudgetListEndpointTests(APITestCase):
    def test_initially_empty(self):
        user = create_user()

        self.client.force_login(user)

        url = reverse("budget-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertEqual(len(response.data), 0, response.data)

    def test_after_inserting_object(self):
        user = create_user()
        Budget.objects.create(name="budget1", owner=user)

        self.client.force_login(user)

        url = reverse("budget-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertEqual(len(response.data), 1, response.data)
        self.assertEqual(response.data[0].get("name"), "budget1")

    def test_empty_for_other_users(self):
        user = create_user()
        Budget.objects.create(name="budget1", owner=user)
        user2 = create_user("user2")

        self.client.force_login(user2)

        url = reverse("budget-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertEqual(len(response.data), 0, response.data)


class BudgetDetailEndpointTests(APITestCase):
    def test_initially_empty(self):
        user = create_user()

        self.client.force_login(user)

        url = reverse("budget-detail", kwargs={"pk": 1})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND, response.data)

    def test_after_inserting_object(self):
        user = create_user()
        Budget.objects.create(name="budget1", owner=user)

        self.client.force_login(user)

        url = reverse("budget-detail", kwargs={"pk": 1})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertEqual(response.data.get("name"), "budget1")

    def test_not_visible_to_other_users(self):
        user = create_user()
        Budget.objects.create(name="budget1", owner=user)
        user2 = create_user("user2")

        self.client.force_login(user2)

        url = reverse("budget-detail", kwargs={"pk": 1})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND, response.data)

