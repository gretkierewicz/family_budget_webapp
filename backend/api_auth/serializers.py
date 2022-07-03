"""
Source: https://medium.com/django-rest/django-rest-framework-login-and-register-user-fd91cf6029d5
Reduced to minimal required functionalities
"""

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from backend.finances.models import Budget


class UserSerializer(serializers.HyperlinkedModelSerializer):
    budgets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Budget.objects.all()
    )

    class Meta:
        model = User
        fields = ["url", "username", "budgets"]


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("username", "password", "password2", "email")

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"], email=validated_data["email"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user
