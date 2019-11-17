from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers

from .viewsets import CustomAuthToken, UserViewSet, UserCarsViewSet

from .views import ProfileView, RegistrationView, ProfileUpdateView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'cars', UserCarsViewSet, base_name='UserCars')

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile-edit/<pk>', ProfileUpdateView.as_view(), name='profile-edit'),
    path('register/', RegistrationView.as_view(), name='register'),
    url(r'^auth/', CustomAuthToken.as_view()),
    url(r'^', include(router.urls)),
]
