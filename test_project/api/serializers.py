from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from ads.models import Advertisement, User


class AdvertisementSerializer(serializers.ModelSerializer):
    """Сериализатор объявления"""
    class Meta:
        model = Advertisement
        fields = ('title', 'id', 'author', 'views', 'position',)

    def validate(self, attrs):
        request = self.context['request']
        if 'Authorization' not in request.headers:
            raise AuthenticationFailed('Unauthorized')

        auth_header = request.headers['Authorization']
        if not auth_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid token')

        token = auth_header.split('Bearer ')[1]
        if not self.validate_token(token):
            raise AuthenticationFailed('Unauthorized')

        return attrs

    def validate_token(self, token):
        # Your custom token validation logic here
        # For example, you can check if the token is expired
        if token.is_expired():
            return False
        return True


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор пользователя"""
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
