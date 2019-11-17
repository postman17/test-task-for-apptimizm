from django.urls import path

from .views import AddCarInSystemView, CarListView, AddCarToUser

urlpatterns = [
    path('add-in-sys/', AddCarInSystemView.as_view(), name='add-in-sys'),
    path('car-list/', CarListView.as_view(), name='car-list'),
    path('add-car-to-user/<pk>', AddCarToUser.as_view(), name='add-car-to-user'),
]