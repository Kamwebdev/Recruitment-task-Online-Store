from django.contrib.auth.models import Group, Permission, User
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse_lazy


class CheckPersmissionsOrderTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.group = Group(name="Client")
        self.group.save()
        self.c = Client()

    def test_anonymoususer_cannot_acces(self):
        response = self.c.get(reverse_lazy('order'))
        self.assertTrue(response.has_header("Location"))

    def test_user_cannot_acces(self):
        self.c.login(username='testuser', password='12345')
        response = self.c.get(reverse_lazy('order'))
        self.assertTrue(response.has_header("Location"))

    def test_user_can_acces(self):
        self.user.groups.add(self.group)
        self.user.save()
        self.c.login(username='testuser', password='12345')
        response = self.c.get(reverse_lazy('order'))
        self.assertFalse(response.has_header("Location"))


class CheckPersmissionsManageProductsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.group = Group(name="Seller")
        self.group.save()
        self.c = Client()

    def test_anonymoususer_cannot_acces(self):
        response = self.c.get(reverse_lazy('product-list-manage'))
        self.assertTrue(response.has_header("Location"))

    def test_user_cannot_acces(self):
        self.c.login(username='testuser', password='12345')
        response = self.c.get(reverse_lazy('product-list-manage'))
        self.assertTrue(response.has_header("Location"))

    def test_user_can_acces(self):
        self.user.groups.add(self.group)
        self.user.save()
        self.c.login(username='testuser', password='12345')
        response = self.c.get(reverse_lazy('product-list-manage'))
        self.assertFalse(response.has_header("Location"))