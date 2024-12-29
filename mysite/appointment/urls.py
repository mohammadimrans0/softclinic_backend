from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import AppointmentViewSet

router = DefaultRouter()

router.register('list', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]