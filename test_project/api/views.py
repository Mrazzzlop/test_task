from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework_simplejwt.tokens import AccessToken

from ads.models import Advertisement, User
from .serializers import AdvertisementSerializer, UserSerializer

from rest_framework.authentication import TokenAuthentication


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
            token = str(AccessToken.for_user(user))  # Convert to string
            return Response({'token': token})
        return Response({
            'error': 'Invalid credentials'},
            status=status.HTTP_401_UNAUTHORIZED
        )


class AdvertisementAPIView(APIView):
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
