"""
Source: https://medium.com/django-rest/django-rest-framework-login-and-register-user-fd91cf6029d5
Reduced to minimal required functionalities
"""

from django.contrib.auth.models import User
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from backend.auth.serializers import RegisterSerializer


class RegisterView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
