from django.utils import timezone
from rest_framework.permissions import BasePermission
from ads.models import AuthToken


class BearerTokenPermission(BasePermission):
    def has_permission(self, request, view):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return False

        token = auth_header.split('Bearer ')[1]
        try:
            auth_token = AuthToken.objects.get(key=token)
            if auth_token.expires_at and auth_token.expires_at < timezone.now():
                return False
            return True
        except AuthToken.DoesNotExist:
            return False
