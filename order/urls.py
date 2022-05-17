from django.urls.conf import path
from .views import OrderStatusList, OrderStatusPut, OrderStatusDetail, \
    ShippingAddressList, ShippingAddressPut, ShippingAddressDetail, \
    OrderList, OrderPut, OrderDetail


urlpatterns = [
    path('order/', OrderList.as_view(), name=''),
    path('order/create/', OrderPut.as_view(), name=''),
    path('order/<int:pk>/', OrderDetail.as_view(), name=''),

    path('order_status/', OrderStatusList.as_view(), name=''),
    path('order_status/create/', OrderStatusPut.as_view(), name=''),
    path('order_status/<int:pk>/', OrderStatusDetail.as_view(), name=''),

    path('shipping_address/', ShippingAddressList.as_view(), name=''),
    path('shipping_address/create/', ShippingAddressPut.as_view(), name=''),
    path('shipping_address/<int:pk>/', ShippingAddressDetail.as_view(), name='')
]
