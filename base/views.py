from django.http import HttpResponse
from rest_framework import generics, mixins

from .models import UserProfile, BaseCountry, BaseProvince, BaseUnit, Company, BaseTax, Currency, CurrencyRate, Partner, BaseCity, BaseSequence
from .serializer import UserRegisterSerializer, CountrySerializer, \
    ProvinceSerializer, BaseUnitSerializer, CompanySerializer, BaseTaxSerializer, \
    CurrencySerializer, CurrencyRateSerializer, PartnerSerializer, CitySerializer, BaseSequenceSerializer


class UserRegisterView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = UserProfile.objects.filter(is_active=True)
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class BaseCountryListView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = BaseCountry.objects.filter(is_active=True)
    serializer_class = CountrySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CountryDetailView(generics.GenericAPIView,
                        mixins.UpdateModelMixin,
                        mixins.RetrieveModelMixin):
    queryset = BaseCountry.objects.filter(is_active=True)
    serializer_class = CountrySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class ProvinceListView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = BaseProvince.objects.filter(is_active=True)
    serializer_class = ProvinceSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProvinceDetailView(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    queryset = BaseProvince.objects.filter(is_active=True)
    serializer_class = ProvinceSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class CityListView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = BaseCity.objects.filter(is_active=True)
    serializer_class = CitySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UnitListView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = BaseUnit.objects.filter(is_active=True)
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


class PartnerListView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Partner.objects.filter(is_active=True)
    serializer_class = PartnerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TaxListView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = BaseTax.objects.filter(is_active=True)
    serializer_class = BaseTaxSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CurrencyListView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Currency.objects.filter(is_active=True)
    serializer_class = CurrencySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CurrencyRateListView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = CurrencyRate.objects.filter(is_active=True)
    serializer_class = CurrencyRateSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BaseSequenceListView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = BaseSequence.objects.filter(is_active=True)
    serializer_class = BaseSequenceSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# ----------------------------------------------------------------------------------------------------------------------


def test_function_view(request):
    ret = BaseSequence.generate_next_code_by_name('test.test01')
    return HttpResponse('<h2>200  OK </h2>\n <h2>{s}</h2>'.format(s=ret), content_type='text/html', status=200)
