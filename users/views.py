from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserRegisterModelSerializer,UserInfoModelSerializer
from django.contrib.auth.models import User


class UserRegisterCreateAPIView(generics.CreateAPIView):
    serializer_class = UserRegisterModelSerializer
    permission_classes = [AllowAny]


class UserInfoDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = UserInfoModelSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    

