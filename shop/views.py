from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response

from shop.models import Category, Supplier
from shop.permissions import IsOwnerOrReadOnly, CanViewOrderStatistics
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
    authentication_classes = [BasicAuthentication]
    # Явно указываем классы разрешений для этого представления.
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        """
        Этот метод определяет список объектов для отображения.
        Мы фильтруем заказы, оставляя только те, где поле `user`
        совпадает с текущим пользователем.
        Таким образом, каждый пользователь видит только свои заказы.
        """
        return Order.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderSerializer
        return OrderCreateUpdateSerializer

    # Переопределяем метод perform_create
    def perform_create(self, serializer):
        """
        При создании заказа мы автоматически подставляем текущего пользователя
        в поле `user`. `self.request.user` — это и есть текущий
        авторизованный пользователь.
        """
        serializer.save(user=self.request.user)


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()

    # Явно указываем классы разрешений для этого представления.
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderItemSerializer
        return OrderItemCreateUpdateSerializer


class OrderStatisticsView(APIView):
    # Применяем наше новое разрешение и IsAuthenticated
    permission_classes = [IsAuthenticated, CanViewOrderStatistics]

    def get(self, request):
        total_orders = Order.objects.count()
        data = {
            'total_orders': total_orders,
        }
        return Response(data)

