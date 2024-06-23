from django.urls import path
from .views import AdvertisementAPIView, LoginView, RegisterView

app_name = 'api'

urlpatterns = [
    path('advertisements/<int:ad_id>/', AdvertisementAPIView.as_view()),
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view())
]
