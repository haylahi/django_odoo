from rest_framework import generics, mixins

from .models import UserProfile
from .serializer import UserRegister


class UserRegisterView(generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = UserProfile.objects.filter(is_active=True)
    serializer_class = UserRegister

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
