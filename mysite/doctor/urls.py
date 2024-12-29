from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import SpecializationViewSet, DesignationViewSet, AvailableTimeViewSet, DoctorViewSet, ReviewViewSet

router = DefaultRouter()

router.register('specialization', SpecializationViewSet)
router.register('designation', DesignationViewSet)
router.register('available_time', AvailableTimeViewSet)
router.register('list', DoctorViewSet)
router.register('reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]