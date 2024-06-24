from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken

from ads.models import Advertisement, User, AuthToken
from .serializers import AdvertisementSerializer, UserSerializer
from .permissions import BearerTokenPermission


class RegisterView(APIView):
    """Вью Регистрации"""
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            token = str(AccessToken.for_user(serializer.instance))
            return Response({'token': token})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """Вью Авторизации"""
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
    """Вью Объявления"""
    permission_classes = [BearerTokenPermission]

    def get(self, request, ad_id):
        try:
            advertisement = Advertisement.objects.get(id=ad_id)
        except Advertisement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AdvertisementSerializer(
            advertisement,
            context={'request': request}
        )
        return Response(serializer.data)
