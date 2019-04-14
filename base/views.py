from django.http import HttpResponse
from rest_framework import generics, mixins

from .models import UserProfile, BaseCountry, BaseProvince, BaseUnit, Company
from .serializer import UserRegisterSerializer, CountrySerializer, \
    ProvinceSerializer, BaseUnitSerializer, CompanySerializer


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


class UnitListView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = BaseUnit.objects.all()
    serializer_class = BaseUnitSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CompanyListView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Company.objects.filter(is_active=True)
    serializer_class = CompanySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# ----------------------------------------------------------------------------------------------------------------------

def test_function_view(request):
    user = UserProfile.objects.all()

    for u in user:
        u.delete()

    return HttpResponse('200 OK', content_type='text/plain', status=200)
