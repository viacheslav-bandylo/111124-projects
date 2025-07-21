from django.shortcuts import render
from rest_framework import viewsets

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
