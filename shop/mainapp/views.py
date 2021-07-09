# from rest_framework import generics, permissions
# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters, status

from mainapp.models import Category, Product, CartProduct, Cart, Order, Customer
from mainapp.serializers import CategorySerializer, ProductSerializer, CartProductSerializer, CartSerializer, OrderSerializer, CustomerSerializer
from mainapp.permissions import IsAdminOrReadOnly

# class LogOut(APIView):

#     def get(self, request, format=None):
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)



class CategoryView(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'pk'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    permission_classes = (IsAdminOrReadOnly)

class CustomerView(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    lookup_field = 'pk'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class ProductView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'pk'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class CartProductView(ModelViewSet):
    serializer_class = CartProductSerializer
    queryset = CartProduct.objects.all()
    lookup_field = 'pk'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class CartView(ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    lookup_field = 'pk'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class OrderView(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = 'pk'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']