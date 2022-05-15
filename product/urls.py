from django.urls.conf import path
from .views import ProductList, ProductPut, ProductDetail, CategoryList, CategoryPut, \
    CategoryDetail, BrandList, BrandPut, BrandDetail, LabelList, LabelPut, LabelDetail


urlpatterns = [
    path('product/', ProductList.as_view(), name=''),
    path('product/create/', ProductPut.as_view(), name=''),
    path('product/<int:pk>/', ProductDetail.as_view(), name=''),

    path('category/', CategoryList.as_view(), name=''),
    path('category/create/', CategoryPut.as_view(), name=''),
    path('category/<int:pk>/', CategoryDetail.as_view(), name=''),

    path('brand/', BrandList.as_view(), name=''),
    path('brand/create/', BrandPut.as_view(), name=''),
    path('brand/<int:pk>/', BrandDetail.as_view(), name=''),

    path('label/', LabelList.as_view(), name=''),
    path('label/create/', LabelPut.as_view(), name=''),
    path('label/<int:pk>/', LabelDetail.as_view(), name=''),
    # path('product/', include('product.urls')),

]
