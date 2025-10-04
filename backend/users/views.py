from rest_framework import generics, permissions
from .serializers import UserRegistrationSerializer, UserSerializer
from .models import User

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permissions_classes = (permissions.AllowAny,)