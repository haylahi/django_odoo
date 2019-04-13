from rest_framework import generics, mixins

from .models import UserProfile, BaseCountry, BaseProvince
from .serializer import UserRegisterSerializer, CountrySerializer, ProvinceSerializer


class UserRegisterView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = UserProfile.objects.filter(is_active=True)
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class BaseCountryListView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = BaseCountry.objects.all()
    serializer_class = CountrySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CountryDetailView(generics.GenericAPIView,
                        mixins.UpdateModelMixin,
                        mixins.RetrieveModelMixin):
    queryset = BaseCountry.objects.all()
    serializer_class = CountrySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class ProvinceListView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = BaseProvince.objects.all()
    serializer_class = ProvinceSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProvinceDetailView(generics.GenericAPIView,
                         mixins.UpdateModelMixin,
                         mixins.RetrieveModelMixin):
    queryset = BaseProvince.objects.all()
    serializer_class = ProvinceSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
