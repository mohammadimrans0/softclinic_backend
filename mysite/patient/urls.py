from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PatientViewSet, UserRegistrationApiView, UserLoginApiView, UserLogoutApiView, activate

router = DefaultRouter()

router.register('list', PatientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationApiView.as_view(), name='register'),
    path('login/', UserLoginApiView.as_view(), name='login'),
    path('logout/', UserLogoutApiView.as_view(), name='logout'),
    path('activate/<uid64>/<token>/', activate, name='activate')
]