from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken

from ads.models import Advertisement, User, AuthToken
from .serializers import AdvertisementSerializer, UserSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            token = str(AccessToken.for_user(serializer.instance))  # Convert to string
            return Response({'token': token})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.filter(email=email).first()
        if user and user.password == password:
            token, _ = AuthToken.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({
            'error': 'Invalid credentials'},
            status=status.HTTP_401_UNAUTHORIZED
        )


class AdvertisementAPIView(APIView):
    def validate_token(self, token):
        try:
            auth_token = AuthToken.objects.get(key=token)
            if auth_token.expires_at and auth_token.expires_at < timezone.now():
                return False
            return True
        except AuthToken.DoesNotExist:
            return False

    def get(self, request, ad_id):
        if 'Authorization' not in request.headers:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

        auth_header = request.headers['Authorization']
        if not auth_header.startswith('Bearer '):
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

        token = auth_header.split('Bearer ')[1]
        if not self.validate_token(token):
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            advertisement = Advertisement.objects.get(id=ad_id)
        except Advertisement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AdvertisementSerializer(advertisement)
        return Response(serializer.data)
