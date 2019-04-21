# author: Liberty
# date: 2019/4/21 15:37

from django.urls import path

from . import views as v

urlpatterns = [
    path('brand/', v.BrandCreateListView.as_view()),
    path('category/', v.CategoryCreateListView.as_view()),
    path('product/', v.ProductCreateListView.as_view()),
    path('product_price_list/', v.ProductPriceListCreateListView.as_view()),
    path('product_price_item/', v.ProductPriceItemCreateListView.as_view()),

    path('looks_type/', v.AppearanceTypeCreateListView.as_view()),
    path('looks_group/', v.AppearanceGroupListCreateView.as_view()),
    path('looks_item/', v.AppearanceItemCreateListView.as_view()),
]
