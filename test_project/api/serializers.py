from rest_framework import serializers
from django.utils import timezone

from ads.models import Advertisement, User, AuthToken


class AdvertisementSerializer(serializers.ModelSerializer):
    """Сериализатор объявления"""
    class Meta:
        model = Advertisement
        fields = ('title', 'id', 'author', 'views', 'position',)

    def validate(self, attrs):
        request = self.context.get('request')
        if 'Authorization' not in request.headers:
            raise serializers.ValidationError({'error': 'Unauthorized'})

        auth_header = request.headers['Authorization']
        if not auth_header.startswith('Bearer '):
            raise serializers.ValidationError({'error': 'Invalid token'})

        token = auth_header.split('Bearer ')[1]
        if not self.validate_token(token):
            raise serializers.ValidationError({'error': 'Unauthorized'})

        return attrs

    def validate_token(self, token):
        try:
            auth_token = AuthToken.objects.get(key=token)
            if auth_token.expires_at and auth_token.expires_at < timezone.now():
                return False
            return True
        except AuthToken.DoesNotExist:
            return False


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор пользователя"""
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
