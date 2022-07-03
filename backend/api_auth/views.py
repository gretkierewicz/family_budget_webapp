"""
Source: https://medium.com/django-rest/django-rest-framework-login-and-register-user-fd91cf6029d5
Reduced to minimal required functionalities
"""

from django.contrib.auth.models import User
from rest_framework import mixins, permissions, viewsets
from rest_framework.permissions import AllowAny

from backend.api_auth.serializers import RegisterSerializer, UserSerializer


class RegisterView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserView(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer
