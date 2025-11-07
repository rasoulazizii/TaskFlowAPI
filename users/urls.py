from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('register/', views.UserRegisterCreateAPIView.as_view(), name='user-register'),
    path('me/', views.UserInfoDetailView.as_view(), name='user-info'),
    path('token/', TokenObtainPairView.as_view(), name='access-token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),


]
