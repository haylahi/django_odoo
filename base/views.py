from rest_framework import generics, mixins

from .models import UserProfile, BaseCountry
from .serializer import UserRegisterSerializer, CountrySerializer


class UserRegisterView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = UserProfile.objects.filter(is_active=True)
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class BaseCountryView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = BaseCountry.objects.all()
    serializer_class = CountrySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
