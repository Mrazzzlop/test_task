from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from ads.models import Advertisement, User


class AdvertisementSerializer(serializers.ModelSerializer):
    """Сериализатор объявления"""
    class Meta:
        model = Advertisement
        fields = ('title', 'id', 'author', 'views', 'position',)


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор пользователя"""
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
