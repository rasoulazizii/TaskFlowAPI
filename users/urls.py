from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegisterCreateAPIView.as_view(), name='user-register'),
    path('me/', views.UserInfoDetailView.as_view(), name='user-info'),
]
