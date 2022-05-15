from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from .serializers import ProductSerializer, BrandSerializer, LabelSerializer, CategorySerializer
from .models import Product, Brand, Label, Category
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# Product
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    # def get(self, request):
    #     orders = Product.objects.all()
    #     serializer = ProductSerializer(orders, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)


class ProductPut(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    # def post(self, request, *args, **kwargs):
    #     serializer = ProductSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    # def get_queryset(self):
    #     pk = self.request.GET.get("pk")
    #     return Product.objects.get(pk=pk)

    # def retrieve(self, request, *args, **kwargs):
    #     pk = self.kwargs.get('pk')
    #     queryset = Product.objects.get(pk=kwargs['pk'])
    #     serializer_class = ProductSerializer()
    #     return Response(serializer_class.data)


# Brand
class BrandList(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [AllowAny]


class BrandPut(generics.CreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [AllowAny]


class BrandDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'pk'


# Category

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class CategoryPut(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'


# Label
class LabelList(generics.ListAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    permission_classes = [AllowAny]


class LabelPut(generics.CreateAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    permission_classes = [AllowAny]


class LabelDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    lookup_field = 'pk'
#
# class UserDetail(generics.ListCreateAPIView):
#     """
#         List all users, or create a new user.
#     """
#     permission_classes = [AllowAny]
#
#     def get(self, request):
#         users = User.objects.all()
#         users_serializer = UserSerializer(users, many=True)
#         return JsonResponse(users_serializer.data, safe=False)
#
#     def post(self, request, *args, **kwargs):
#         serializer = RegisterUserSerializer(data=request.data)
#         if serializer.is_valid():
#             self.perform_create(serializer)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class UserDetail(APIView):
#     """
#         Retrieve, update or delete a user instance.
#     """
#     permission_classes = [IsAuthenticated]
#
#     def get_object(self, pk):
#         try:
#             return User.objects.get(id=pk)
#         except User.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         user = self.get_object(pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
#
#     def put(self, requesl, pk, format=None):
#         user = self.get_object(pk)
#         serializer = UserSerializer(user, data=requesl.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         user = self.get_object(pk)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
