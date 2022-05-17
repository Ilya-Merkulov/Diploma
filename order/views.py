from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from .serializers import OrderSerializer, ShippingAddressSerializer, OrderStatusSerializer
from .models import Order, OrderStatus, ShippingAddress
from rest_framework import generics
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status


# OrderStatus
class OrderStatusList(generics.ListAPIView):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer
    permission_classes = [AllowAny]


class OrderStatusPut(generics.CreateAPIView):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer
    permission_classes = [AllowAny]


class OrderStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer
    lookup_field = 'pk'


# ShippingAddressSerializer
class ShippingAddressList(generics.ListAPIView):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
    permission_classes = [AllowAny]


class ShippingAddressPut(generics.CreateAPIView):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
    permission_classes = [AllowAny]


class ShippingAddressDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
    lookup_field = 'pk'


# Order
class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]


class OrderPut(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'pk'
