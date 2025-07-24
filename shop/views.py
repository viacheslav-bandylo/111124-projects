from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from shop.models import Category, Supplier
from shop.serializers import *


class CategoryViewSet(viewsets.ModelViewSet):
    """
    Это представление предоставляет полный набор действий (CRUD) для модели Category.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class SupplierViewSet(viewsets.ModelViewSet):
    """
    Это представление предоставляет полный набор действий (CRUD) для модели Supplier.
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class ProductListCreateView(ListCreateAPIView):
    """
    Представление для получения списка продуктов и создания нового продукта.
    """
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'price']

    # Явно указываем классы аутентификации для этого представления.
    # Это переопределит глобальные настройки, если они есть.
    # authentication_classes = [BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    authentication_classes = [JWTAuthentication]

    # Явно указываем классы разрешений для этого представления.
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Этот метод позволяет нам динамически выбирать сериалайзер
    def get_serializer_class(self):
        # Для безопасных методов (только чтение), таких как GET
        if self.request.method == 'GET':
            return ProductSerializer
        # Для остальных методов (POST)
        return ProductCreateUpdateSerializer


class ProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    Представление для просмотра, обновления и удаления одного продукта.
    """
    queryset = Product.objects.all()

    # Явно указываем классы разрешений для этого представления.
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        # Для чтения данных
        if self.request.method == 'GET':
            return ProductSerializer
        # Для изменения или удаления (PUT, PATCH, DELETE)
        return ProductCreateUpdateSerializer


class ProductDetailViewSet(viewsets.ModelViewSet):
    queryset = ProductDetail.objects.all()
    # Явно указываем классы разрешений для этого представления.
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Этот метод позволяет нам динамически выбирать сериалайзер
    def get_serializer_class(self):
        # Для безопасных методов (только чтение), таких как GET
        if self.request.method == 'GET':
            return ProductDetailSerializer
        # Для остальных методов
        return ProductDetailCreateUpdateSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    # Явно указываем классы разрешений для этого представления.
    permission_classes = [IsAdminUser]


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()

    # Явно указываем классы разрешений для этого представления.
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CustomerSerializer
        return CustomerCreateUpdateSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()

    # Явно указываем классы разрешений для этого представления.
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderSerializer
        return OrderCreateUpdateSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()

    # Явно указываем классы разрешений для этого представления.
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderItemSerializer
        return OrderItemCreateUpdateSerializer

